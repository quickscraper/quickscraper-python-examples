from quickscraper_sdk import QuickScraper
quickscraper_client = QuickScraper('YLvVRa54d4wZuRwx9DtAy4SYH')
response = quickscraper_client.getData('https://www.amazon.com/Apple-iPhone-Mini-128GB-Black/dp/B08PNKN4J7?th=1', parserSubscriptionId='e65296a6-1849-5858-8564-5dc16472db89')
print(response._content)