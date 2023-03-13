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
driver.find_element(By.ID, 'mat-select-9').click() # CH1 라이선스 리스트
license_set = driver.find_elements(By.CLASS_NAME, 'mat-option-text')
for int, license_list in enumerate(license_set):
    print(
        "=======================\nLicense List:", license_list.text,"\n======================="
    ) # 등록된 라이선스 리스트
driver.find_element(By.ID, 'mat-option-32').click() # CH1 TOTAL
driver.find_element(By.ID, 'mat-select-11').click() # CH2 라이선스 리스트
driver.find_element(By.ID, 'mat-option-35').click() # CH2 TOTAL
driver.find_element(By.ID, 'mat-select-12').click() # CH3 라이선스 리스트
driver.find_element(By.ID, 'mat-option-36').click() # CH3 TOTAL
driver.find_element(By.ID, 'mat-select-13').click() # CH4 라이선스 리스트
driver.find_element(By.ID, 'mat-option-38').click() # CH4 TOTAL
btn_license_apply = driver.find_element(By.XPATH, '/html/body/app-root/app-sidenav-responsive/div/mat-sidenav-container/mat-sidenav-content/app-license/div/mat-card/mat-list[1]/mat-card/div[3]/app-btn-apply/button/span')
btn_license_apply.click()
print('License CH apply complete!\n----------------------------------------------------------------')
# driver.get_screenshot_as_file('D:\Auto_test\license.png')
# print('system_license complte!\n----------------------------------------------------------------')
# time.sleep(1)
# pyautogui.scroll(-500)
