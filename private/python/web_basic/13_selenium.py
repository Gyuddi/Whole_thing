import time
from selenium import webdriver

browser = webdriver.Chrome() # "./chromedriver.exe"

# 1. 네이버 이동
browser.get("https://flight.naver.com/flights/")
