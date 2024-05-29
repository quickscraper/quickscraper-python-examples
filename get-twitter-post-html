from quickscraper_sdk import QuickScraper
import json

access_token = 'YOUR_ACCESS_TOKEN' #access_token = Get you access token from app.quickscraper.co

quickscraper_client = QuickScraper(access_token)
response = quickscraper_client.getHtml(
  'https://x.com/Ticketmaster/status/1712878623253057713')
print(response._content)
