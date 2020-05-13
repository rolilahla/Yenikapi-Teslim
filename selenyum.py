# -*- coding: utf-8 -*-
#
#https://atlantis.udhb.gov.tr/OTV2/_public/
#adresinden defter sorgulaması yapıp ekran görüntüsü alır
#
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

def sorgula(defter_no):
    opts = Options()
    opts.headless = True
    driver = Chrome(options=opts, executable_path='lib\geckodriver\chromedriver.exe')
    driver.get('https://atlantis.udhb.gov.tr/OTV2/_public/')
    no_listesi = defter_no.split("-")
    driver.find_element_by_id('pfix').send_keys(no_listesi[0])
    driver.find_element_by_id('region').send_keys(no_listesi[1])
    driver.find_element_by_id('city').send_keys(no_listesi[2])
    driver.find_element_by_id('number').send_keys(no_listesi[3])
    tetikle = driver.find_element_by_name('Submit')
    tetikle.click()
    driver.save_screenshot("screenshot.png")
    driver.quit()
