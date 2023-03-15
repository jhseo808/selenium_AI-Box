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

driver.get('http://172.16.6.230/web/#/web/auth')
action = ActionChains(driver)

driver.find_element(By.CLASS_NAME, 'mat-form-field-infix')
(action.send_keys('admin').key_down(Keys.TAB).send_keys('Pass0001!').pause(1).key_down(Keys.ENTER).perform())
action.reset_actions
time.sleep(1)
print('Login OK\n----------------------------------------------------------------')

driver.get('http://172.16.6.230/web/#/web/ai')
time.sleep(1)
cam_list_ai = driver.find_element(By.ID, 'chSelect') # 카메라 리스트
cam_list_ai.click() 
driver.find_element(By.ID, 'mat-option-35').click() # 채널4
master_pg = driver.find_element(By.ID, 'mat-tab-label-0-4') # 마스터 슬레이브 페이지
master_pg.click()
time.sleep(2)
print('Master-Slave Page')

master_list = driver.find_element(By.ID, 'mat-select-1') # 마스터 채널 리스트
master_list.click()
master_ch1 = driver.find_element(By.ID, 'mat-option-18')
master_ch1.click()
slave_list = driver.find_element(By.ID, 'mat-select-2') #mast1 slave2
slave_list.click()
slave_ch2 = driver.find_element(By.ID, 'mat-option-21')
slave_ch2.click()
list_add = driver.find_element(By.XPATH, '//*[@id="mat-tab-content-0-4"]/div/mat-list/div[3]/div/mat-list[1]/mat-card/div/div[2]/app-btn-add-logined/button/span')
list_add.click()
time.sleep(2)
print('Master Ch.1 - Slave Ch.4 Mapping OK')

btn_set = driver.find_element(
    By.XPATH, '//*[@id="mat-tab-content-0-4"]/div/mat-list/div[3]/div/mat-list[2]/mat-card/div[2]/form/mat-table/mat-row/mat-cell[4]/button'
    ) # 연동 추적 설정 페이지
btn_set.click() 
time.sleep(3) # 라이브 출력 대기

pyautogui.scroll(-800)
btn_select_all = driver.find_element(
    By.CSS_SELECTOR, 'body > app-root > app-sidenav-responsive > div > mat-sidenav-container > mat-sidenav-content > router-outlet > app-ai > div > mat-card > mat-list:nth-child(2) > mat-card:nth-child(2) > div:nth-child(3) > mat-list > mat-card.mat-card.ng-star-inserted > div > div:nth-child(2) > app-btn-select-all'
    ) # [전체 선택]
btn_select_all.click() 
# btn_deselect_all = driver.find_element(
    # By.CSS_SELECTOR, 'body > app-root > app-sidenav-responsive > div > mat-sidenav-container > mat-sidenav-content > router-outlet > app-ai > div > mat-card > mat-list:nth-child(2) > mat-card:nth-child(2) > div:nth-child(3) > mat-list > mat-card.mat-card.ng-star-inserted > div > div:nth-child(2) > app-btn-deselect-all'
    # ) # [전체 해제]
# btn_deselect_all.click() 
btn_delete = driver.find_element(
    By.CSS_SELECTOR, 'body > app-root > app-sidenav-responsive > div > mat-sidenav-container > mat-sidenav-content > router-outlet > app-ai > div > mat-card > mat-list:nth-child(2) > mat-card:nth-child(2) > div:nth-child(3) > mat-list > mat-card.mat-card.ng-star-inserted > div > div:nth-child(2) > app-btn-delete'
    ) # [제거]
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
master_position_add = driver.find_element(
    By.CSS_SELECTOR, 'body > app-root > app-sidenav-responsive > div > mat-sidenav-container > mat-sidenav-content > router-outlet > app-ai > div > mat-card > mat-list:nth-child(2) > mat-card:nth-child(2) > div:nth-child(3) > mat-list > mat-card:nth-child(1) > div.flex-row > div > div > app-btn-add-change > button'
    ) # 마스터 좌표 번호 [추가/변경]
master_position_add.click()
time.sleep(2)

master_position_no.clear()
master_position_no.click()
master_position_no.send_keys('2')
pyautogui.click(617, 280) # 마스터 좌표2
ptz_d = pyautogui.locateOnScreen('ptz_down.png')
pyautogui.mouseDown(ptz_d)
time.sleep(1)
master_position_add.click()
time.sleep(1)

master_position_no.clear()
master_position_no.click()
master_position_no.send_keys('3')
pyautogui.click(617, 370) # 마스터 좌표3
ptz_dl = pyautogui.locateOnScreen('ptz_downleft.png')
pyautogui.mouseDown(ptz_dl)
time.sleep(1)
print('Master 1,2,3 / Slave PTZ control OK ')

master_position_add.click()
master_position_no.clear()
master_position_no.click()
master_position_no.send_keys('4')
pyautogui.click(717, 370) # 마스터 좌표4 
preset_no = driver.find_element(By.CSS_SELECTOR, '#mat-input-1')
preset_no.clear()
preset_no.click()
preset_no.send_keys("2")
master_position_add.click()
master_position_no.clear()
master_position_no.click()
master_position_no.send_keys('5')
pyautogui.click(817, 370) # 마스터 좌표5
preset_no.clear()
preset_no.click()
preset_no.send_keys("2")
master_position_add.click()
print('Master 4,5 / Slave Preset OK ')

btn_set_apply = driver.find_element(
    By.XPATH, '/html/body/app-root/app-sidenav-responsive/div/mat-sidenav-container/mat-sidenav-content/router-outlet/app-ai/div/mat-card/mat-list[1]/mat-card[2]/div[2]/mat-list/mat-card[2]/form/div/app-btn-apply/button'
    ) # 연동 추적 설정 페이지 [적용]
btn_set_apply.click()
time.sleep(0.5)
popup_btn_apply = driver.find_element(
    By.XPATH, '//*[@id="mat-dialog-4"]/app-dialogs/div[2]/button/span'
    ) # 연동 추적 설정 팝업 [확인]
popup_btn_apply.click()
btn_apply = driver.find_element(
    By.XPATH, '//*[@id="mat-tab-content-0-4"]/div/mat-list/div[3]/div/mat-list[2]/div/app-btn-apply/button/span'
    ) # 마스터 슬레이브 페이지 [적용]
btn_apply.click()

auto_traking_btn = driver.find_element(By.ID, 'mat-button-toggle-2-button') # 자동추적 켜짐
auto_traking_btn.click()
print('Auto Traking ON')
analysis_btn = driver.find_element(By.ID, 'mat-button-toggle-61-button') # 영상분석 켜짐
analysis_btn.click()
print('VA ON')

live_pg = driver.find_element(
    By.XPATH, '/html/body/app-root/app-sidenav-responsive/div/mat-sidenav-container/mat-sidenav/div/mat-tree/mat-tree-node[1]'
    ) # 라이브
live_pg.click()
time.sleep(3)
cam_list = driver.find_element(By.ID, 'mat-select-11') # 카메라 리스트_라이브
cam_list.click()
driver.find_element(By.ID, 'mat-option-57').click() # 채널4
