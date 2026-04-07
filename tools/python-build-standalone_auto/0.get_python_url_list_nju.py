#!/usr/bin/env python3

import requests
import os
from html.parser import HTMLParser
from urllib.parse import urljoin,unquote

current_dir = os.path.dirname(os.path.abspath(__file__))

python_url = r'https://mirror.nju.edu.cn/github-release/astral-sh/python-build-standalone/LatestRelease/'

class DownloadLinkParser(HTMLParser):
    '''定义一个继承自 HTMLParser 的类，用于处理 HTML 标签'''
    def __init__(self, base_url:str):
        super().__init__()
        self.base_url = base_url
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for attr, value in attrs:
                if attr == 'href':
                    if value and value != '../' and not value.endswith('/'):
                        full_url = urljoin(self.base_url, value)
                        self.links.append(full_url)

def get_download_url(url:str):
    '''生成下载链接'''
    response = requests.get(url)
    parser = DownloadLinkParser(url)
    parser.feed(response.text)
    return parser.links


def post_filter(links:list):
    '''后过滤器'''
    file_urls = []
    for i in links:
        if any(i.endswith(suffix) for suffix in ['.zst','.tar.gz']) \
        and any(target in i for target in ['linux','windows'] ) \
            and any(arch in i for arch in ['aarch64','x86_64'] ):
            if i not in file_urls:
                file_urls.append(unquote(i))
    return file_urls

with open(f'{current_dir}/0.python_url_nju.txt','w') as f:
    for i in post_filter(get_download_url(python_url)):
        f.write(i+'\n')