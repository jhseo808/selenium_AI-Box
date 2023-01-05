from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

import time
import pyautogui

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

#로그인
driver.find_element(By.CLASS_NAME, 'mat-form-field-infix')
(
action.send_keys('admin').key_down(Keys.TAB)
.send_keys('Pass0001!').pause(1).key_down(Keys.ENTER).perform()
)
action.reset_actions
time.sleep(1)

#네트워크 페이지
url = 'http://172.16.4.114/web/#/web/user-setting'
driver.get(url)
time.sleep(1)

#사용자 11개 추가 
pyautogui.scroll(-300)
add_btn = driver.find_element(By.CSS_SELECTOR, 'body > app-root > app-sidenav-responsive > div > mat-sidenav-container > mat-sidenav-content > app-user-setting > div > mat-card > mat-list:nth-child(3) > mat-card > div.flex-row > div.ng-star-inserted > app-btn-add')
add_btn.click()
add_btn.click()
add_btn.click()
add_btn.click()
add_btn.click()
add_btn.click()
add_btn.click()
add_btn.click()
add_btn.click()
add_btn.click()

add_user = driver.find_element(By.ID, 'mat-input-16')
add_user.clear()
add_user.click()
time.sleep(1)

(action.send_keys('qatest1').key_down(Keys.TAB).send_keys('Pass0001!').key_down(Keys.TAB).key_down(Keys.TAB).key_down(Keys.TAB).key_down(Keys.TAB)
 .send_keys('qatest2').key_down(Keys.TAB).send_keys('Pass0001!').key_down(Keys.TAB).key_down(Keys.TAB).key_down(Keys.TAB).key_down(Keys.TAB)
 .send_keys('qatest3').key_down(Keys.TAB).send_keys('Pass0001!').key_down(Keys.TAB).key_down(Keys.TAB).key_down(Keys.TAB).key_down(Keys.TAB)
 .send_keys('qatest4').key_down(Keys.TAB).send_keys('Pass0001!').key_down(Keys.TAB).key_down(Keys.TAB).key_down(Keys.TAB).key_down(Keys.TAB)
 .send_keys('qatest5').key_down(Keys.TAB).send_keys('Pass0001!').key_down(Keys.TAB).key_down(Keys.TAB).key_down(Keys.TAB).key_down(Keys.TAB)
 .send_keys('qatest6').key_down(Keys.TAB).send_keys('Pass0001!').key_down(Keys.TAB).key_down(Keys.TAB).key_down(Keys.ENTER).key_down(Keys.TAB).key_down(Keys.TAB)
 .send_keys('qatest7').key_down(Keys.TAB).send_keys('Pass0001!').key_down(Keys.TAB).key_down(Keys.TAB).key_down(Keys.ENTER).key_down(Keys.TAB).key_down(Keys.TAB)
 .send_keys('qatest8').key_down(Keys.TAB).send_keys('Pass0001!').key_down(Keys.TAB).key_down(Keys.TAB).key_down(Keys.ENTER).key_down(Keys.TAB).key_down(Keys.TAB)
 .send_keys('qatest9').key_down(Keys.TAB).send_keys('Pass0001!').key_down(Keys.TAB).key_down(Keys.TAB).key_down(Keys.ENTER).key_down(Keys.TAB).key_down(Keys.TAB)
 .send_keys('qatest10').key_down(Keys.TAB).send_keys('Pass0001!').key_down(Keys.TAB).key_down(Keys.TAB).key_down(Keys.ENTER).key_down(Keys.TAB).key_down(Keys.TAB).perform()
 )
time.sleep(1)

apply_btn = driver.find_element(By.CSS_SELECTOR, 'body > app-root > app-sidenav-responsive > div > mat-sidenav-container > mat-sidenav-content > app-user-setting > div > mat-card > div:nth-child(4) > app-btn-apply > button')
apply_btn.click()
time.sleep(1)

#사용자 제거
driver.find_element(By.ID, 'mat-checkbox-13').click()
driver.find_element(By.ID, 'mat-checkbox-14').click()
driver.find_element(By.ID, 'mat-checkbox-15').click()
driver.find_element(By.ID, 'mat-checkbox-16').click()
driver.find_element(By.ID, 'mat-checkbox-17').click()
driver.find_element(By.ID, 'mat-checkbox-18').click()
driver.find_element(By.ID, 'mat-checkbox-19').click()
driver.find_element(By.ID, 'mat-checkbox-20').click()
driver.find_element(By.ID, 'mat-checkbox-21').click()
driver.find_element(By.ID, 'mat-checkbox-22').click()

del_btn = driver.find_element(By.CSS_SELECTOR, 'body > app-root > app-sidenav-responsive > div > mat-sidenav-container > mat-sidenav-content > app-user-setting > div > mat-card > mat-list:nth-child(3) > mat-card > div.flex-row > div.ng-star-inserted > app-btn-delete > button')
del_btn.click()

#사용자 삭제 팝업
popup_btn_del = driver.find_element(By.XPATH, '//*[@id="mat-dialog-0"]/app-confirm-dialog/div[2]/button[2]/span')
popup_btn_del.click()
