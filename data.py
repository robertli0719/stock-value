# -*- coding: utf-8 -*-
"""
从yahoo finance下载网页数据，并提取有用信息。
如果当前一小时内重复发起抓数据，那么直接读取本地缓存

@author: robert
"""

from bs4 import BeautifulSoup
import urllib.request
import datetime
import storage


def __file_key(ticker):
    now = datetime.datetime.now()
    now_str = str(now.year)+"-"+str(now.month) + \
        "-"+str(now.day)+"-"+str(now.hour)
    return ticker+"-"+now_str


def __pick_url(ticker):
    return "https://finance.yahoo.com/quote/" + ticker + "/key-statistics"


def __pick_html(ticker):
    url = __pick_url(ticker)
    with urllib.request.urlopen(url) as response:
        return response.read()


def __pick_html_file(ticker_arr):
    html_dic = {}
    for ticker in ticker_arr:
        key = __file_key(ticker)
        if not storage.has(key):
            html = __pick_html(ticker)
            storage.put(key, html)
        html = storage.get(key)
        html_dic[ticker] = html
    return html_dic


def __pick_val_out(soup, title):
    tr = soup.find_all("span", text=title)[0].parent.parent
    return tr.td.next_sibling.string


def __pick_values(html, title_arr):
    values = {}
    soup = BeautifulSoup(html, features="html.parser")
    for title in title_arr:
        val = __pick_val_out(soup, title)
        values[title] = val
    return values


def pick_data(ticker_arr, title_arr):
    data = {}
    html_files = __pick_html_file(ticker_arr)
    for ticker in ticker_arr:
        html = html_files[ticker]
        values = __pick_values(html, title_arr)
        data[ticker] = values
    return data
