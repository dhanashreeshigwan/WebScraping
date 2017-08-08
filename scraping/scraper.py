import time
import json
import requests

from bs4 import BeautifulSoup
from selenium import webdriver

URL = "https://www.nseindia.com/live_market/dynaContent/live_analysis/top_gainers_losers.htm?cat=G"

class WebScraper(object):

    def __init__(self):
        self.browser = webdriver.PhantomJS(service_args=['--ignore-ssl-errors=true', '--ssl-protocol=TLSv1'])

    def make_request(self):
        """
        Makes http request to given url with params
        """
        self.browser.get(URL)

    def parse_response(self):
        """
        Parses table from html source
        """

        soup = BeautifulSoup(self.browser.page_source, 'html.parser')
        table = soup.find("table", {"id": "topGainers"})
        headers = [th.get_text(strip=True)for th in table.find_all('th')]
        headers = [w.replace(' ', '') for w in headers]
        headers = [w.replace('%', '') for w in headers]
        headers = [w.replace('.', '') for w in headers]
        headers = [w.replace('(', '') for w in headers]
        headers = [w.replace(')', '') for w in headers]
        response = []

        for tr in table.find_all('tr'):
            row = [td.get_text(strip=True)for td in tr.find_all('td')]
            if row:
                response.append(dict(zip(headers, row)))

        return response

    def get_nifty_50_table(self):
        """
        Returns nifty_50 table in json format
        """

        self.make_request()
        return self.parse_response()