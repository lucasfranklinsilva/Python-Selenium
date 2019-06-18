from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time 
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions();
options.add_argument('--user-data-dir=./User_Data')
driver = webdriver.Chrome(r'C:/chromedriver.exe', chrome_options=options)
driver.get('https://web.whatsapp.com/')

time.sleep(20)

j = 5

for t in range(j):
    
    name = "Teste de Software"
    msg = "Teste"
    count = 1
    wait = WebDriverWait(driver = driver, timeout = 900)
    
    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()
    
    msg_box = driver.find_element_by_class_name('_2S1VP')
    #msg += '\n this is a system generated message'

    for i in range(count):
            msg_box.send_keys(Keys.CONTROL, 'v')
            time.sleep(10)
            driver.find_element_by_css_selector('span[data-icon="send-light"]').click()

    time.sleep(15)


wait = WebDriverWait(driver = driver, timeout = 600)
driver.close()