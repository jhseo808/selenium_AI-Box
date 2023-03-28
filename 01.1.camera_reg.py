from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

import time
import os
try:
    os.makedirs('D:\Auto_test')
    print('Auto테스트 파일이 생성되었습니다.')
except FileExistsError as a:
    print(a)

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

driver.get('http://172.16.6.230/web/#/web/camera-setting') # 카메라 등록 페이지

# 카메라 삭제
for i in range(1, 5):
    ch_xpath = f"/html/body/app-root/app-sidenav-responsive/div/mat-sidenav-container/mat-sidenav-content/app-camera-setting/div/mat-card/form/mat-table/mat-row[{2*i-1}]/mat-cell[1]/button"
    driver.find_element(By.XPATH, ch_xpath).click()
    print(f'Ch{i} delete')

driver.find_element(By.CSS_SELECTOR, \
   'body > app-root > app-sidenav-responsive > div > mat-sidenav-container > mat-sidenav-content > app-camera-setting > div > mat-card > form > div > app-btn-apply > button'\
       ).click()
print('All Ch delete complete!\n------------------------------------------------------------')
time.sleep(5)

# 카메라 등록
ch1 = driver.find_element(By.CSS_SELECTOR, '#mat-input-12')
ch1.clear()
ch1.click()
(action.send_keys('Test!테스트@#123').key_down(Keys.TAB).send_keys('rtsp://172.16.6.200:554/profile2/media.smp').key_down(Keys.TAB)
 .send_keys('admin').key_down(Keys.TAB).send_keys('Pass0001!').perform())
print('Ch1 register')
ch2 = driver.find_element(By.CSS_SELECTOR, '#mat-input-18')
ch2.clear()
ch2.click()
(action.send_keys('QA!한글00000456').key_down(Keys.TAB).send_keys('rtsp://172.16.6.203/video1+audio1').key_down(Keys.TAB)
 .send_keys('admin').key_down(Keys.TAB).send_keys('admin').perform())
print('Ch2 register')
ch3 = driver.find_element(By.CSS_SELECTOR, '#mat-input-24')
ch3.clear()
ch3.click()
(action.send_keys('InetlliVIX연결999').key_down(Keys.TAB).send_keys('rtsp://172.16.6.204:554/0/onvif/profile2/media.smp').key_down(Keys.TAB)
 .send_keys('admin').key_down(Keys.TAB).send_keys('pass0001!').perform())
print('Ch3 register')
ch4 = driver.find_element(By.CSS_SELECTOR, '#mat-input-30')
ch4.clear()
ch4.click()
(
    action.send_keys('PTZ카메라연결').key_down(Keys.TAB).send_keys('rtsp://172.16.6.202/video1+audio1').key_down(Keys.TAB)
    .send_keys('admin').key_down(Keys.TAB).send_keys('Pass0001!').perform()
)
ch4PTZlist = driver.find_element(By.CSS_SELECTOR, 'body > app-root > app-sidenav-responsive > div > mat-sidenav-container > mat-sidenav-content > app-camera-setting > div > mat-card > form > mat-table > mat-row:nth-child(9) > mat-cell.mat-cell.cdk-column-conType.mat-column-conType.ng-star-inserted > mat-form-field')
ch4PTZlist.click()
ch4PTZ = driver.find_element(By.CSS_SELECTOR, '#mat-option-157 > span')
ch4PTZ.click()
print('Ch4 PTZ register')

driver.find_element(By.CSS_SELECTOR, \
    'body > app-root > app-sidenav-responsive > div > mat-sidenav-container > mat-sidenav-content > app-camera-setting > div > mat-card > form > div > app-btn-apply > button'\
        ).click() # 카메라 페이지 적용
print('All Ch register complete!\n------------------------------------------------------------')
driver.get_screenshot_as_file('D:\Auto_test\camera_list.png')
