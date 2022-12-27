from selenium import webdriver
from bs4 import BeautifulSoup

url = 'https://calculator.aws/#/addService'



def _init_browser():
    driver = webdriver.Chrome()
    return driver


if __name__ == "__init__":
    driver = _init_browser()
    driver.get(url)
    driver.quit()