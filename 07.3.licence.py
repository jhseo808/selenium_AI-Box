from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

import time
import pyautogui
import os
try:
    os.makedirs('D:\Auto_test')
    print('Auto테스트 파일이 생성되었습니다.')
except FileExistsError as a:
    print(a)

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
print('Login OK')

driver.get('http://172.16.6.230/web/#/web/license') # 시스템 > 라이선스

select_ids = ['mat-select-10', 'mat-select-12', 'mat-select-13', 'mat-select-14'] # 라이선스 리스트
option_ids = ['mat-option-33', 'mat-option-36', 'mat-option-37', 'mat-option-39'] # 라이선스 TOTAL

for select_id, option_id in zip(select_ids, option_ids):
    select_elem = driver.find_element(By.ID, select_id)
    select_elem.click()
    option_elem = driver.find_element(By.ID, option_id)
    option_elem.click()
    print('Ch license:',option_elem.text)

btn_license_apply = driver.find_element(By.XPATH, '/html/body/app-root/app-sidenav-responsive/div/mat-sidenav-container/mat-sidenav-content/app-license/div/mat-card/mat-list[1]/mat-card/div[3]/app-btn-apply/button/span')
btn_license_apply.click()
print('Ch License apply OK')

pyautogui.scroll(-1000)
driver.find_element(By.ID, 'mat-select-11').click() # 직접 등록
time.sleep(1)
manual_license = driver.find_elements(By.CLASS_NAME, 'mat-option-text') # 라이선스 리스트 출력
for idx, license_list in enumerate(manual_license):
    print(license_list.text)
'''
mat-option-20 VIX-120B
mat-option-21 VIX-220B 
mat-option-22 VIX-220F 
mat-option-23 VIX-220P 
mat-option-24 VIX-220R 
mat-option-25 VIX-220S 
mat-option-26 VIXAI-120B 
mat-option-27 VIXAI-220B 
mat-option-28 VIXAI-220F 
mat-option-29 VIXAI-220P 
mat-option-30 VIXAI-220R 
mat-option-31 VIXAI-VIXAI-220S 
mat-option-32 TOTALLINTELLIVIX 
'''
driver.find_element(By.ID, 'mat-option-32').click() # TOTAL 선택

# 시리얼, 라이선스 입력
serial = driver.find_element(By.ID, 'mat-input-16')
serial.click()
(action.send_keys('시리얼 번호 입력하세요!!').key_down(Keys.TAB).send_keys('라이선스 키 입력하세요!!').perform())

btn_online_apply = driver.find_element(By.XPATH, '/html/body/app-root/app-sidenav-responsive/div/mat-sidenav-container/mat-sidenav-content/app-license/div/mat-card/mat-list[3]/mat-card/div[5]/app-btn-online-registration/button')
btn_offline_apply = driver.find_element(By.XPATH, '/html/body/app-root/app-sidenav-responsive/div/mat-sidenav-container/mat-sidenav-content/app-license/div/mat-card/mat-list[3]/mat-card/div[5]/app-btn-offline-registration/button')
# btn_online_apply.click()
# btn_offline_apply.click()

# driver.get_screenshot_as_file('D:\Auto_test\license.png')
# pyautogui.scroll(-500)
