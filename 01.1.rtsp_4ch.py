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
(action.send_keys('admin').key_down(Keys.TAB).send_keys('Pass0001!').pause(1).key_down(Keys.ENTER).perform()) # 로그인
action.reset_actions
time.sleep(2)
print('Login OK!\n----------------------------------------------------------------------------------------------------------------')

# 화면 표시 팝업
osd_btn = driver.find_element(By.CSS_SELECTOR,\
    'body > app-root > app-sidenav-responsive > div > mat-sidenav-container > mat-sidenav-content > app-live > div.flex-container > mat-card:nth-child(3) > div > button'\
        )
osd_btn.click()
time.sleep(1)
checkbox_ids = [
    'mat-checkbox-3', 'mat-checkbox-4', 'mat-checkbox-5', 'mat-checkbox-6', 'mat-checkbox-8', 'mat-checkbox-9', 'mat-checkbox-10', 'mat-checkbox-11', 'mat-checkbox-12', 'mat-checkbox-13',
    'mat-checkbox-7'
    ]
for checkbox_id in checkbox_ids:
    driver.find_element(By.ID, checkbox_id).click()
time.sleep(1)
osd_apply_btn = driver.find_element(By.XPATH, '//*[@id="mat-dialog-0"]/display-option-dialog/div/div[2]/button[1]')
osd_apply_btn.click()
print('OSD All enable OK')

# 채널별 계수기 초기화, 분석 재시작
count_reset = driver.find_element(By.XPATH, '/html/body/app-root/app-sidenav-responsive/div/mat-sidenav-container/mat-sidenav-content/app-live/div[1]/mat-list/mat-card/div/button')
va_restart = driver.find_element(By.XPATH, '/html/body/app-root/app-sidenav-responsive/div/mat-sidenav-container/mat-sidenav-content/app-live/div[1]/mat-list/mat-card/div/app-btn-va-restart/button/span')
count_reset.click() 
va_restart.click() 
cam_list = driver.find_element(By.ID, 'mat-select-3') # 라이브 페이지 채널 리스트

channels = [1,2,3]
for channel in channels:
    cam_list.click()
    driver.find_element(By.ID, f'mat-option-{channel}').click()
    count_reset.click()
    va_restart.click()
    time.sleep(2)
    print(f'ch{channel+1} Count Reset & Va Restart OK')

# PTZ 이미지 추적
pyautogui.scroll(-1000)
ptz_images = [
    'ptz_right.png', 'ptz_left.png', 'ptz_up.png', 'ptz_down.png',
    'ptz_downleft.png', 'ptz_downright.png', 'ptz_upleft.png', 'ptz_upright.png'
    ]
for ptz_image in ptz_images:
    ptz = pyautogui.locateOnScreen(ptz_image)
    pyautogui.mouseDown(ptz)
    time.sleep(2)
pyautogui.click()
print('PTZ Control OK!\n----------------------------------------------------------------------------------------------------------------')
