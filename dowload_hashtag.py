from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import re
from selenium import webdriver;
import time
import urllib;
import os;
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import traceback


######################GLOBAL VARS################################
caps = DesiredCapabilities.FIREFOX
exp = r'https:\/\/scontent-waw1[a-z|A-Z|_|\/|\-|\.|0-9|+\.]+'
TIME_TO_WAIT = 60
FTP_DIR = '/tmp/' #put slash at the end of the var. The photos will be download in this dir + hashtag
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
def descargarImagenes(hashtag,links):
    i = 0
    for link in links:
        direc = FTP_DIR + hashtag + '/' + re.findall(r'\w+.jpg', link)[0]
        if not os.path.isfile(direc):
            print "Downloaded ", direc, 'number', i
            urllib.urlretrieve(link, direc)
            i += 1
        else:
            print direc + " already exist"

def wait_and_quit(driver):
    driver.delete_all_cookies()
    print "All done. I am going to sleep", TIME_TO_WAIT, "seconds"
    time.sleep(TIME_TO_WAIT)
    driver.get("https://www.instagram.com/explore/tags/" + hashtag)
    time.sleep(5)
    driver.find_element_by_class_name('_oidfu').click()


hashtag = raw_input('Put the hashtag to be downloaded: \n')
if not os.path.exists(FTP_DIR + hashtag): # Directory that I want to save the image to
        os.mkdir(FTP_DIR + hashtag) # If no directory create it

caps["marionette"] = True
driver = webdriver.Firefox(capabilities=caps)
driver.get("https://www.instagram.com/explore/tags/" + hashtag)
time.sleep(5)
driver.find_element_by_class_name('_oidfu').click()
while True:
    ant = driver.execute_script('return window.pageYOffset;')
    dsp = 0
    while ant != dsp:
        ant = dsp
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        dsp = driver.execute_script('return window.pageYOffset;')
        print ant,  dsp
    html = (driver.page_source).encode('ascii', 'ignore')
    links = re.findall(exp, html)
    descargarImagenes(hashtag, links)
    wait_and_quit(driver)


