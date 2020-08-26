import requests
from bs4 import BeautifulSoup as bs
import pandas 
import time

def get_url(myurl):
    
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    header = {
        'user-agent': user_agent,
        'cookie': '__mta=251100857.1597935083958.1597964713055.1597964729537.5; uuid_n_v=v1; uuid=9C315DC0E2F411EA984097C6069B5E1D8D7B52490C4A4D1B93B1236D0E8CCF5D; mojo-uuid=a6f7e7b3b36710a2b6f92555dd7bd6a2; _lxsdk_cuid=1740c5a6146c8-007f09683322e7-e323069-144000-1740c5a6146c8; _lxsdk=9C315DC0E2F411EA984097C6069B5E1D8D7B52490C4A4D1B93B1236D0E8CCF5D; _csrf=b7e502bce25702f79dc2d12e04ed5b51afd4b27775e0b04484970525483238a7; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1597935084,1597935283,1597963567,1598137889; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1598137889; mojo-session-id={"id":"a30c29e909b4a79214c212c46e2b84a6","time":1598137888612}; __mta=251100857.1597935083958.1597964729537.1598137892525.6; mojo-trace-id=2; _lxsdk_s=1741870efee-704-033-9ea%7C%7C3'
        }
    resopnse = requests.get(myurl, headers=header)
    bs_info = bs(resopnse.text, 'html.parser')
    return bs_info

myurl = 'https://maoyan.com/films?showType=3'
bs_info = get_url(myurl)
urls_list = []
prefix_url = 'https://maoyan.com'
for tags in bs_info.find_all('div', attrs={'class': 'channel-detail movie-item-title'}, limit=10):
        for atag in tags.find_all('a'):
            urls_list.append(prefix_url + atag.get('href'))
#print(urls_list)

movies = {'电影名称':[],'电影类型':[],'上映日期':[]}
for url in urls_list:
    time.sleep(5)
    bs_info = get_url(url)
    #获取电影名称
    film_name = bs_info.find('h1', attrs={'class':'name'}).text
    movies['电影名称'].append(film_name) 
    print(film_name)

    #获取电影类型
    film_type_list= bs_info.find('a', attrs={'class': 'text-link'}).text
    movies['电影类型'].append(film_type_list)
    print(film_type_list)

    #获取上映时间
    plan_date = bs_info.find_all('li', attrs={'class': 'ellipsis'})[2].text
    movies['上映日期'].append(plan_date) 
    print(plan_date)

print(movies)

movie = pandas.DataFrame(data=movies,index=[0])
movie.to_csv('./movies.csv', encoding='utf_8_sig', index=False)



