import pandas as pd
import numpy as np
import re
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import urllib
from urllib.request import urlopen
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time



PATH = "C:\Program Files (x86)\chromedriver.exe"


x = 0
website_pages = []
name = []
Url = ["hello"]
Price = []
ArrayN = np.array(name)
ArrayU = np.array(Url)
ArrayP = np.array(Price)

#"""""
for x in range (2,3):
    y = "https://www.daraz.pk/skincare/?page={}&price=1000-&style=wf".format(x+1)
    website_pages.append(y)
    #print (website_pages)
    #""""

    #inks_df = pd.DataFrame(website_page)
array1 = np.array(website_pages)
df1 = pd.DataFrame(columns = ['Name','Price','Url'])
i = 0
a = 0
b = 0

for x in website_pages:
    driver = webdriver.Chrome(PATH)
    #options = webdriver.ChromeOptions()z
    #options.add_argument('headless')
    #capa = DesiredCapabilities.CHROME
    #capa["pageLoadStrategy"] = "none"
    #driver = webdriver.Chrome(PATH, options=options, desired_capabilities=capa)
    #driver.set_window_size(1440,900)
    page = driver.get(x)
    #driver.set_window_size(1440,900)
    #SCROLL_PAUSE_TIME = 0.5
    time.sleep(3)
    body = driver.find_element_by_tag_name('html')
    for x in range (0,100):
     body.send_keys(Keys.PAGE_DOWN)



    # Get scroll height
    #driver.execute_script("window.scrollTo(0, 1000);")
    
    #    """""
    #   try :
    #   price = driver.find_element_by_class_name("price")
    # except :
    #   price = driver.find_element_by_class_name("price-new")
    #else :
    #  price = "NaN" 
    #
    #image = driver.find_elements_by_class_name("c1ZEkM")
    #image_url = []
    #for x in image :
    #   img_url = img[x].get('src')
    #  print(img_url)
    #"""    
    #try:
    #    element = WebDriverWait(driver, 120).until(
    #      EC.presence_of_element_located((By.ID, "product-collection-image-365467"))
    # )
    #finally:
    #print("help")
    product_items = []
    #soup = BeautifulSoup(urllib.request.urlopen(x,"timeout" = 50).read())
    soup = BeautifulSoup(driver.page_source,"lxml")
    product_items = soup.find_all("div", attrs={"data-qa-locator" : "product-item"})
    product_name = soup.find_all("div", attrs={"class" : "c16H9d"})
    product_price = soup.find_all("div", attrs={"class" : "c3gUW0"})
    #print(product_items[0])
    #print(product_price)
    #print(product_items)
    #print(product_items.prettify())
    #print(product_items.div.div.div.div.a.img)
    #product_items = soup.find_all("div", attrs={"data-qa-locator": "product-item"})
        #img =soup.find_all("img" , {'class' : 'c1ZEkM'})
    page_url = []
    image_src = []
    item_url = []
    
    
    for item in product_items:
        #name = item.a.get("title")
        #print(name)
        item_url = item.a.get('href')
        #print(item_url)
        #print(item.contents)
        #item_image =item.img.get('src')
        #print(item_image)
        
        
        #try :
         #print(image_url)
        #print(len(item_url))
        #print(len(image_url))
        #image_url = f"https:{item.find('img')['src']}"
        #print(image_url)
        df1.loc[i,['Url']]= item_url
        i = i + 1
        
    for item in product_name:
        name = item.a.text
        #print(name)
        df1.loc[a,['Name']]= name
        a = a + 1
        
    for item in product_price:
        price = item.span.text
        #print(price)
        df1.loc[b,['Price']]= price
        b = b + 1
    
    
    
    print(df1)
    #name = driver.find_element_by_css_selector("div.product-item")
    #print(name.get_attribute("src"))
    #price = driver.find_elements_by_class_name("price")
    #url = driver.find_children_by_class_name("product-name")
    #url =  name.find_elements_by_tag_name("a")
    #image = driver.find_elements_by_class_name("woo-entry-image-main lazyloaded")
    
    #for a in range(0, 40):
     #   df1.loc[i,['Name']]= name[a].textz
      #  df1.loc[i,['Price']]= price[a].text
       # df1.loc[i,['page-Url']]= item
     
    print(ArrayU)   
    #print(df1)
#driver.close()
df1.to_csv ("Daraz-N-url-image.csv")
