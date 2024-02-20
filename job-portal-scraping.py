import requests
from bs4 import BeautifulSoup
import csv
import json
from flask import Flask, render_template


access_token = '6JQrJqzL0MEZ7EBN584yap' #access_token = Get you access token from app.quickscraper.co
url = f"https://api.quickscraper.co/parse?access_token={access_token}&url=https://www.linkedin.com/jobs/search?keywords=Account-Manager&location=Germany&position=1&pageNum=0/"

print(url)
response = requests.get(url)
html_content = response.content

soup = BeautifulSoup(html_content, 'html.parser')

jobs = soup.find_all('div', {'class': 'job-search-card'})


job_listings = []

for job_element in jobs:
    title = job_element.find('h3', {'class': 'base-search-card__title'}).text.strip() if job_element.find('h3', {'class': 'base-search-card__title'}) else None
    company = job_element.find('h4', {'class': 'base-search-card__subtitle'}).text.strip() if job_element.find('h4', {'class': 'base-search-card__subtitle'}) else None
    url_element = job_element.find('a', {'class': 'base-card__full-link'})
    url = url_element.get('href') if url_element else None
    location = job_element.find('span', {'class': 'job-search-card__location'}).text.strip() if job_element.find('span', {'class': 'job-search-card__location'}) else None

    job_listing = {
        "title": title,
        "company": company,
        "location": location,
        "url": url,
    }
    job_listings.append(job_listing)


with open("job_listings.json", "w") as file:
    json.dump(job_listings, file, indent=4)



app = Flask(__name__, template_folder='templates')


@app.route("/")
def home():
    with open("job_listings.json", "r") as file:
        job_listings = json.load(file)
    return render_template("index.html", job_listings=job_listings)

if __name__ == "__main__":
    app.run(debug=True)
