import requests
from bs4 import BeautifulSoup as bs
import lxml.etree
import pandas as pd

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
header = {
    'user-agent': user_agent,
    'cookie': 'uuid_n_v=v1; uuid=9C315DC0E2F411EA984097C6069B5E1D8D7B52490C4A4D1B93B1236D0E8CCF5D; _csrf=8d3c6d10032876dd1ef857e023df0e6f1fba50a56c3e801eee89d943d9bd4a49; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1597935084; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1597935084; mojo-uuid=a6f7e7b3b36710a2b6f92555dd7bd6a2; _lxsdk_cuid=1740c5a6146c8-007f09683322e7-e323069-144000-1740c5a6146c8; _lxsdk=9C315DC0E2F411EA984097C6069B5E1D8D7B52490C4A4D1B93B1236D0E8CCF5D; mojo-session-id={"id":"b1296f913b268b8bcc9da7bdf10a6ce7","time":1597935083862}; mojo-trace-id=1; __mta=251100857.1597935083958.1597935083958.1597935083958.1; _lxsdk_s=1740c5a6148-b40-6f0-dec%7C%7C2'
}
myurl = 'https://maoyan.com/films?showType=3'
resopnse = requests.get(myurl, headers=header)

bs_info = bs(resopnse.text, 'html.parser')
prefix_url = 'https://maoyan.com'
urls_list = []

# 获取电影url
for tags in bs_info.find_all('div', attrs={'class': 'channel-detail movie-item-title'}):
    #print(tags.get('title'))
    for atag in tags.find_all('a'):
        urls_list.append(prefix_url + atag.get('href'))
#print(urls_list)
for url in urls_list[0:10]:
    print(f'当前链接：{url}')
    resopnse = requests.get(url, headers=header)
    selector = lxml.etree.HTML(resopnse.text)
    # 电影名称
    film_name = selector.xpath('/html/body/div[3]/div/div[2]/div[1]/h1/text()')
    print(f'电影名称: {film_name}')
    # 电影类型
    film_type = selector.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[1]/a[1]/text()')
    print(f'电影类型：{film_type}')
    # 上映时间
    plan_date = selector.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[3]/text()')
    print(f'上映日期：{plan_date}')


