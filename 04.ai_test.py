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
action.send_keys('admin').key_down(Keys.TAB).send_keys('Pass0001!').pause(1).key_down(Keys.ENTER).perform()
)
action.reset_actions
time.sleep(2)

#영상분석 페이지
url = 'http://172.16.4.114/web/#/web/ai'
driver.get(url)
time.sleep(2)
pyautogui.scroll(-300)
time.sleep(3)

ai_all = pyautogui.locateOnScreen('ai_all.png')
pyautogui.click(ai_all)
time.sleep(1)

ai_event = pyautogui.locateOnScreen('event.png')
pyautogui.click(ai_event)
time.sleep(1)

dnn = pyautogui.locateOnScreen('dnn_set.png')
pyautogui.click(dnn)

# pyautogui.locateCenterOnScreen('ptz_right.png', grayscale=True, confidence=0.7)
# pyautogui.click()
# pyautogui.click(clicks=10, interval=0.5)
#ai_all = pyautogui.locateOnScreen('ai_all.png')
#pyautogui.click(ai_all)
#time.sleep(1)

#ai_event 
# = pyautogui.locateOnScreen('event.png')
#pyautogui.click(ai_event)
#time.sleep(1)

#dnn = pyautogui.locateOnScreen('dnn_set.png')
#pyautogui.click(dnn)

# pyautogui.locateCenterOnScreen('ptz_right.png', grayscale=True, confidence=0.7)
# pyautogui.click()
# pyautogui.click(clicks=10, interval=0.5)
