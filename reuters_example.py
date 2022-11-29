from bs4 import BeautifulSoup
from quickscraper_sdk import QuickScraper


def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def get_data(contents, *vars):
    soup = BeautifulSoup(contents, 'lxml')
    scripts = soup.find_all(
        "script", {"id": "fusion-metadata"})[0].text.strip()
    clean_data = []
    output = dict()
    for var in vars:
        for i in scripts.split(";")[7].split("=")[1].split(","):
            clean_data.append(i.strip("""[ | " , \ / {} "]"""))
        for i in clean_data:
            if len(i) >= len(var):
                if i[:len(var)] == var:
                    if isfloat(i[len(var):].strip("""[ : | " , \ / {} "]""")):
                        output[var] = float(i[len(var):].strip(
                            """[ : | " , \ / {} "]"""))

    for var in vars:
        if var not in output:
            output[var] = None

    return output


def execute():
    try:
        client = QuickScraper('ACCESS_TOKEN')
        result = client.getHtml(
            url='https://www.reuters.com/markets/companies/INTC.N/key-metrics/per-share-data').text
        print(result)
        var = ["eps_excl_extra_annual", "eps_basic_excl_extra_annual",
               "eps_excl_extra_anual", "tangible_book_annual"]
        print(get_data(result, *var))
    except Exception as error:
        print('error ', error)


if __name__ == "__main__":
    execute()
