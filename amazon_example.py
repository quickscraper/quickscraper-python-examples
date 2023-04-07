from quickscraper_sdk import QuickScraper
client = QuickScraper('AVkwSQEmFJ3C3nIGPwkaitP05')
result = client.getHtml(url = 'https://www.amazon.com/dp/B08QMB94YW').text
print(result)