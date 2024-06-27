
from quickscraper_sdk import QuickScraper
quickscraper_client = QuickScraper('ACCESS_TOKEN')
response = quickscraper_client.getHtml('https://www.prismetric.com/job-opportunities/',keepSelection=True,customSelectors=[{
				'name':'click',
    			'isScript': 'False',
				'options':'',
				'selectorScript':'a[href="https://www.prismetric.com/taxi-booking-app-development-solutions/"]',
				}]
			)
print(response.content)
response = quickscraper_client.getHtml('https://www.prismetric.com/',keepSelection=True,customSelectors=[{
				'name':'waitForElement',
    			'isScript': 'False',
				'options':'',
				'selectorScript':'a[href="https://www.prismetric.com/mobile-app-development/"]',
				}]
			)
print(response.content)