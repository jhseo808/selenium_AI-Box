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
print('Login ok')

driver.get('http://172.16.6.230/web/#/web/information') # 시스템 > 정보
time.sleep(1)
device_name = driver.find_element(By.CSS_SELECTOR, '#mat-input-16')
device_name.clear()
device_name.click()
action.send_keys('test장치명12!@#').perform() # 장치명 변경
btn_apply = driver.find_element(By.CSS_SELECTOR, 'body > app-root > app-sidenav-responsive > div > mat-sidenav-container > mat-sidenav-content > app-information > div > mat-card > div:nth-child(6) > app-btn-apply > button > span')
btn_apply.click()
driver.get_screenshot_as_file('D:\Auto_test\information.png')
print('device_name change ok')

driver.get('http://172.16.6.230/web/#/web/resource-monitor') # 시스템 > 리소스 모니터
pyautogui.scroll(-300)
driver.get_screenshot_as_file('D:\Auto_test\resource-monitor.png')
print('system_resource-monitor ok')
time.sleep(1)

driver.get('http://172.16.6.230/web/#/web/datetime') # 시스템 > 날짜/시간
driver.find_element(By.XPATH, '//*[@id="mat-select-11"]').click()
aaa = driver.find_elements(By.CLASS_NAME, 'mat-option-text')
for idx, gmt_list in enumerate(aaa):
    print(gmt_list.text)
driver.find_element(By.ID, 'mat-option-103').click() # GMT-07:00 치와와,마샤틀란 (mat-option-20 부터 시작)
driver.find_element(By.ID, 'mat-button-toggle-25-button').click() # 수동
time_manual = driver.find_element(By.CSS_SELECTOR, '#mat-input-20') # 년/월/일 텍스트창
time_manual.clear()
time_manual.click()
(action.send_keys("2023").send_keys(Keys.TAB).send_keys("01").send_keys("02").send_keys(Keys.ARROW_UP).send_keys(Keys.TAB)
 .send_keys("12").send_keys("34").send_keys("56").perform())
time.sleep(3)
driver.find_element(By.ID, 'mat-checkbox-3').click() # PC 동기화
driver.find_element(By.ID, 'mat-button-toggle-26-button').click() # NTP 서버
time_ntp = driver.find_element(By.CSS_SELECTOR, '#mat-input-18')
time_ntp.clear()
time_ntp.click()
(action.send_keys("time.test_seo").perform())
driver.get_screenshot_as_file('D:\Auto_test\datetime.png')
print('system_datetime ok')
time.sleep(1)

driver.get('http://172.16.6.230/web/#/web/upgrade') # 시스템 > 업그레이드
driver.get_screenshot_as_file(r'D:\Auto_test\upgrade.png')
print('system_upgrade ok')
time.sleep(1)

driver.get('http://172.16.6.230/web/#/web/license') # 시스템 > 라이선스

select_ids = ['mat-select-12', 'mat-select-14', 'mat-select-15', 'mat-select-16'] # 라이선스 리스트
option_ids = ['mat-option-133', 'mat-option-136', 'mat-option-137', 'mat-option-139'] # 라이선스 TOTAL

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
driver.find_element(By.ID, 'mat-select-13').click() # 직접 등록
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
driver.find_element(By.ID, 'mat-option-132').click() # TOTAL 선택

# 시리얼, 라이선스 입력
serial = driver.find_element(By.ID, 'mat-input-23')
serial.click()
(action.send_keys('시리얼 번호 입력하세요!!').key_down(Keys.TAB).send_keys('라이선스 키 입력하세요!!').perform())

btn_online_apply = driver.find_element(By.XPATH, '/html/body/app-root/app-sidenav-responsive/div/mat-sidenav-container/mat-sidenav-content/app-license/div/mat-card/mat-list[3]/mat-card/div[5]/app-btn-online-registration/button')
btn_offline_apply = driver.find_element(By.XPATH, '/html/body/app-root/app-sidenav-responsive/div/mat-sidenav-container/mat-sidenav-content/app-license/div/mat-card/mat-list[3]/mat-card/div[5]/app-btn-offline-registration/button')
# btn_online_apply.click()
# btn_offline_apply.click()

# driver.get_screenshot_as_file('D:\Auto_test\license.png')
# pyautogui.scroll(-500)
