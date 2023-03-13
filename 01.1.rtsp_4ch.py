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

osd_btn = driver.find_element(By.CSS_SELECTOR,\
    'body > app-root > app-sidenav-responsive > div > mat-sidenav-container > mat-sidenav-content > app-live > div.flex-container > mat-card:nth-child(3) > div > button'\
        )
osd_btn.click() # 화면 표시 팝업
time.sleep(1)
driver.find_element(By.ID, 'mat-checkbox-3').click() # 이벤트가 발생한 물체만 표시 (default:enable)
driver.find_element(By.ID, 'mat-checkbox-4').click() # 객체ID
driver.find_element(By.ID, 'mat-checkbox-5').click() # 객체 종류
driver.find_element(By.ID, 'mat-checkbox-6').click() # 이벤트 메시지
driver.find_element(By.ID, 'mat-checkbox-8').click() # 차량 번호   
driver.find_element(By.ID, 'mat-checkbox-9').click()  # 이벤트 영역
driver.find_element(By.ID, 'mat-checkbox-10').click() # 객체 감지 영역
driver.find_element(By.ID, 'mat-checkbox-11').click() # 객체 비감지 영역
driver.find_element(By.ID, 'mat-checkbox-12').click() # 동적 배경 영역
driver.find_element(By.ID, 'mat-checkbox-13').click() # 객체 감지 ROI
driver.find_element(By.ID, 'mat-checkbox-7').click() # 계수기 (default:disable)
time.sleep(1)
osd_apply_btn = driver.find_element(By.XPATH, '//*[@id="mat-dialog-0"]/display-option-dialog/div/div[2]/button[1]')
osd_apply_btn.click() # 화면 표시 팝업 적용
print('OSD All enable OK')

count_reset = driver.find_element(By.XPATH, '/html/body/app-root/app-sidenav-responsive/div/mat-sidenav-container/mat-sidenav-content/app-live/div[1]/mat-list/mat-card/div/button')
count_reset.click() # 계수기 초기화
va_restart = driver.find_element(By.XPATH, '/html/body/app-root/app-sidenav-responsive/div/mat-sidenav-container/mat-sidenav-content/app-live/div[1]/mat-list/mat-card/div/app-btn-va-restart/button/span')
va_restart.click() # 영상 분석 재시작
print('Ch1 Count Reset & Va Restart OK!\n----------------------------------------------------------------------------------------------------------------')
cam_list = driver.find_element(By.ID, 'mat-select-3')
cam_list.click() # 카메라 리스트
driver.find_element(By.ID, 'mat-option-1').click() # 채널2
count_reset.click()
va_restart.click()
time.sleep(2)
print('Ch2 Count Reset & Va Restart OK!\n----------------------------------------------------------------------------------------------------------------')
cam_list.click() 
driver.find_element(By.ID, 'mat-option-2').click() # 채널3
count_reset.click()
va_restart.click()
time.sleep(2)
print('Ch3 Count Reset & Va Restart OK!\n----------------------------------------------------------------------------------------------------------------')
cam_list.click() 
driver.find_element(By.ID, 'mat-option-3').click() # 채널4
count_reset.click()
va_restart.click()
time.sleep(2)
print('Ch4 Count Reset & Va Restart OK!\n----------------------------------------------------------------------------------------------------------------')

pyautogui.scroll(-1000)
ptz_r = pyautogui.locateOnScreen('ptz_right.png')
pyautogui.mouseDown(ptz_r)
time.sleep(2)
ptz_l = pyautogui.locateOnScreen('ptz_left.png')
pyautogui.mouseDown(ptz_l)
time.sleep(2)
ptz_u = pyautogui.locateOnScreen('ptz_up.png')
pyautogui.mouseDown(ptz_u)
time.sleep(2)
ptz_d = pyautogui.locateOnScreen('ptz_down.png')
pyautogui.mouseDown(ptz_d)
time.sleep(2)
ptz_dl = pyautogui.locateOnScreen('ptz_downleft.png')
pyautogui.mouseDown(ptz_dl)
time.sleep(2)
ptz_dr = pyautogui.locateOnScreen('ptz_downright.png')
pyautogui.mouseDown(ptz_dr)
time.sleep(2)
ptz_ul = pyautogui.locateOnScreen('ptz_upleft.png')
pyautogui.mouseDown(ptz_ul)
time.sleep(2)
ptz_ur = pyautogui.locateOnScreen('ptz_upright.png')
pyautogui.mouseDown(ptz_ur)
time.sleep(2)
pyautogui.click()
print('PTZ Control OK!\n----------------------------------------------------------------------------------------------------------------')
