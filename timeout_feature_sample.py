from quickscraper_sdk import QuickScraper
quickscraper_client = QuickScraper('ACCESS_TOKEN')
response = quickscraper_client.getHtml('https://www.google.com/', isScroll=True, scrollTimeout=30000)
print(response.content)