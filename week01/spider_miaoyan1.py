#-*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import time


# 返回bs对象
def get_url(myurl):
    #user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    header = {
        'user-agent': user_agent,
        'cookie': '__mta=251100857.1597935083958.1597964713055.1597964729537.5; uuid_n_v=v1; uuid=9C315DC0E2F411EA984097C6069B5E1D8D7B52490C4A4D1B93B1236D0E8CCF5D; mojo-uuid=a6f7e7b3b36710a2b6f92555dd7bd6a2; _lxsdk_cuid=1740c5a6146c8-007f09683322e7-e323069-144000-1740c5a6146c8; _lxsdk=9C315DC0E2F411EA984097C6069B5E1D8D7B52490C4A4D1B93B1236D0E8CCF5D; _csrf=b7e502bce25702f79dc2d12e04ed5b51afd4b27775e0b04484970525483238a7; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1597935084,1597935283,1597963567,1598137889; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1598137889; mojo-session-id={"id":"a30c29e909b4a79214c212c46e2b84a6","time":1598137888612}; __mta=251100857.1597935083958.1597964729537.1598137892525.6; mojo-trace-id=2; _lxsdk_s=1741870efee-704-033-9ea%7C%7C3'
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
