# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pandas as pd
import pymysql


class MaoyanPipeline:
    def process_item(self, item, spider):
        film_name = item['film_name']
        film_types = item['film_types']
        plan_date = item['plan_date']
        
        # movie = pd.DataFrame([
        #     film_name, film_types, plan_date
        # ])
        # movie.to_csv('./movie.csv', mode='a', encoding='utf-8', index=False, header=False)
        
        #return item
        conn = pymysql.connect(host='127.0.0.1', prot = 3306, user = 'xx', password = 'xxx', db = 'spiders')
        cur = conn.cursor()
        try:
            cur.execute("insert into scrapy(film_name,film_types,plan_type) values(%s,%s,%s)" % (film_name,film_types,plan_date))
            conn.commit()
        except Exception as e:
            print(e)
        finally:
             conn.close()
