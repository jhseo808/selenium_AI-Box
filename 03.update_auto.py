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
time.sleep(1)

#업그레이드 페이지 이동
url = "http://172.16.4.114/web/#/web/upgrade"
driver.get(url)

#파일선택
file_btn = driver.find_element(By.CSS_SELECTOR,"body > app-root > app-sidenav-responsive > div > mat-sidenav-container > mat-sidenav-content > app-upgrade > div > mat-card > mat-list:nth-child(2) > mat-card > div:nth-child(4) > div:nth-child(2) > button > span")
file_btn.click()

#pyautogui.moveTo(554, 946, 1)
#pyautogui.doubleClick()
#pyautogui.click()

time.sleep(1)
pyautogui.typewrite('D:\VIXAI-120G-0200-1.5.14.img')
time.sleep(2)
pyautogui.press('enter')
time.sleep(2)
#pyautogui.moveTo(1222, 879, 1)
#pyautogui.click()

upgrade_btn = driver.find_element(By.CSS_SELECTOR, "body > app-root > app-sidenav-responsive > div > mat-sidenav-container > mat-sidenav-content > app-upgrade > div > mat-card > mat-list:nth-child(2) > mat-card > div:nth-child(5) > app-btn-upgrade > button > span")
upgrade_btn.click()
time.sleep(2)
#upgrade_popup_btn = driver.find_element(By.CSS_SELECTOR, '#mat-dialog-0 > app-confirm-dialog > div.mat-dialog-actions > button.mat-raised-button.mat-primary > span')
#upgrade_popup_btn.click()
