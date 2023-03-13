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

driver.get('http://172.16.6.230/web/#/web/auth')
action = ActionChains(driver)

driver.find_element(By.CLASS_NAME, 'mat-form-field-infix')
(action.send_keys('admin').key_down(Keys.TAB).send_keys('Pass0001!').pause(1).key_down(Keys.ENTER).perform())
action.reset_actions
time.sleep(1)
print('Login OK\n----------------------------------------------------------------')

driver.get('http://172.16.6.230/web/#/web/network-setting') # 네트워크 페이지
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, '#mat-button-toggle-26-button').click() # 네트워크 DHCP
print('Network DHCP complete!\n----------------------------------------------------------------')
time.sleep(0.5)
driver.find_element(By.ID, 'mat-button-toggle-25').click() # 네트워크 수동
pyautogui.scroll(-300)

network_set = driver.find_element(By.CSS_SELECTOR, '#mat-input-12')
network_set.clear()
network_set.click()
( #네트워크 수동 입력
    action.send_keys('172.16.6.230').key_down(Keys.TAB).send_keys('255.255.255.0').key_down(Keys.TAB).send_keys('172.16.6.1').key_down(Keys.TAB).send_keys('1.1.1.1').key_down(Keys.TAB)
    .send_keys('80').key_down(Keys.TAB).send_keys('554').perform()
)
action.reset_actions
time.sleep(1)
network_apply = driver.find_element(By.CSS_SELECTOR, 'body > app-root > app-sidenav-responsive > div > mat-sidenav-container > mat-sidenav-content > app-network-setting > div > mat-card > div:nth-child(6) > app-btn-apply > button > span')
#network_apply.click()
print('Network Static complete!\n----------------------------------------------------------------')
