from quickscraper_sdk import QuickScraper
accessToken = '';
client = QuickScraper(accessToken)
result = client.getHtml('https://www.tiktok.com/@khaby.lame', parserSubscriptionId='9076cfb5-6c47-54eb-9717-8846d2cdcc38').text

print(result)