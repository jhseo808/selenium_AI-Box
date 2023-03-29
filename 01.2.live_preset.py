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
(action.send_keys('admin').key_down(Keys.TAB).send_keys('Pass0001!').pause(1).key_down(Keys.ENTER).perform()) # 로그인
action.reset_actions
time.sleep(2)
print('Login OK!\n----------------------------------------------------------------------------------------------------------------')

cam_list = driver.find_element(By.ID, 'mat-select-3')
cam_list.click() # 카메라 리스트
driver.find_element(By.ID, 'mat-option-3').click() # 채널4
time.sleep(4) # RTSP 출력시 간헐적 스크롤UP 방지 대기 시간
pyautogui.scroll(-1000)
time.sleep(2)

ptz_r = pyautogui.locateOnScreen('ptz_right.png')
pyautogui.mouseDown(ptz_r)
time.sleep(1)
# pyautogui.mouseUp(ptz_r)
preset_no = driver.find_element(By.ID, 'mat-input-11') # 프리셋 번호 텍스트
preset_no.clear()
preset_no.send_keys("1") # 프리셋 1번
btn_preset_set = driver.find_element(By.XPATH, '/html/body/app-root/app-sidenav-responsive/div/mat-sidenav-container/mat-sidenav-content/app-live/div[1]/mat-card[2]/div/app-ptz-control/div/div/div[2]/div[2]/button[2]/span')
btn_preset_set.click() # 프리셋 설정 버튼

ptz_l = pyautogui.locateOnScreen('ptz_left.png')
pyautogui.mouseDown(ptz_l)
time.sleep(2)
preset_no.clear()
preset_no.send_keys("2") # 프리셋 2번
btn_preset_set.click()

ptz_u = pyautogui.locateOnScreen('ptz_up.png')
pyautogui.mouseDown(ptz_u)
time.sleep(2)
preset_no.clear()
preset_no.send_keys("3") # 프리셋 3번
btn_preset_set.click()

ptz_d = pyautogui.locateOnScreen('ptz_down.png')
pyautogui.mouseDown(ptz_d)
time.sleep(2)
preset_no.clear()
preset_no.send_keys("4") # 프리셋 4번
btn_preset_set.click()

ptz_dl = pyautogui.locateOnScreen('ptz_downleft.png')
pyautogui.mouseDown(ptz_dl)
time.sleep(2)
preset_no.clear()
preset_no.send_keys("5") # 프리셋 5번
btn_preset_set.click() 

ptz_dr = pyautogui.locateOnScreen('ptz_downright.png')
pyautogui.mouseDown(ptz_dr)
time.sleep(2)
preset_no.clear()
preset_no.send_keys("6") # 프리셋 6번
btn_preset_set.click()

ptz_ul = pyautogui.locateOnScreen('ptz_upleft.png')
pyautogui.mouseDown(ptz_ul)
time.sleep(2)
preset_no.clear()
preset_no.send_keys("7") # 프리셋 7번
btn_preset_set.click()

ptz_ur = pyautogui.locateOnScreen('ptz_upright.png')
pyautogui.mouseDown(ptz_ur)
time.sleep(2)
preset_no.clear()
preset_no.send_keys("8") # 프리셋 8번
btn_preset_set.click()
print(
    '''PTZ Move Right, Left, Up, Down
    Down Left, Right
    Preset 1,2,3,4,5,6,7,8 OK!\n------------------------------------------------------------------------------------------'''
     )

ptz_zoomin = pyautogui.locateOnScreen('zoom_in.png')
pyautogui.mouseDown(ptz_zoomin)
time.sleep(1)
ptz_zoomout = pyautogui.locateOnScreen('zoom_out.png')
pyautogui.mouseDown(ptz_zoomout)
time.sleep(3)
pyautogui.click()
print('Zoom In, Out OK\n------------------------------------------------------------------------------------------')

preset_no.clear() # 프리셋 텍스트 삭제
preset_no.send_keys("1") # 프리셋 1번
btn_preset_mv = driver.find_element(
    By.XPATH, '/html/body/app-root/app-sidenav-responsive/div/mat-sidenav-container/mat-sidenav-content/app-live/div[1]/mat-card[2]/div/app-ptz-control/div/div/div[2]/div[2]/button[1]/span'
    )
btn_preset_mv.click() # 프리셋 1번으로 이동
print('Move to Preset1 OK')
