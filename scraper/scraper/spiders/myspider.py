import scrapy
from scrapy.crawler import CrawlerProcess
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from scrapy.http import HtmlResponse
import time

class SeleniumMiddleware(object):
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    def process_request(self, request, spider):
        self.driver.get(request.url)
        time.sleep(3)
        body = self.driver.page_source
        return HtmlResponse(self.driver.current_url, body=body, encoding='utf-8', request=request)

    def spider_closed(self, spider):
        self.driver.quit()

class MySpider(scrapy.Spider):
    name = 'my_spider'
    allowed_domains = ['multy.ai']
    start_urls = ['https://multy.ai/']

    custom_settings = {
        'DOWNLOADER_MIDDLEWARES': {'__main__.SeleniumMiddleware': 800},
    }

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text(separator=' ', strip=True)
        text = text.replace('You need to enable JavaScript to run this app.', '')
        filename = f'{self.name}.txt'
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(text)
        self.log(f'Saved file {filename}')

if __name__ == "__main__":
    process = CrawlerProcess(settings={
        'LOG_LEVEL': 'INFO',
    })
    process.crawl(MySpider)
    process.start()
