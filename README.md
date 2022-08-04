# quickscraper-python-examples

- Create a scrapy project
```
scrapy startproject amazon_scraper
```

- Generate a spider
```
scrapy genspider amazon amazon.com
```

- Crawl spider and get response in json file
```
scrapy crawl amazon -O response.json
```
