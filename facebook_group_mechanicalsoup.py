import mechanicalsoup
import requests
from bs4 import BeautifulSoup
import csv
import json

# Connect to Website
browser = mechanicalsoup.StatefulBrowser()
access_token = 'L5vConM41B7pI1fWZYNh' #access_token = Get you access token from app.quickscraper.co
url = f"https://api.quickscraper.co/parse?access_token={access_token}&url=https://www.facebook.com/groups/2770323333294139/"
page = browser.get(url)


# Parse HTML
soup = BeautifulSoup(page.content, 'html.parser')

with open('output.html', 'w', encoding='utf-8') as file:
    file.write(str(soup))

posts = soup.find_all('div', class_=['x1yztbdb', 'x1n2onr6', 'xh8yej3', 'x1ja2u2z'])

post_items = []

for post in posts:
    userName = post.find('h3', class_=['x1heor9g' ,'x1qlqyl8' ,'x1pd3egz' ,'x1a2a7pz' ,'x1gslohp' ,'x1yc453h']).text.strip() if post.find('h3', class_=['x1heor9g' ,'x1qlqyl8' ,'x1pd3egz' ,'x1a2a7pz' ,'x1gslohp' ,'x1yc453h']) else None
    desciption = post.find('div', class_=['x1iorvi4', 'x1pi30zi','x1l90r2v' ,'x1swvt13']).text.strip() if post.find('div', class_=['x1iorvi4', 'x1pi30zi','x1l90r2v' ,'x1swvt13']) else None
    likes = post.find('span', class_=['xrbpyxo' ,'x6ikm8r', 'x10wlt62' ,'xlyipyv' ,'x1exxlbk']).text.strip() if post.find('span', class_=['xrbpyxo' ,'x6ikm8r', 'x10wlt62' ,'xlyipyv' ,'x1exxlbk']) else None

    foundItem = {
        "userName": userName,
        "desciption": desciption,
        "likes": likes,
    }
    post_items.append(foundItem)


with open("post_items.json", "w") as file:
    json.dump(post_items, file, indent=4)