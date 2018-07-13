import json

from selenium import webdriver
from bs4 import BeautifulSoup


driver = webdriver.PhantomJS('./phantomjs/phantomjs')

# driver.get('http://assavictory.blog.me/221316338437')
driver.get('http://assavictory.blog.me/221317031819')

try:
    driver.switch_to.frame('screenFrame')
except Exception as e:
    print(json.loads(e.msg)['errorMessage'])
driver.switch_to.frame('mainFrame')

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
div_comment_cnt = soup.find('div', {'class': 'post_commentview_btn'})

try:
    comment_cnt = div_comment_cnt.find('em').text
except Exception as e:
    comment_cnt = 0

try:
    like_cnt = soup.find('em', {'class': '_cnt'}).text
except Exception as e:
    like_cnt = 0

print(like_cnt, comment_cnt)