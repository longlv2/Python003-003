from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get('https://shimo.im/login?from=home')
    time.sleep(2)
    browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/input').send_keys('xxxx')
    time.sleep(2)
    browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/input').send_keys('xxxx')
    browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/button').click()
    cookies = browser.get_cookie()
    print(cookies)
    time.sleep(3)
except Exception as e:
    print(e)
finally:
    browser.close()
