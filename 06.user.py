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

driver.get('http://172.16.6.230')
action = ActionChains(driver)

driver.find_element(By.CLASS_NAME, 'mat-form-field-infix')
(action.send_keys('admin').key_down(Keys.TAB).send_keys('Pass0001!').pause(1).key_down(Keys.ENTER).perform())
action.reset_actions
time.sleep(1)
print('Login OK\n----------------------------------------------------------------')

url = 'http://172.16.6.230/web/#/web/user-setting'
driver.get(url) # 네트워크 페이지
time.sleep(1)
'''
driver.find_element(By.ID, 'mat-input-13').click() #  현재 비밀번호
action.send_keys('Pass0001!').perform()
driver.find_element(By.ID, 'mat-input-14').click() #  새 비밀번호
action.send_keys('Pass0001!!').perform()
driver.find_element(By.ID, 'mat-input-15').click() #  새 비밀번호 확인
action.send_keys('Pass0001!!').perform()

btn_apply = driver.find_element(By.CSS_SELECTOR, 'body > app-root > app-sidenav-responsive > div > mat-sidenav-container > mat-sidenav-content > app-user-setting > div > mat-card > div:nth-child(4) > app-btn-apply > button')
btn_apply.click()
print('Password change complte!\n----------------------------------------------------------------')
btn_logout = driver.find_element(By.CSS_SELECTOR, 'body > app-root > app-sidenav-responsive > div > mat-toolbar > button:nth-child(4)')
btn_logout.click()

driver.find_element(By.CLASS_NAME, 'mat-form-field-infix')
(action.send_keys('admin').key_down(Keys.TAB).send_keys('Pass0001!').pause(1).key_down(Keys.ENTER).perform())
action.reset_actions
time.sleep(1)
'''

pyautogui.scroll(-300)
btn_add = driver.find_element(By.CSS_SELECTOR, 'body > app-root > app-sidenav-responsive > div > mat-sidenav-container > mat-sidenav-content > app-user-setting > div > mat-card > mat-list:nth-child(3) > mat-card > div.flex-row > div.ng-star-inserted > app-btn-add')
btn_add.click() # 사용자 11개 추가
btn_add.click()
btn_add.click()
btn_add.click()
btn_add.click()
btn_add.click()
btn_add.click()
btn_add.click()
btn_add.click()
btn_add.click()
add_user = driver.find_element(By.ID, 'mat-input-16')
add_user.clear()
add_user.click()
time.sleep(1)
(
    action.send_keys('qatest1').key_down(Keys.TAB).send_keys('Pass0001!').key_down(Keys.TAB).key_down(Keys.TAB).key_down(Keys.TAB).key_down(Keys.TAB)
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
btn_apply = driver.find_element(By.CSS_SELECTOR, 'body > app-root > app-sidenav-responsive > div > mat-sidenav-container > mat-sidenav-content > app-user-setting > div > mat-card > div:nth-child(4) > app-btn-apply > button')
btn_apply.click()
time.sleep(1)
print('10 user add complte!\n----------------------------------------------------------------')
btn_logout = driver.find_element(By.CSS_SELECTOR, 'body > app-root > app-sidenav-responsive > div > mat-toolbar > button:nth-child(4)')
btn_logout.click()

driver.find_element(By.CLASS_NAME, 'mat-form-field-infix')
(action.send_keys('qatest10').key_down(Keys.TAB).send_keys('Pass0001!').pause(1).key_down(Keys.ENTER).perform())
action.reset_actions
time.sleep(1)
print('User Login OK\n----------------------------------------------------------------')
btn_logout = driver.find_element(By.CSS_SELECTOR, 'body > app-root > app-sidenav-responsive > div > mat-toolbar > button:nth-child(4)')
btn_logout.click()
driver.find_element(By.CLASS_NAME, 'mat-form-field-infix')
(action.send_keys('admin').key_down(Keys.TAB).send_keys('Pass0001!').pause(1).key_down(Keys.ENTER).perform())
action.reset_actions
time.sleep(1)
driver.get(url) # 네트워크 페이지
time.sleep(1)

driver.find_element(By.ID, 'mat-checkbox-27').click() # 사용자 제거
driver.find_element(By.ID, 'mat-checkbox-28').click()
driver.find_element(By.ID, 'mat-checkbox-29').click()
driver.find_element(By.ID, 'mat-checkbox-30').click()
driver.find_element(By.ID, 'mat-checkbox-31').click()
driver.find_element(By.ID, 'mat-checkbox-32').click()
driver.find_element(By.ID, 'mat-checkbox-33').click()
driver.find_element(By.ID, 'mat-checkbox-34').click()
driver.find_element(By.ID, 'mat-checkbox-35').click()
driver.find_element(By.ID, 'mat-checkbox-36').click()
btn_del = driver.find_element(By.CSS_SELECTOR, 'body > app-root > app-sidenav-responsive > div > mat-sidenav-container > mat-sidenav-content > app-user-setting > div > mat-card > mat-list:nth-child(3) > mat-card > div.flex-row > div.ng-star-inserted > app-btn-delete > button')
btn_del.click()
print('10 user delete complte!\n----------------------------------------------------------------')
btn_del_popup = driver.find_element(By.XPATH, '//*[@id="mat-dialog-0"]/app-confirm-dialog/div[2]/button[2]/span')
btn_del_popup.click() # 사용자 삭제 팝업
