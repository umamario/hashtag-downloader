from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import random
import re
from selenium import webdriver;
import time
import urllib;
import os;
import random;
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import sys
import traceback


######################GLOBAL VARS################################
caps = DesiredCapabilities.FIREFOX
exp = r'https:\/\/scontent-mad1[a-z|A-Z|_|\/|\-|\.|0-9|+\.]+'
TIME_TO_WAIT = 300
################################################################

def is_element_present(driver, how, what):
    try:
        driver.find_element(by=how, value=what)
    except NoSuchElementException as e:
        return False
    return True
def hay_nuevas_imagenes(encont):
    if not encont:
        return False
    elif not os.path.isfile(encont[-1]):
        return True
    else:
        return False
def descargarImagenes(html,hashtag,links, point):
    i = point
    for link in links[point:]:
        direc = os.getcwd() + '/' + hashtag + '/' + re.findall(r'\w+.jpg', link)[0]
        if not os.path.isfile(direc):
            print "Downloaded ", direc, 'number', i
            urllib.urlretrieve(link, direc)
            i += 1
        else:
            print direc + " already exist"
    return i
def wait_and_quit(driver):
    driver.delete_all_cookies()
    #driver.quit()
    print "All done. I am going to sleep", TIME_TO_WAIT, "seconds"
    time.sleep(TIME_TO_WAIT)
    driver.get("https://www.instagram.com/explore/tags/" + hashtag)
    time.sleep(5)
    driver.find_element_by_class_name('_oidfu').click()
    html = (driver.page_source).encode('ascii', 'ignore')
    return re.findall(exp, html)

hashtag = 'cuadrilla5' #raw_input('Put the hashtag to be downloaded: \n')
if not os.path.exists('./'+hashtag): # Directory that I want to save the image to
        os.mkdir(hashtag) # If no directory create it
#hashtag = 'justlikethis'

caps["marionette"] = True
driver = webdriver.Firefox()  #capabilities=caps)
driver.get("https://www.instagram.com/explore/tags/" + hashtag)
#import ipdb; ipdb.set_trace(context=5)
time.sleep(5)
driver.find_element_by_class_name('_oidfu').click()
html = (driver.page_source).encode('ascii', 'ignore')
links = re.findall(exp, html)
point = 0
import ipdb; ipdb.set_trace(context=5)
while True:
    while hay_nuevas_imagenes(links):
        point = descargarImagenes(html, hashtag, links, point)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        html = (driver.page_source).encode('ascii', 'ignore')
        links = re.findall(exp, html)
    enc = wait_and_quit(driver)


