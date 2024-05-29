from quickscraper_sdk import QuickScraper
import json

access_token = 'L5vCo5nM4n13B7pI1J8fWZYNh' #access_token = Get you access token from app.quickscraper.co

quickscraper_client = QuickScraper(access_token)
response = quickscraper_client.writeHtmlToFile(
  'https://x.com/Ticketmaster/status/1712878623253057713', file_path='filename.html')
print(response._content)
