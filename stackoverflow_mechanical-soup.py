import mechanicalsoup
import requests
from bs4 import BeautifulSoup
import csv

# Connect to Website
browser = mechanicalsoup.StatefulBrowser()
access_token = 'L5vCo54n13BpI1J8WZYNh' #access_token = Get you access token from app.quickscraper.co
url = f"https://api.quickscraper.co/parse?access_token={access_token}&url=https://stackoverflow.com/"
page = browser.get(url)

# Parse HTML
soup = BeautifulSoup(page.content, 'html.parser')

# Extract Data
headers = soup.find_all('h2')

# Print Headers
for header in headers:
    print(header.get_text())

# Save Scraped Data to CSV
data_to_save = [["headers",'headers2']]
for header in headers:
    data_to_save.append([header.get_text()])

with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data_to_save)

print("Data saved to data.csv")