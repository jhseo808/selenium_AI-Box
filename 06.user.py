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
print('Login ok')

# 네트워크 페이지
driver.get('http://172.16.6.230/web/#/web/user-setting') 
time.sleep(1)
'''
# 관리자 현재 pw, 새 pw 변경
driver.find_element(By.ID, 'mat-input-13').click() 
action.send_keys('Pass0001!').perform()
driver.find_element(By.ID, 'mat-input-14').click() 
action.send_keys('Pass0001!!').key_down(Keys.TAB).send_keys('Pass0001!!').perform()

btn_user_apply = driver.find_element(By.CSS_SELECTOR, 'body > app-root > app-sidenav-responsive > div > mat-sidenav-container > mat-sidenav-content > app-user-setting > div > mat-card > div:nth-child(4) > app-btn-apply > button')
btn_user_apply.click()
print('Password change ok')
time.sleep(1)

driver.find_element(By.CLASS_NAME, 'mat-form-field-infix')
(action.send_keys('admin').key_down(Keys.TAB).send_keys('Pass0001!!').pause(1).key_down(Keys.ENTER).perform())
action.reset_actions
time.sleep(1)

# 네트워크 페이지
driver.get('http://172.16.6.230/web/#/web/user-setting') 
time.sleep(1)

# 변경된 관리자 현재 pw, 새 pw
driver.find_element(By.ID, 'mat-input-20').click() 
action.send_keys('Pass0001!!').perform()
driver.find_element(By.ID, 'mat-input-21').click() 
action.send_keys('Pass0001!').key_down(Keys.TAB).send_keys('Pass0001!').perform()

btn_user_apply = driver.find_element(By.CSS_SELECTOR, 'body > app-root > app-sidenav-responsive > div > mat-sidenav-container > mat-sidenav-content > app-user-setting > div > mat-card > div:nth-child(4) > app-btn-apply > button')
btn_user_apply.click()
print('Password change ok')
time.sleep(1)

driver.find_element(By.CLASS_NAME, 'mat-form-field-infix')
(action.send_keys('admin').key_down(Keys.TAB).send_keys('Pass0001!').pause(1).key_down(Keys.ENTER).perform())
action.reset_actions
time.sleep(1)

'''
# 사용자 계정 10개 추가
for i in range(10):
    btn_user_add = driver.find_element(By.CSS_SELECTOR, 'body > app-root > app-sidenav-responsive > div > mat-sidenav-container > mat-sidenav-content > app-user-setting > div > mat-card > mat-list:nth-child(3) > mat-card > div.flex-row > div.ng-star-inserted > app-btn-add')
    btn_user_add.click()

user_input_text = driver.find_element(By.ID, 'mat-input-16')
user_input_text.clear()
user_input_text.click()
time.sleep(1)

user_data = [
    ('qatest1', 'Pass0001!'),
    ('qatest2', 'Pass0001!'),
    ('qatest3', 'Pass0001!'),
    ('qatest4', 'Pass0001!'),
    ('qatest5', 'Pass0001!'),
    ('qatest6', 'Pass0001!'),
    ('qatest7', 'Pass0001!'),
    ('qatest8', 'Pass0001!'),
    ('qatest9', 'Pass0001!'),
    ('qatest10', 'Pass0001!'),
]
for i in range(10):
    user = user_data[i]
    if i < 5:
        action.send_keys(user[0]).key_down(Keys.TAB).send_keys(user[1]).key_down(Keys.TAB).key_down(Keys.TAB).key_down(Keys.TAB).key_down(Keys.TAB)
    else:
        action.send_keys(user[0]).key_down(Keys.TAB).send_keys(user[1]).key_down(Keys.TAB).key_down(Keys.TAB).key_down(Keys.ENTER).key_down(Keys.TAB).key_down(Keys.TAB)
action.perform()

btn_user_apply = driver.find_element(By.CSS_SELECTOR, 'body > app-root > app-sidenav-responsive > div > mat-sidenav-container > mat-sidenav-content > app-user-setting > div > mat-card > div:nth-child(4) > app-btn-apply > button')
btn_user_apply.click()
time.sleep(1)
print('10 user add ok')
'''
# user10으로 로그인 확인
btn_logout = driver.find_element(By.CSS_SELECTOR, 'body > app-root > app-sidenav-responsive > div > mat-toolbar > button:nth-child(4)')
btn_logout.click()

driver.find_element(By.CLASS_NAME, 'mat-form-field-infix')
(action.send_keys('qatest10').key_down(Keys.TAB).send_keys('Pass0001!').pause(1).key_down(Keys.ENTER).perform())
action.reset_actions
time.sleep(1)
print('User10 Login ok')

btn_logout = driver.find_element(By.CSS_SELECTOR, 'body > app-root > app-sidenav-responsive > div > mat-toolbar > button:nth-child(4)')
btn_logout.click()

driver.find_element(By.CLASS_NAME, 'mat-form-field-infix')
(action.send_keys('admin').key_down(Keys.TAB).send_keys('Pass0001!').pause(1).key_down(Keys.ENTER).perform())
action.reset_actions
time.sleep(1)
driver.get('http://172.16.6.230/web/#/web/user-setting') # 네트워크 페이지
time.sleep(1)
'''
# 사용자 전체 제거
for i in range(13, 23):
    driver.find_element(By.ID, f'mat-checkbox-{i}').click()
btn_user_del = driver.find_element(By.CSS_SELECTOR, 'body > app-root > app-sidenav-responsive > div > mat-sidenav-container > mat-sidenav-content > app-user-setting > div > mat-card > mat-list:nth-child(3) > mat-card > div.flex-row > div.ng-star-inserted > app-btn-delete > button')
btn_user_del.click()
print('10 user delete OK')
btn_del_popup = driver.find_element(By.XPATH, '//*[@id="mat-dialog-0"]/app-confirm-dialog/div[2]/button[2]/span')
btn_del_popup.click() # 사용자 삭제 팝업
