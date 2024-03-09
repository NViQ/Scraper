import scrapy
from scrapy.crawler import CrawlerProcess
from bs4 import BeautifulSoup


class MySpider(scrapy.Spider):
    name = 'my_spider'
    allowed_domains = ['multy.ai']
    start_urls = ['https://multy.ai/']


    def parse(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text(separator=' ', strip=True)
        text = text.replace('You need to enable JavaScript to run this app.', '')
        filename = f'{self.name}.txt'
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(text)
        self.log(f'Saved file {filename}')

# if __name__ == "__main__":
#     process = CrawlerProcess(settings={
#         'LOG_LEVEL': 'INFO',
#     })
#     process.crawl(MySpider)
#     process.start()
