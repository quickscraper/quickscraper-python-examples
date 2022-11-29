# quickscraper-python-examples

# Install QuickScraper

```
python3 -m pip install quickscraper_sdk
```

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

- Other modules
```
pip install lxml
```