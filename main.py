#for twitter account liking

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from random import randint
import os


#creates a browser that can have memory / store previous information
#treats the item as one whole newly installed / incongito, need to log in once to retain info

chrome_options = Options()
dir_path = os.getcwd()
chrome_options.add_argument(f'user-data-dir={dir_path}/storedatahere')
#chrome_options.add_argument("--headless")
#chrome_options.add_argument("--disable-gpu")
#alt - chrome_options.add_argument("user-data-dir=C:\environments\selenium") #creates a new cookie/cache in the session
#old - chrome_options.add_argument("--user-data-dir=chrome-data") #creates a new cookie/cache in the session)
driver = webdriver.Chrome("A:\\Coding stuffs\\documents\\chromedriver.exe",options=chrome_options)#makes the driver use the data in the options



#-------------start trying here-------------------------
try:

    driver.get('https://twitter.com/home') #gets page


    element = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[4]/div/div/section/div/div/div[1]")) #wait until posts loaded(inside plc_main element)
    )


    targets = driver.find_elements_by_xpath('//span[contains(@class,"css-901oao css-16my406 r-poiln3 r-n6v787 r-1cwl3u0 r-1k6nrdp r-1e081e0 r-qvutc0")]')[2::3]


    for target in targets:
        target.click()
        time.sleep(randint(1,5)) #pauses for random 1-5secs

    print('twitter like post - done')
    driver.quit()

except:
    print('twitter like post - nope')
