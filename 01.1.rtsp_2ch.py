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
#채널2번_PTZ
ch2 = driver.find_element(By.CSS_SELECTOR, '#mat-input-18')
ch2.clear()
ch2.click()
(
action.send_keys('QA!한글00000456').key_down(Keys.TAB).send_keys('rtsp://172.16.4.163/video1+audio1').key_down(Keys.TAB)
.send_keys('admin').key_down(Keys.TAB).send_keys('Pass0001!').perform()
)

ch2PTZlist = driver.find_element(By.ID, 'mat-select-10')
ch2PTZlist.click()
ch2PTZ = driver.find_element(By.CSS_SELECTOR, '#mat-option-61')
ch2PTZ.click()

driver.find_element(By.CSS_SELECTOR, 'body > app-root > app-sidenav-responsive > div > mat-sidenav-container > mat-sidenav-content > app-camera-setting > div > mat-card > form > div > app-btn-apply > button').click()

#라이브 페이지
driver.get('http://172.16.4.114/web/#/web/live')

#라이브 채널별 스트린샷
# time.sleep(3)
# driver.get_screenshot_as_file('live_ch1.png')
# 
# mv1 = driver.find_element(By.CSS_SELECTOR,"body > app-root > app-sidenav-responsive > div > mat-sidenav-container > mat-sidenav-content > app-live > div.flex-container > mat-list > mat-card > div > mat-form-field")
# mv1.click()
# mv2 = driver.find_element(By.CSS_SELECTOR,"#mat-option-203 > span")
# mv2.click()
# time.sleep(3)
# driver.get_screenshot_as_file('live_ch2.png')
# 
# mv2 = driver.find_element(By.CSS_SELECTOR,"body > app-root > app-sidenav-responsive > div > mat-sidenav-container > mat-sidenav-content > app-live > div.flex-container > mat-list > mat-card > div > mat-form-field")
# mv2.click()
# mv3 = driver.find_element(By.CSS_SELECTOR, '#mat-option-204 > span')
# mv3.click()
# time.sleep(3)
# driver.get_screenshot_as_file('live_ch3.png')
# 
# mv3 = driver.find_element(By.CSS_SELECTOR,"body > app-root > app-sidenav-responsive > div > mat-sidenav-container > mat-sidenav-content > app-live > div.flex-container > mat-list > mat-card > div > mat-form-field")
# mv3.click()
# mv4 = driver.find_element(By.CSS_SELECTOR, '#mat-option-205 > span')
# mv4.click()
# time.sleep(3)
# driver.get_screenshot_as_file('live_ch4.png')

osd_btn = driver.find_element(By.CSS_SELECTOR, 'body > app-root > app-sidenav-responsive > div > mat-sidenav-container > mat-sidenav-content > app-live > div.flex-container > mat-card:nth-child(3) > div > button')
osd_btn.click() # 1채널 화면 표시 팝업 출력
time.sleep(1)
osd_eventbox = driver.find_element(By.ID, 'mat-checkbox-3') # default enable
osd_eventbox.click()
osd_object_id = driver.find_element(By.ID, 'mat-checkbox-4')
osd_object_id.click()
osd_object_category = driver.find_element(By.ID, 'mat-checkbox-5')
osd_object_category.click()
osd_eventmsg = driver.find_element(By.ID, 'mat-checkbox-6')
osd_eventmsg.click()
osd_count = driver.find_element(By.ID, 'mat-checkbox-7') # default disable 이벤트 영역 활성화시 enable 처리
osd_numberplate = driver.find_element(By.ID, 'mat-checkbox-8')
osd_numberplate.click()
osd_eventzone = driver.find_element(By.ID, 'mat-checkbox-9')
osd_eventzone.click()
osd_objectzone = driver.find_element(By.ID, 'mat-checkbox-10')
osd_objectzone.click()
osd_nonobjectzone = driver.find_element(By.ID, 'mat-checkbox-11')
osd_nonobjectzone.click()
osd_dynamiczone = driver.find_element(By.ID, 'mat-checkbox-12')
osd_dynamiczone.click()
osd_roizone = driver.find_element(By.ID, 'mat-checkbox-13').click

