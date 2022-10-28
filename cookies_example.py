from quickscraper_sdk import QuickScraper
client = QuickScraper('ENTER_YOUR_ACCESS_TOKEN')
result = client.getHtml(url='http://httpbin.org/cookies',
                        keep_headers=True,
                        headers={'Cookie': 'key1=value1;key2=value2;key3=value3'}).text
print(result)
