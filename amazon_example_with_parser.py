from quickscraper_sdk import QuickScraper
quickscraper_client = QuickScraper('ENTER_YOUR_ACCESS_TOKEN')
response = quickscraper_client.getHtml('https://www.amazon.es/deals', parserSubscriptionId='PARSER_SUBSCRIPTION_ID')
print(response.text)