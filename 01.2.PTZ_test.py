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


url = 'http://172.16.4.114/web/#/web/auth'
driver.get(url)
action = ActionChains(driver)

#로그인
driver.find_element(By.CLASS_NAME, 'mat-form-field-infix')
(
action.send_keys('admin').key_down(Keys.TAB)
.send_keys('Pass0001!').pause(1).key_down(Keys.ENTER).perform()
)
action.reset_actions
time.sleep(2)

mv_list = driver.find_element(By.CSS_SELECTOR,"body > app-root > app-sidenav-responsive > div > mat-sidenav-container > mat-sidenav-content > app-live > div.flex-container > mat-list > mat-card > div > mat-form-field")
mv_list.click()
mv_ch4 = driver.find_element(By.ID, 'mat-option-1')
#mv_ch4 = driver.find_element(By.CSS_SELECTOR, '#mat-option-3 > span')
mv_ch4.click()
time.sleep(2)

pyautogui.scroll(-1000)
time.sleep(3)
#ptzcontroll = driver.find_element(By.XPATH, '/html/body/app-root/app-sidenav-responsive/div/mat-sidenav-container/mat-sidenav-content/app-live/div[1]/mat-card[2]/div/app-ptz-control/div/div/div[2]/mat-slider/div/div[2]/div')
#action.move_to_element(ptzcontroll).perform()
#time.sleep(3)

ptz_r = pyautogui.locateOnScreen('ptz_right.png')
pyautogui.mouseDown(ptz_r)
time.sleep(3)
ptz_l = pyautogui.locateOnScreen('ptz_left.png')
pyautogui.mouseDown(ptz_l)
time.sleep(3)
ptz_u = pyautogui.locateOnScreen('ptz_up.png')
pyautogui.mouseDown(ptz_u)
time.sleep(3)
ptz_d = pyautogui.locateOnScreen('ptz_down.png')
pyautogui.mouseDown(ptz_d)
time.sleep(3)
ptz_dl = pyautogui.locateOnScreen('ptz_downleft.png')
pyautogui.mouseDown(ptz_dl)
time.sleep(3)
ptz_dr = pyautogui.locateOnScreen('ptz_downright.png')
pyautogui.mouseDown(ptz_dr)
time.sleep(3)
ptz_ul = pyautogui.locateOnScreen('ptz_upleft.png')
pyautogui.mouseDown(ptz_ul)
time.sleep(3)
ptz_ur = pyautogui.locateOnScreen('ptz_upright.png')
pyautogui.mouseDown(ptz_ur)
time.sleep(3)
pyautogui.click()


#pyautogui.locateCenterOnScreen('ptz_right.png', grayscale=True, confidence=0.7)
#pyautogui.click()
#pyautogui.click(clicks=10, interval=0.5)
