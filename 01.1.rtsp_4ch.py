from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

import time

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

#카메라 등록 페이지
url = 'http://172.16.4.114/web/#/web/camera-setting'
driver.get(url)

#채널1번
ch1 = driver.find_element(By.CSS_SELECTOR, '#mat-input-12')
ch1.clear()
ch1.click()
(
action.send_keys('Test!테스트@#123').key_down(Keys.TAB).send_keys('rtsp://172.16.4.164/video1+audio1').key_down(Keys.TAB)
.send_keys('admin').key_down(Keys.TAB).send_keys('pass0001!').perform()
)
#채널2번
ch2 = driver.find_element(By.CSS_SELECTOR, '#mat-input-18')
ch2.clear()
ch2.click()
(
action.send_keys('QA!한글00000456').key_down(Keys.TAB).send_keys('rtsp://172.16.4.163/video1+audio1').key_down(Keys.TAB)
.send_keys('admin').key_down(Keys.TAB).send_keys('pass0001!').perform()
)
#채널3번
ch3 = driver.find_element(By.CSS_SELECTOR, '#mat-input-24')
ch3.clear()
ch3.click()
(
action.send_keys('InetlliVIX연결999').key_down(Keys.TAB).send_keys('rtsp://172.16.4.119/ch1/stream1/media.imp').key_down(Keys.TAB)
.send_keys('intellivix').key_down(Keys.TAB).send_keys('pass0001!').perform()
)
#채널4번_PTZ
ch4 = driver.find_element(By.CSS_SELECTOR, '#mat-input-30')
ch4.clear()
ch4.click()
(
action.send_keys('PTZ카메라연결').key_down(Keys.TAB).send_keys('rtsp://172.16.4.163/video1+audio1').key_down(Keys.TAB)
.send_keys('admin').key_down(Keys.TAB).send_keys('Pass0001!').perform()
)
ch4PTZlist = driver.find_element(By.CSS_SELECTOR, 'body > app-root > app-sidenav-responsive > div > mat-sidenav-container > mat-sidenav-content > app-camera-setting > div > mat-card > form > mat-table > mat-row:nth-child(9) > mat-cell.mat-cell.cdk-column-conType.mat-column-conType.ng-star-inserted > mat-form-field')
ch4PTZlist.click()
ch4PTZ = driver.find_element(By.CSS_SELECTOR, '#mat-option-157 > span')
ch4PTZ.click()

driver.find_element(By.CSS_SELECTOR, 'body > app-root > app-sidenav-responsive > div > mat-sidenav-container > mat-sidenav-content > app-camera-setting > div > mat-card > form > div > app-btn-apply > button').click()

#라이브 페이지
driver.get('http://172.16.4.114/web/#/web/live')

#라이브 채널별 스트린샷
time.sleep(3)
driver.get_screenshot_as_file('live_ch1.png')

mv1 = driver.find_element(By.CSS_SELECTOR,"body > app-root > app-sidenav-responsive > div > mat-sidenav-container > mat-sidenav-content > app-live > div.flex-container > mat-list > mat-card > div > mat-form-field")
mv1.click()
mv2 = driver.find_element(By.CSS_SELECTOR,"#mat-option-203 > span")
mv2.click()
time.sleep(3)
driver.get_screenshot_as_file('live_ch2.png')

mv2 = driver.find_element(By.CSS_SELECTOR,"body > app-root > app-sidenav-responsive > div > mat-sidenav-container > mat-sidenav-content > app-live > div.flex-container > mat-list > mat-card > div > mat-form-field")
mv2.click()
mv3 = driver.find_element(By.CSS_SELECTOR, '#mat-option-204 > span')
mv3.click()
time.sleep(3)
driver.get_screenshot_as_file('live_ch3.png')

mv3 = driver.find_element(By.CSS_SELECTOR,"body > app-root > app-sidenav-responsive > div > mat-sidenav-container > mat-sidenav-content > app-live > div.flex-container > mat-list > mat-card > div > mat-form-field")
mv3.click()
mv4 = driver.find_element(By.CSS_SELECTOR, '#mat-option-205 > span')
mv4.click()
time.sleep(3)
driver.get_screenshot_as_file('live_ch4.png')
