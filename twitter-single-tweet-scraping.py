from quickscraper_sdk import QuickScraper
import json

access_token = 'YOUR_ACCESS_TOKEN' #access_token = Get you access token from app.quickscraper.co

quickscraper_client = QuickScraper(access_token)
response = quickscraper_client.getHtml(
  'https://x.com/Ticketmaster/status/1712878623253057713',
   parserSubscriptionId='99590f57-571a-5f9a-b6f3-74a00436707a' # Get your parser subscription id from app.quickscraper.co/user/request
   )
print(response._content['data'])
