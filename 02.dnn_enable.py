from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

import time

#브라우저 꺼짐 방지
options = Options()
options.add_experimental_option("detach", True)
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
driver.implicitly_wait(3)
driver.maximize_window()

url = 'http://172.16.4.114/web/#/web/auth'
driver.get(url)
action = ActionChains(driver)

driver.find_element(By.CLASS_NAME, 'mat-form-field-infix')
(
action.send_keys('admin').key_down(Keys.TAB)
.send_keys('Pass0001!').pause(1).key_down(Keys.ENTER).perform()
)
action.reset_actions
time.sleep(1)

#dnn 페이지 이동
url = 'http://172.16.4.114/web/#/web/ai-dnn-resource'
driver.get(url)

#검출기 활성화
driver.find_element(By.CSS_SELECTOR, '#mat-checkbox-3 > label > span').click()
driver.find_element(By.CSS_SELECTOR, '#mat-checkbox-4 > label > span').click()
#driver.find_element(By.CSS_SELECTOR, '#mat-checkbox-5 > label > span').click()
driver.find_element(By.CSS_SELECTOR, '#mat-checkbox-6 > label > span').click()
driver.find_element(By.CSS_SELECTOR, '#mat-checkbox-7 > label > span').click()

#인식모듈 활성화
driver.find_element(By.CSS_SELECTOR, '#mat-checkbox-8 > label > span').click()
driver.find_element(By.CSS_SELECTOR, '#mat-checkbox-9 > label > span').click()
driver.find_element(By.CSS_SELECTOR, '#mat-checkbox-10 > label > span').click()
driver.find_element(By.CSS_SELECTOR, '#mat-checkbox-11 > label > span').click()
driver.find_element(By.CSS_SELECTOR, '#mat-checkbox-12 > label > span').click()
driver.find_element(By.CSS_SELECTOR, '#mat-checkbox-13 > label > span').click()
driver.find_element(By.CSS_SELECTOR, '#mat-checkbox-14 > label > span').click()

driver.find_element(By.CSS_SELECTOR, 'body > app-root > app-sidenav-responsive > div > mat-sidenav-container > mat-sidenav-content > app-ai-dnn-resource > div > mat-card > div:nth-child(4) > app-btn-apply > button > span').click()

