import requests
from bs4 import BeautifulSoup
import csv
import json

access_token = 'L5vCo54n1B7p1J8fZYNh' #access_token = Get you access token from app.quickscraper.co
url = f"https://api.quickscraper.co/parse?access_token={access_token}&url=https://www.ebay.com/sch/i.html?_nkw=mobile"

print(url)
response = requests.get(url)
html_content = response.content
soup = BeautifulSoup(html_content, 'html.parser')

productItems = soup.find_all('li', class_=['s-item','s-item__pl-on-bottom'])

products = []

for product in productItems:
    title = product.find('span', role=['heading']).text.strip() if product.find('span', role=['heading']) else None
    subTitle = product.find('div', class_=['s-item__subtitle']).text.strip() if product.find('div', class_=['s-item__subtitle']) else None
    price = product.find('span', class_=['s-item__price']).text.strip() if product.find('span', class_=['s-item__price']) else None
    url_element = product.find('a', {'class': 's-item__link'})
    url = url_element.get('href') if url_element else None

    foundItem = {
        "title": title,
        "subTitle": subTitle,
        "price": price,
        "url": url,
    }
    products.append(foundItem)


with open("products.json", "w") as file:
    json.dump(products, file, indent=4)
