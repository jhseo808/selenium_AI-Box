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

url = 'http://172.16.6.230/web/#/web/auth'
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
print('로그인 OK')

url = 'http://172.16.6.230/web/#/web/camera-setting' # 카메라 등록 페이지
driver.get(url)

# driver.find_element(By.XPATH, \
    # '/html/body/app-root/app-sidenav-responsive/div/mat-sidenav-container/mat-sidenav-content/app-camera-setting/div/mat-card/form/mat-table/mat-row[1]/mat-cell[1]/button'\
        # ).click() # 채널 1 카메라 삭제
# print('채널 1 삭제')
# driver.find_element(By.XPATH, \
    # '/html/body/app-root/app-sidenav-responsive/div/mat-sidenav-container/mat-sidenav-content/app-camera-setting/div/mat-card/form/mat-table/mat-row[3]/mat-cell[1]/button'\
        # ).click() # 채널 2 카메라 삭제
# print('채널 2 삭제')
# driver.find_element(By.XPATH, \
    # '/html/body/app-root/app-sidenav-responsive/div/mat-sidenav-container/mat-sidenav-content/app-camera-setting/div/mat-card/form/mat-table/mat-row[5]/mat-cell[1]/button'\
        # ).click() # 채널 3 카메라 삭제
# print('채널 3 삭제')
# driver.find_element(By.XPATH, \
    # '/html/body/app-root/app-sidenav-responsive/div/mat-sidenav-container/mat-sidenav-content/app-camera-setting/div/mat-card/form/mat-table/mat-row[7]/mat-cell[1]/button'\
        # ).click() # 채널 4 카메라 삭제
# print('채널 4 삭제')
# driver.find_element(By.CSS_SELECTOR, \
    # 'body > app-root > app-sidenav-responsive > div > mat-sidenav-container > mat-sidenav-content > app-camera-setting > div > mat-card > form > div > app-btn-apply > button'\
        # ).click() # 카메라 페이지 적용
# print('채널 전체 삭제')

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

driver.find_element(By.CSS_SELECTOR, \
    'body > app-root > app-sidenav-responsive > div > mat-sidenav-container > mat-sidenav-content > app-camera-setting > div > mat-card > form > div > app-btn-apply > button'\
        ).click() # 카메라 페이지 적용
print('4채널 카메라 등록 OK')
driver.get_screenshot_as_file('D:\Auto_test\camera_list.png')

driver.get('http://172.16.6.230/web/#/web/live') # 라이브 페이지

osd_btn = driver.find_element(By.CSS_SELECTOR,\
    'body > app-root > app-sidenav-responsive > div > mat-sidenav-container > mat-sidenav-content > app-live > div.flex-container > mat-card:nth-child(3) > div > button'\
        )
osd_btn.click() # 화면 표시 팝업 출력
time.sleep(1)
driver.find_element(By.ID, 'mat-checkbox-3').click() # 이벤트가 발생한 물체만 표시 (default:enable)
driver.find_element(By.ID, 'mat-checkbox-4').click() # 객체ID
driver.find_element(By.ID, 'mat-checkbox-5').click() # 객체 종류
driver.find_element(By.ID, 'mat-checkbox-6').click() # 이벤트 메시지
driver.find_element(By.ID, 'mat-checkbox-8').click() # 차량 번호   
driver.find_element(By.ID, 'mat-checkbox-9').click()  # 이벤트 영역
driver.find_element(By.ID, 'mat-checkbox-10').click() # 객체 감지 영역
driver.find_element(By.ID, 'mat-checkbox-11').click() # 객체 비감지 영역
driver.find_element(By.ID, 'mat-checkbox-12').click() # 동적 배경 영역
driver.find_element(By.ID, 'mat-checkbox-13').click() # 객체 감지 ROI
driver.find_element(By.ID, 'mat-checkbox-7').click() # 계수기 (default:disable)
osd_apply_btn = driver.find_element(By.XPATH, '//*[@id="mat-dialog-0"]/display-option-dialog/div/div[2]/button[1]/span')
osd_apply_btn.click() # 화면 표시 팝업 적용
print('화면 표시 팝업 OK')

driver.find_element(By.XPATH,\
    '/html/body/app-root/app-sidenav-responsive/div/mat-sidenav-container/mat-sidenav-content/app-live/div[1]/mat-list/mat-card/div/button/span'\
        ).click() # 1채널 계수기 초기화
print('1채널 계수기 초기화 OK')
time.sleep(1)
driver.find_element(By.CSS_SELECTOR,\
    'body > app-root > app-sidenav-responsive > div > mat-sidenav-container > mat-sidenav-content > app-live > div.flex-container > mat-list > mat-card > div > app-btn-va-restart'\
        ).click() # 1채널 영상 분석 재시작
print('1채널 영상 분석 재시작 OK')

#라이브 채널별 스트린샷
time.sleep(3)
driver.get_screenshot_as_file('D:\Auto_test\live_ch1.png')
print('1채널 라이브 화면 OK')

mv1 = driver.find_element(By.CSS_SELECTOR,"body > app-root > app-sidenav-responsive > div > mat-sidenav-container > mat-sidenav-content > app-live > div.flex-container > mat-list > mat-card > div > mat-form-field")
mv1.click()
mv2 = driver.find_element(By.CSS_SELECTOR,"#mat-option-203 > span")
mv2.click()
time.sleep(3)
driver.get_screenshot_as_file('D:\Auto_test\live_ch2.png')
print('2채널 라이브 화면 OK')
driver.find_element(By.XPATH,\
    '/html/body/app-root/app-sidenav-responsive/div/mat-sidenav-container/mat-sidenav-content/app-live/div[1]/mat-list/mat-card/div/button/span'\
        ).click() # 2채널 계수기 초기화
print('2채널 계수기 초기화 OK')
time.sleep(1)
driver.find_element(By.CSS_SELECTOR,\
    'body > app-root > app-sidenav-responsive > div > mat-sidenav-container > mat-sidenav-content > app-live > div.flex-container > mat-list > mat-card > div > app-btn-va-restart'\
        ).click() # 2채널 영상 분석 재시작
print('2채널 영상 분석 재시작 OK')

mv2 = driver.find_element(By.CSS_SELECTOR,"body > app-root > app-sidenav-responsive > div > mat-sidenav-container > mat-sidenav-content > app-live > div.flex-container > mat-list > mat-card > div > mat-form-field")
mv2.click()
mv3 = driver.find_element(By.CSS_SELECTOR, '#mat-option-204 > span')
mv3.click()
time.sleep(3)
driver.get_screenshot_as_file('D:\Auto_test\live_ch3.png')
print('3채널 라이브 화면 OK')

driver.find_element(By.XPATH,\
    '/html/body/app-root/app-sidenav-responsive/div/mat-sidenav-container/mat-sidenav-content/app-live/div[1]/mat-list/mat-card/div/button/span'\
        ).click() # 3채널 계수기 초기화
print('3채널 계수기 초기화 OK')
time.sleep(1)
driver.find_element(By.CSS_SELECTOR,\
    'body > app-root > app-sidenav-responsive > div > mat-sidenav-container > mat-sidenav-content > app-live > div.flex-container > mat-list > mat-card > div > app-btn-va-restart'\
        ).click() # 3채널 영상 분석 재시작
print('3채널 영상 분석 재시작 OK')

mv3 = driver.find_element(By.CSS_SELECTOR,"body > app-root > app-sidenav-responsive > div > mat-sidenav-container > mat-sidenav-content > app-live > div.flex-container > mat-list > mat-card > div > mat-form-field")
mv3.click()
mv4 = driver.find_element(By.CSS_SELECTOR, '#mat-option-205 > span')
mv4.click()
time.sleep(3)
driver.get_screenshot_as_file('D:\Auto_test\live_ch4.png')
print('4채널 라이브 화면 OK')

driver.find_element(By.XPATH,\
    '/html/body/app-root/app-sidenav-responsive/div/mat-sidenav-container/mat-sidenav-content/app-live/div[1]/mat-list/mat-card/div/button/span'\
        ).click() # 4채널 계수기 초기화
print('4채널 계수기 초기화 OK')
time.sleep(1)
driver.find_element(By.CSS_SELECTOR,\
    'body > app-root > app-sidenav-responsive > div > mat-sidenav-container > mat-sidenav-content > app-live > div.flex-container > mat-list > mat-card > div > app-btn-va-restart'\
        ).click() # 4채널 영상 분석 재시작
print('4채널 영상 분석 재시작 OK')
