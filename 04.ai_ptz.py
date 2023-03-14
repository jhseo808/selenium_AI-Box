from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

import time
import pyautogui

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

driver.get('http://172.16.6.230/web/#/web/ai')
time.sleep(1)
cam_list = driver.find_element(By.ID, 'chSelect')
cam_list.click() # 카메라 리스트
driver.find_element(By.ID, 'mat-option-35').click() # 채널4
ptz_pg = driver.find_element(By.ID, 'mat-tab-label-0-2')
ptz_pg.click()
time.sleep(3)
print('PTZ Feature START!')

ptz_r = pyautogui.locateOnScreen('ptz_right.png')
pyautogui.mouseDown(ptz_r)
time.sleep(1)
preset_no = driver.find_element(By.CSS_SELECTOR, '#mat-input-2')
preset_no.click()
preset_no.send_keys("1") # Preset 1
time.sleep(1)
preset_apply = driver.find_element(By.CSS_SELECTOR, 'body > app-root > app-sidenav-responsive > div > mat-sidenav-container > mat-sidenav-content > router-outlet > app-ai > div > mat-card > mat-list:nth-child(2) > mat-card:nth-child(2) > div:nth-child(4) > mat-card:nth-child(1) > div > mat-card:nth-child(2) > app-ptz-control > div > div > div.flex-col > div.flex-row > button:nth-child(3)')
preset_apply.click()

ptz_u = pyautogui.locateOnScreen('ptz_up.png')
pyautogui.mouseDown(ptz_u)
time.sleep(3)
preset_no = driver.find_element(By.CSS_SELECTOR, '#mat-input-2')
preset_no.clear()
preset_no.click()
preset_no.send_keys("2") # Preset 2
time.sleep(1)
preset_apply.click()
print('Preset 1,2 set OK')

preset_no = driver.find_element(By.CSS_SELECTOR, '#mat-input-2')
preset_no.clear()
preset_no.click()
preset_no.send_keys("1")
preset_mv = driver.find_element(By.CSS_SELECTOR, 'body > app-root > app-sidenav-responsive > div > mat-sidenav-container > mat-sidenav-content > router-outlet > app-ai > div > mat-card > mat-list:nth-child(2) > mat-card:nth-child(2) > div:nth-child(4) > mat-card:nth-child(1) > div > mat-card:nth-child(2) > app-ptz-control > div > div > div.flex-col > div.flex-row > button:nth-child(2) > span')
preset_mv.click() # Preset 이동
print('Preset 1 move OK')

pyautogui.scroll(-500)   
home_off = driver.find_element(By.ID, 'mat-button-toggle-5')
home_off.click()
home_on = driver.find_element(By.ID, 'mat-button-toggle-4')
home_on.click() # 홈위치 사용
time.sleep(1)
print('PTZ Home enable OK')

ptz_d = pyautogui.locateOnScreen('ptz_down.png')
pyautogui.mouseDown(ptz_d)
time.sleep(5)
home_apply = driver.find_element(By.CSS_SELECTOR, 'body > app-root > app-sidenav-responsive > div > mat-sidenav-container > mat-sidenav-content > router-outlet > app-ai > div > mat-card > mat-list:nth-child(2) > mat-card:nth-child(2) > div:nth-child(4) > mat-card:nth-child(2) > div:nth-child(2) > div.flex-col > div > button')
home_apply.click() # 홈 위치 설정
ptz_r = pyautogui.locateOnScreen('ptz_right.png')
pyautogui.mouseDown(ptz_r)
time.sleep(4)
home_mv = driver.find_element(By.CSS_SELECTOR, 'body > app-root > app-sidenav-responsive > div > mat-sidenav-container > mat-sidenav-content > router-outlet > app-ai > div > mat-card > mat-list:nth-child(2) > mat-card:nth-child(2) > div:nth-child(4) > mat-card:nth-child(2) > div:nth-child(2) > div.flex-col > div > app-btn-move > button > span')
home_mv.click() # 홈 위치 이동
print('PTZ Home move OK\n----------------------------------------------------------------------------------------------------------------')
