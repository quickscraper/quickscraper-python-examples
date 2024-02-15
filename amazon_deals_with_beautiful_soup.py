import requests
from bs4 import BeautifulSoup
import json

access_token = 'L5vCo5nM4n13B7pI1J8fWZYNh' #access_token = Get you access token from app.quickscraper.co
url = f"https://api.quickscraper.co/parse?access_token={access_token}&url=https://www.amazon.com/deals" 
response = requests.get(url)

with open('amazon_deals.html', 'w', encoding='utf-8') as file:
    file.write(response.text)

soup = BeautifulSoup(response.text, 'html.parser')

# Find all divs containing the desired class pattern
deal_items = soup.find_all('div', class_=lambda x: x and 'DealGridItem-module__' in x)

data = []
# Loop through the divs to find the titles
for item in deal_items:
    title_element = item.select('div[class*=DealContent-module__truncate_]')
    for title_ele in title_element:
      title = title_ele.text.strip()
      data.append({
            'title': title
        })

print(data)
with open('amazon_product.json', 'w') as f:
    json.dump(data, f)