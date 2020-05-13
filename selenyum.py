# -*- coding: utf-8 -*-

from selenium import webdriver
import os

tam_yol = os.getcwd() +"\lib\geckodriver"
browser = webdriver.Firefox(executable_path='{}'.format(tam_yol))
browser.get('https://www.google.com')