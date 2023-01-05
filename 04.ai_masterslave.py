from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

import time
import pyautogui

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
time.sleep(1)
ch_list = driver.find_element(By.CSS_SELECTOR,'#chSelect > div > div.mat-select-arrow-wrapper')
ch_list.click()
ch2_mv = driver.find_element(By.XPATH, '//*[@id="mat-option-27"]/span')
ch2_mv.click()
master_pg = driver.find_element(By.ID, 'mat-tab-label-0-4') #마스터 슬레이브 페이지
master_pg.click()
time.sleep(2)

master_list = driver.find_element(By.ID, 'mat-select-1') #mast1 slave2
master_list.click()
master_ch1 = driver.find_element(By.ID, 'mat-option-14')
master_ch1.click()
slave_list = driver.find_element(By.ID, 'mat-select-2') #mast1 slave2
slave_list.click()
slave_ch2 = driver.find_element(By.ID, 'mat-option-15')
slave_ch2.click()
list_add = driver.find_element(By.XPATH, '//*[@id="mat-tab-content-0-4"]/div/mat-list/div[3]/div/mat-list[1]/mat-card/div/div[2]/app-btn-add-logined/button/span')
list_add.click()
time.sleep(2)

# 연동 추적 설정 페이지
btn_set = driver.find_element(By.XPATH, '//*[@id="mat-tab-content-0-4"]/div/mat-list/div[3]/div/mat-list[2]/mat-card/div[2]/form/mat-table/mat-row/mat-cell[4]/button')
btn_set.click()
time.sleep(3) # 마스터 슬레이브 라이브 출력 대기

pyautogui.scroll(-800)
btn_select_all = driver.find_element(By.CSS_SELECTOR, 'body > app-root > app-sidenav-responsive > div > mat-sidenav-container > mat-sidenav-content > router-outlet > app-ai > div > mat-card > mat-list:nth-child(2) > mat-card:nth-child(2) > div:nth-child(3) > mat-list > mat-card.mat-card.ng-star-inserted > div > div:nth-child(2) > app-btn-select-all')
btn_select_all.click()
# btn_deselect_all = driver.find_element(By.CSS_SELECTOR, 'body > app-root > app-sidenav-responsive > div > mat-sidenav-container > mat-sidenav-content > router-outlet > app-ai > div > mat-card > mat-list:nth-child(2) > mat-card:nth-child(2) > div:nth-child(3) > mat-list > mat-card.mat-card.ng-star-inserted > div > div:nth-child(2) > app-btn-deselect-all')
# btn_deselect_all.click()
btn_delete = driver.find_element(By.CSS_SELECTOR, 'body > app-root > app-sidenav-responsive > div > mat-sidenav-container > mat-sidenav-content > router-outlet > app-ai > div > mat-card > mat-list:nth-child(2) > mat-card:nth-child(2) > div:nth-child(3) > mat-list > mat-card.mat-card.ng-star-inserted > div > div:nth-child(2) > app-btn-delete')
btn_delete.click()
time.sleep(1)

pyautogui.click(717, 280) # 마스터 좌표1
master_position_no = driver.find_element(By.ID, 'mat-input-0')
master_position_no.clear()
master_position_no.click()
master_position_no.send_keys('1')
time.sleep(0.5)
ptz_u = pyautogui.locateOnScreen('ptz_up.png')
pyautogui.mouseDown(ptz_u)
time.sleep(1)
master_position_add = driver.find_element(By.CSS_SELECTOR, 'body > app-root > app-sidenav-responsive > div > mat-sidenav-container > mat-sidenav-content > router-outlet > app-ai > div > mat-card > mat-list:nth-child(2) > mat-card:nth-child(2) > div:nth-child(3) > mat-list > mat-card:nth-child(1) > div.flex-row > div > div > app-btn-add-change > button')
master_position_add.click()
time.sleep(2)
master_position_no = driver.find_element(By.ID, 'mat-input-0')
master_position_no.clear()
master_position_no.click()
master_position_no.send_keys('2')
pyautogui.click(617, 280) # 마스터 좌표2
ptz_d = pyautogui.locateOnScreen('ptz_down.png')
pyautogui.mouseDown(ptz_d)
time.sleep(1)
master_position_add = driver.find_element(By.CSS_SELECTOR, 'body > app-root > app-sidenav-responsive > div > mat-sidenav-container > mat-sidenav-content > router-outlet > app-ai > div > mat-card > mat-list:nth-child(2) > mat-card:nth-child(2) > div:nth-child(3) > mat-list > mat-card:nth-child(1) > div.flex-row > div > div > app-btn-add-change > button')
master_position_add.click()
time.sleep(1)
master_position_no = driver.find_element(By.ID, 'mat-input-0') 
master_position_no.clear()
master_position_no.click()
master_position_no.send_keys('3')
pyautogui.click(617, 370) # 마스터 좌표3 > 좌표3까지 PTZ 컨트롤러로 적용
ptz_dl = pyautogui.locateOnScreen('ptz_downleft.png')
pyautogui.mouseDown(ptz_dl)
time.sleep(1)
master_position_add = driver.find_element(By.CSS_SELECTOR, 'body > app-root > app-sidenav-responsive > div > mat-sidenav-container > mat-sidenav-content > router-outlet > app-ai > div > mat-card > mat-list:nth-child(2) > mat-card:nth-child(2) > div:nth-child(3) > mat-list > mat-card:nth-child(1) > div.flex-row > div > div > app-btn-add-change > button')
master_position_add.click()
master_position_no = driver.find_element(By.ID, 'mat-input-0') 
master_position_no.clear()
master_position_no.click()
master_position_no.send_keys('4')
pyautogui.click(717, 370) # 마스터 좌표4 > 프리셋으로 추가
preset_no = driver.find_element(By.CSS_SELECTOR, '#mat-input-1')
preset_no.clear()
preset_no.click()
preset_no.send_keys("2")
master_position_add = driver.find_element(By.CSS_SELECTOR, 'body > app-root > app-sidenav-responsive > div > mat-sidenav-container > mat-sidenav-content > router-outlet > app-ai > div > mat-card > mat-list:nth-child(2) > mat-card:nth-child(2) > div:nth-child(3) > mat-list > mat-card:nth-child(1) > div.flex-row > div > div > app-btn-add-change > button')
master_position_add.click()
master_position_no = driver.find_element(By.ID, 'mat-input-0') 
master_position_no.clear()
master_position_no.click()
master_position_no.send_keys('5')
pyautogui.click(817, 370) # 마스터 좌표5 > 프리셋으로 추가
preset_no = driver.find_element(By.CSS_SELECTOR, '#mat-input-1')
preset_no.clear()
preset_no.click()
preset_no.send_keys("2")
master_position_add = driver.find_element(By.CSS_SELECTOR, 'body > app-root > app-sidenav-responsive > div > mat-sidenav-container > mat-sidenav-content > router-outlet > app-ai > div > mat-card > mat-list:nth-child(2) > mat-card:nth-child(2) > div:nth-child(3) > mat-list > mat-card:nth-child(1) > div.flex-row > div > div > app-btn-add-change > button')
master_position_add.click()

btn_set_apply = driver.find_element(By.XPATH, '/html/body/app-root/app-sidenav-responsive/div/mat-sidenav-container/mat-sidenav-content/router-outlet/app-ai/div/mat-card/mat-list[1]/mat-card[2]/div[2]/mat-list/mat-card[2]/form/div/app-btn-apply/button')
btn_set_apply.click()
time.sleep(0.5)
popup_btn_apply = driver.find_element(By.XPATH, '//*[@id="mat-dialog-4"]/app-dialogs/div[2]/button/span')
popup_btn_apply.click()
btn_apply = driver.find_element(By.XPATH, '//*[@id="mat-tab-content-0-4"]/div/mat-list/div[3]/div/mat-list[2]/div/app-btn-apply/button/span')
btn_apply.click()

auto_traking_btn = driver.find_element(By.ID, 'mat-button-toggle-2-button') # 자동추적 켜짐
auto_traking_btn.click()
analysis_btn = driver.find_element(By.ID, 'mat-button-toggle-61-button') # 영상분석 켜짐
analysis_btn.click()

url = 'http://172.16.4.114/web/#/web/live' # 라이브 채널로 이동
driver.get(url)
time.sleep(3)
driver.get_screenshot_as_file('masterslave_ch1.png') # 마스터채널1 스크린샷
mv1 = driver.find_element(By.CSS_SELECTOR,"body > app-root > app-sidenav-responsive > div > mat-sidenav-container > mat-sidenav-content > app-live > div.flex-container > mat-list > mat-card > div > mat-form-field")
mv1.click()
mv2 = driver.find_element(By.CSS_SELECTOR,"#mat-option-43")
mv2.click()
time.sleep(5)
driver.get_screenshot_as_file('masterslave_ch2.png') # 슬레이브채널2 스크린샷
