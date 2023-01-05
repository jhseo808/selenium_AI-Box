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

#시스템 > 정보
url = 'http://172.16.4.114/web/#/web/information'
driver.get(url)
time.sleep(1)

device_name = driver.find_element(By.CSS_SELECTOR, '#mat-input-12')
device_name.clear()
device_name.click()
action.send_keys('test장치명12!@#').perform()

apply_btn = driver.find_element(By.CSS_SELECTOR, 'body > app-root > app-sidenav-responsive > div > mat-sidenav-container > mat-sidenav-content > app-information > div > mat-card > div:nth-child(6) > app-btn-apply > button > span')
apply_btn.click()

#시스템 > 리소스 모니터
url = 'http://172.16.4.114/web/#/web/resource-monitor'
driver.get(url)
pyautogui.scroll(-300)
time.sleep(1)

#시스템 > 날짜/시간
url = 'http://172.16.4.114/web/#/web/datetime'
driver.get(url)
time.sleep(1)

#시스템 > 업그레이드
url = 'http://172.16.4.114/web/#/web/upgrade'
driver.get(url)
time.sleep(1)

#시스템 > 라이선스
url = 'http://172.16.4.114/web/#/web/license'
driver.get(url)
time.sleep(1)
pyautogui.scroll(-500)

print('>>>>OK>>>>>>')
