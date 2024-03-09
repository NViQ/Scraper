Scraper
scrapy+selenium+bs4

You should run:

[myspider.py](./scraper/scraper/spiders/myspider.py)

Before launching the module, you must put the Site that you want to scrape into variables
```

  allowed_domains = 

  start_urls =

```

for Docker:

```
   docker build -t scraper .
  
   docker run scraper  
```

for new file - my_spider.txt

```
    docker cp <CONTAINER_ID>:/app/my_spider.txt <LOCAL_PATH>
```