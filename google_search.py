import requests
from bs4 import BeautifulSoup
import csv
import json

access_token = 'L5vCo5nM4n13B7pI1J8fWZYNh' #access_token = Get you access token from app.quickscraper.co
url = f"https://api.quickscraper.co/parse?access_token={access_token}&url=https://www.google.com/search?q=laptop"

print(url)
response = requests.get(url)
html_content = response.content

soup = BeautifulSoup(html_content, 'html.parser')

items = soup.find_all('div', class_=['g', 'Ww4FFb', 'vt6azd','asEBEc', 'tF2Cxc'])

google_search_items = []

for item in items:
    title = item.find('h3', class_=['LC20lb','MBeuO', 'DKV0Md']).text.strip() if item.find('h3', class_=['LC20lb','MBeuO', 'DKV0Md']) else None
    desciption = item.find('div', class_=['VwiC3b', 'yXK7lf', 'lVm3ye', 'r025kc', 'hJNv6b', 'Hdw6tb']).text.strip() if item.find('h3', class_=['VwiC3b', 'yXK7lf', 'lVm3ye', 'r025kc', 'hJNv6b', 'Hdw6tb']) else None
    url_element = item.find('a', {'class': '.UWckNb'})
    url = url_element.get('href') if url_element else None

    foundItem = {
        "title": title,
        "desciption": desciption,
        "url": url,
    }
    google_search_items.append(foundItem)


with open("google_search_items.json", "w") as file:
    json.dump(google_search_items, file, indent=4)


