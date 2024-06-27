
from quickscraper_sdk import QuickScraper
quickscraper_client = QuickScraper('ACCESS_TOKEN')
response = quickscraper_client.getHtml('https://www.google.com/',keepSelection=True,customSelectors=[{
				'isScript': 'BOOLEAN',
				'options':'click',
				'selectorScript':'SELECT_INPUT',
				}]
			)
print(response.content)
