# -*- coding: utf-8 -*-
from urllib.request import urlopen
import re

from bs4 import BeautifulSoup

def crawl_url_soup(url):
    page = urlopen(url).read()
    return BeautifulSoup(page, 'lxml')

def main():
    url = 'https://rate.bot.com.tw/xrt'
    soup = crawl_url_soup(url)
    trs = soup.select('table tr')
    for tr in trs:
        if 'JPY' in tr.text:
            tds = tr.select('td.rate-content-cash')
            print(float(tds[1].text))
            return

if __name__ == '__main__':
    main()
