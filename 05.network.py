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

#네트워크 페이지
url = 'http://172.16.4.114/web/#/web/network-setting'
driver.get(url)
time.sleep(1)

network_DHCP = driver.find_element(By.CSS_SELECTOR, '#mat-button-toggle-26-button')
network_DHCP.click()
time.sleep(0.5)
network_manual = driver.find_element(By.ID, 'mat-button-toggle-25')
network_manual.click()
pyautogui.scroll(-300)

#네트워크 수동 입력
network_set = driver.find_element(By.CSS_SELECTOR, '#mat-input-12')
network_set.clear()
network_set.click()
(
    action.send_keys('172.16.4.114').key_down(Keys.TAB).send_keys('255.255.255.0').key_down(Keys.TAB).send_keys('172.16.4.1').key_down(Keys.TAB).send_keys('1.1.1.1').key_down(Keys.TAB)
    .send_keys('80').key_down(Keys.TAB).send_keys('554').perform()
)
action.reset_actions
time.sleep(1)
network_apply = driver.find_element(By.CSS_SELECTOR, 'body > app-root > app-sidenav-responsive > div > mat-sidenav-container > mat-sidenav-content > app-network-setting > div > mat-card > div:nth-child(6) > app-btn-apply > button > span')
#network_apply.click()
