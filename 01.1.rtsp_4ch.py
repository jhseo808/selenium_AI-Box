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
print('Login ok')

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
print('OSD All enable ok')

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
    print(f'ch{channel+1} Count Reset & Va Restart ok')

# PTZ 컨트롤 이미지
ptz_r = pyautogui.locateOnScreen('ptz_right.png')
ptz_l = pyautogui.locateOnScreen('ptz_left.png')
ptz_u = pyautogui.locateOnScreen('ptz_up.png')
ptz_d = pyautogui.locateOnScreen('ptz_down.png')
ptz_dl = pyautogui.locateOnScreen('ptz_downleft.png')
ptz_dr = pyautogui.locateOnScreen('ptz_downright.png')
ptz_ul = pyautogui.locateOnScreen('ptz_upleft.png')
ptz_ur = pyautogui.locateOnScreen('ptz_upright.png')
ptz_zoomin = pyautogui.locateOnScreen('zoom_in.png')
ptz_zoomout = pyautogui.locateOnScreen('zoom_out.png')

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
print('PTZ Control ok')

preset_text = driver.find_element(By.ID, 'mat-input-11') # 프리셋 번호 텍스트
btn_preset_set = driver.find_element(By.XPATH, '/html/body/app-root/app-sidenav-responsive/div/mat-sidenav-container/mat-sidenav-content/app-live/div[1]/mat-card[2]/div/app-ptz-control/div/div/div[2]/div[2]/button[2]/span')
btn_preset_mv = driver.find_element(
    By.XPATH, '/html/body/app-root/app-sidenav-responsive/div/mat-sidenav-container/mat-sidenav-content/app-live/div[1]/mat-card[2]/div/app-ptz-control/div/div/div[2]/div[2]/button[1]/span'
    )

zoom_images = ['zoom_in.png','zoom_out.png']
preset_nums = ['1','2','3','4','5','6','7','8']

# 순차적으로 ptz_images와 preset_nums로 지정
for ptz_image, preset_num in zip(ptz_images, preset_nums):
    ptz = pyautogui.locateOnScreen(ptz_image)
    pyautogui.mouseDown(ptz)
    time.sleep(2)
    preset_text.clear()
    preset_text.send_keys(preset_num)
    btn_preset_set.click()
    print(f"Preset {preset_num} set for {ptz_image}")

for zoom_image in zoom_images:
    zoom = pyautogui.locateOnScreen(zoom_image)
    pyautogui.mouseDown(zoom)
    time.sleep(2)
    print(f"Zoom set for {zoom_image}")

preset_text.clear() # 프리셋 텍스트 삭제
preset_text.send_keys("1") # 프리셋 1번
btn_preset_mv.click() # 프리셋 1번으로 이동
print('Move to Preset1 OK')
