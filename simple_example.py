from quickscraper_sdk import QuickScraper
client = QuickScraper('ACCESS_TOKEN')
result = client.getHtml(url = 'http://httpbin.org/ip').text
print(result)