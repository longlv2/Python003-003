#-*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import time


# 返回bs对象
def get_url(myurl):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    header = {
        'user-agent': user_agent,
        'cookie': 'uuid_n_v=v1; uuid=78016D70E35B11EA94345B95E7867004FCBF7E861048496DB7EE22322EC1B5DE; _csrf=dcc0db631d205cbef8d23d4b4ddccfd8cf56b1a14d698e165da6a9b4bffc7555; _lxsdk_cuid=174096d6d34c8-0792fd5fb08f1-c373667-144000-174096d6d34c8; _lxsdk=78016D70E35B11EA94345B95E7867004FCBF7E861048496DB7EE22322EC1B5DE; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1597886000,1597973346,1597979353; mojo-uuid=2b31650890aacf17f613a054490eee34; mojo-session-id={"id":"4a73a990d9b7d50ca4070bda99482720","time":1597979353449}; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1597979362; __mta=144137098.1597979353431.1597979353431.1597979362238.2; mojo-trace-id=3; _lxsdk_s=1740efddf97-446-141-dd7%7C%7C7'
        }
    resopnse = requests.get(myurl, headers=header)
    bs_info = bs(resopnse.text, 'html.parser')
    return bs_info


# 获取前10电影url列表
def get_urls_list(myurl):
    urls_list = []
    prefix_url = 'https://maoyan.com'
    bs_info = get_url(myurl)
    for tags in bs_info.find_all('div', attrs={'class': 'channel-detail movie-item-title'}, limit=10):
        for atag in tags.find_all('a'):
            urls_list.append(prefix_url + atag.get('href'))
    return urls_list


# 获取电影名称、类型及上映时间
def get_detail(url):
    data = get_url(url)
    movie = {}
    print(data.text)
    for tags in data.find_all('div', attrs={'class': 'moive-brief-container'}):
        for atag in tags:
            movie['电影名'] = atag.find('div', attrs={'class': 'name'}).string
            movie['电影类型'] = atag.find('a', attrs={'class': 'text-link'}).string
            movie['上映日期'] = atag.find('li', attrs={'class': 'ellipsis'}).get_text()
    time.sleep(5)
    return movie


myurl = 'https://maoyan.com/films?showType=3'
movies_url = get_urls_list(myurl)
movie_data = []
for url in movies_url:
    movie_data.append(get_detail(url))

print(movie_data)

#movie1 = pd.DataFrame(data= movie_data)
#movie1.to_csv('./movie1.csv', encoding='utf-8', index=False, header=False)
