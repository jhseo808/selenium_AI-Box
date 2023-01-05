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

url = 'http://172.16.4.114/web/#/web/auth'
driver.get(url)
action = ActionChains(driver)

#로그인
driver.find_element(By.CLASS_NAME, 'mat-form-field-infix')
(
action.send_keys('admin').key_down(Keys.TAB).send_keys('Pass0001!').pause(1).key_down(Keys.ENTER).perform()
)
action.reset_actions
time.sleep(2)

#영상분석 페이지
url = 'http://172.16.4.114/web/#/web/ai'
driver.get(url)
time.sleep(1)
ch_list = driver.find_element(By.CSS_SELECTOR,'#chSelect > div > div.mat-select-arrow-wrapper')
ch_list.click()
ch2_mv = driver.find_element(By.XPATH, '//*[@id="mat-option-27"]/span')
ch2_mv.click()
ptz_pg = driver.find_element(By.ID, 'mat-tab-label-0-2')
ptz_pg.click()
time.sleep(5)

#PTZ 동작 테스트
#ptz_r = pyautogui.locateOnScreen('ptz_right.png')
#pyautogui.mouseDown(ptz_r)
#time.sleep(1)
#ptz_l = pyautogui.locateOnScreen('ptz_left.png')
#pyautogui.mouseDown(ptz_l)
#time.sleep(1)
#ptz_u = pyautogui.locateOnScreen('ptz_up.png')
#pyautogui.mouseDown(ptz_u)
#time.sleep(1)
#ptz_d = pyautogui.locateOnScreen('ptz_down.png')
#pyautogui.mouseDown(ptz_d)
#time.sleep(1)
#ptz_dl = pyautogui.locateOnScreen('ptz_downleft.png')
#pyautogui.mouseDown(ptz_dl)
#time.sleep(1)
#ptz_dr = pyautogui.locateOnScreen('ptz_downright.png')
#pyautogui.mouseDown(ptz_dr)
#time.sleep(1)
#ptz_ul = pyautogui.locateOnScreen('ptz_upleft.png')
#pyautogui.mouseDown(ptz_ul)
#time.sleep(1)
#ptz_ur = pyautogui.locateOnScreen('ptz_upright.png')
#pyautogui.mouseDown(ptz_ur)
#time.sleep(1)

#preset1
ptz_r = pyautogui.locateOnScreen('ptz_right.png')
pyautogui.mouseDown(ptz_r)
time.sleep(1)
preset_no = driver.find_element(By.CSS_SELECTOR, '#mat-input-2')
preset_no.click()
preset_no.send_keys("1")
time.sleep(2)
preset_apply = driver.find_element(By.CSS_SELECTOR, 'body > app-root > app-sidenav-responsive > div > mat-sidenav-container > mat-sidenav-content > router-outlet > app-ai > div > mat-card > mat-list:nth-child(2) > mat-card:nth-child(2) > div:nth-child(4) > mat-card:nth-child(1) > div > mat-card:nth-child(2) > app-ptz-control > div > div > div.flex-col > div.flex-row > button:nth-child(3)')
preset_apply.click()

#preset2
ptz_u = pyautogui.locateOnScreen('ptz_up.png')
pyautogui.mouseDown(ptz_u)
time.sleep(3)
preset_no = driver.find_element(By.CSS_SELECTOR, '#mat-input-2')
preset_no.clear()
preset_no.click()
preset_no.send_keys("2")
time.sleep(2)

#preset 설정
preset_apply = driver.find_element(By.CSS_SELECTOR, 'body > app-root > app-sidenav-responsive > div > mat-sidenav-container > mat-sidenav-content > router-outlet > app-ai > div > mat-card > mat-list:nth-child(2) > mat-card:nth-child(2) > div:nth-child(4) > mat-card:nth-child(1) > div > mat-card:nth-child(2) > app-ptz-control > div > div > div.flex-col > div.flex-row > button:nth-child(3)')
preset_apply.click()

#preset 이동
preset_no = driver.find_element(By.CSS_SELECTOR, '#mat-input-2')
preset_no.clear()
preset_no.click()
preset_no.send_keys("1")
preset_mv = driver.find_element(By.CSS_SELECTOR, 'body > app-root > app-sidenav-responsive > div > mat-sidenav-container > mat-sidenav-content > router-outlet > app-ai > div > mat-card > mat-list:nth-child(2) > mat-card:nth-child(2) > div:nth-child(4) > mat-card:nth-child(1) > div > mat-card:nth-child(2) > app-ptz-control > div > div > div.flex-col > div.flex-row > button:nth-child(2) > span')
preset_mv.click()

#홈위치 사용
pyautogui.scroll(-500)   
home_off = driver.find_element(By.ID, 'mat-button-toggle-5')
home_off.click()
home_on = driver.find_element(By.ID, 'mat-button-toggle-4')
home_on.click()
time.sleep(1)

#홈 위치 설정
ptz_d = pyautogui.locateOnScreen('ptz_down.png')
pyautogui.mouseDown(ptz_d)
time.sleep(2)
home_apply = driver.find_element(By.CSS_SELECTOR, 'body > app-root > app-sidenav-responsive > div > mat-sidenav-container > mat-sidenav-content > router-outlet > app-ai > div > mat-card > mat-list:nth-child(2) > mat-card:nth-child(2) > div:nth-child(4) > mat-card:nth-child(2) > div:nth-child(2) > div.flex-col > div > button')
home_apply.click()
ptz_r = pyautogui.locateOnScreen('ptz_right.png')
pyautogui.mouseDown(ptz_r)
time.sleep(4)
home_mv = driver.find_element(By.CSS_SELECTOR, 'body > app-root > app-sidenav-responsive > div > mat-sidenav-container > mat-sidenav-content > router-outlet > app-ai > div > mat-card > mat-list:nth-child(2) > mat-card:nth-child(2) > div:nth-child(4) > mat-card:nth-child(2) > div:nth-child(2) > div.flex-col > div > app-btn-move > button > span')
home_mv.click()
