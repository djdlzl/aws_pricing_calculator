from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

url = 'https://calculator.aws/#/addService'



def _init_browser():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True);
    options.add_experimental_option("excludeSwitches", ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    return driver

def _service_choice(driver):
    WebDriverWait(driver , 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="awsui-select-2-textbox"]'))).click()  # Choose a resion
    WebDriverWait(driver , 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="awsui-select-2-dropdown-option-8"]/div[1]'))).click() # ap-northeast-2 click
    WebDriverWait(driver , 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="awsui-input-0"]'))).send_keys('ec2') # find ec2
    time.sleep(2)
    try:
        title = driver.find_element(By.XPATH, '//*[@id="awsui-cards-0-0-header"]/span/span').text
        print(title)
        if(title == 'Amazon EC2'):
            WebDriverWait(driver , 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div/main/div/div[2]/div/div[1]/div/div[2]/awsui-cards/div/ol/li[1]/div/div[3]/div/span/div/div[2]/button'))).click() # 구성 click
    except:
        print("error",title)


    
def _configure_EC2(driver):
    print('ec2')
    time.sleep(3)
    WebDriverWait(driver , 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ec2enhancement"]/div/div/awsui-form/div/div[1]/div/span/div/div/div/div[2]/div/div[2]/div/div/div/div/div/input'))).send_keys('description') # find ec2
    WebDriverWait(driver , 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="awsui-select-5"]/div/awsui-icon/span'))).click() # ap-northeast-2 click
    

if __name__ == "__main__":
    print("init browser")
    driver = _init_browser()
    driver.get(url)
    _service_choice(driver)
    _configure_EC2(driver)
