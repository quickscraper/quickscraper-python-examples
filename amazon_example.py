from quickscraper_sdk import QuickScraper
client = QuickScraper('ACCESS_TOKEN')
result = client.getHtml(url = 'https://www.amazon.com/dp/B08QMB94YW').text
print(result)