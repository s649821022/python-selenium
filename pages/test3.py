# Data 
# Name:kobe
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
import os
import random
driver=webdriver.Chrome()
url = 'http://106.13.46.164:8080/iwebshop/index.php?controller=site&action=pro_list&cat=67'
driver.get(url)
# scroll="document.getElementById('index_category').scrollIntoView(true)"
# driver.execute_script(scroll)
ul = driver.find_element_by_xpath('/html/body/div[1]/div[6]/div[2]/ul')
li = ul.find_elements_by_tag_name('li')
li[random.randint(0, len(li)-1)].find_element_by_tag_name('a').click()
# div.find_element_by_tag_name('a').click()