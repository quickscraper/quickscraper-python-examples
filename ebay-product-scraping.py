import requests
from bs4 import BeautifulSoup
import csv


access_token = '6JQrJqjzL0MwEZ7EB4yap' #access_token = Get you access token from app.quickscraper.co
url = f"https://api.quickscraper.co/parse?access_token={access_token}&url=https://www.ebay.com/b/Outdoor-Sports/159043/bn_1855398/"

response = requests.get(url)
html_content = response.content

soup = BeautifulSoup(html_content, 'html.parser')

products = soup.find_all('li', {'class': 'carousel__snap-point'})

product_data = []

for product in products:
    title = product.find('div', {'class': 'b-info__title'}).text.strip() if product.find('div', {'class': 'b-info__title'}) else None
    price = product.find('div', {'class': 'b-info__price clearfix'}).text.strip() if product.find('div', {'class': 'b-info__price clearfix'}) else None
    url_element = product.find('a', {'class': 'b-tile'})
    url = url_element.get('href') if url_element else None

    product_data.append({
        'Title': title,
        'Price': price,
        'URL': url
    })

with open('product_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Title', 'Price', 'URL']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    for product in product_data:
        writer.writerow(product)
