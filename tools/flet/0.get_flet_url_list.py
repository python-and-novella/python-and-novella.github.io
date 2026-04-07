#!/usr/bin/env python3

import requests,json,os
from urllib.parse import unquote

current_dir = os.path.dirname(os.path.abspath(__file__))

python_url = r'https://api.github.com/repos/flet-dev/flet/releases/latest'
# 如果是预发行版本，需要指定具体tag
#python_url = r'https://api.github.com/repos/flet-dev/flet/releases/tags/v0.83.1'

def get_download_url_git(url):
    response = requests.get(url)
    content = response.text
    json_obj = json.loads(content)
    file_urls = []
    for i in json_obj["assets"]:
        browser_download_url = i["browser_download_url"]
        file_urls.append(unquote(browser_download_url))
    alt_url = r'https://ghfast.top/'
    return [ alt_url+i for i in file_urls ]

with open(f'{current_dir}/0.flet_url.txt','w') as f:
    for i in get_download_url_git(python_url):
        f.write(i+'\n')



