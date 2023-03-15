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
cam_list = driver.find_element(By.ID, 'chSelect')
cam_list.click() # 카메라 리스트
driver.find_element(By.ID, 'mat-option-35').click() # 채널4
preset_pg = driver.find_element(By.ID, 'mat-tab-label-0-3')
preset_pg.click() # 프리셋 투어링 페이지
time.sleep(2)
print('Preset List')

pyautogui.scroll(-700)
btn_list_all = driver.find_element(
    By.XPATH, '//*[@id="mat-tab-content-0-3"]/div/mat-list/div[2]/div/app-preset-touring/div/mat-list/div/mat-card/div[1]/div[2]/div/div[1]/button[1]'
    )
btn_list_all.click() # btn [전체 선택] 
time.sleep(0.5)
btn_list_del = driver.find_element(
    By.XPATH, '//*[@id="mat-tab-content-0-3"]/div/mat-list/div[2]/div/app-preset-touring/div/mat-list/div/mat-card/div[1]/div[2]/div/div[2]/button[2]'
    )
btn_list_del.click() # btn [제거]
pyautogui.scroll(-700)
print('Preset List Delete!')

preset_no = driver.find_element(By.CSS_SELECTOR, '#mat-input-8')
preset_no.clear()
preset_no.click() # [프리셋 번호 텍스트창]
preset_no.send_keys("1")
list_add = driver.find_element(
    By.XPATH, '//*[@id="mat-tab-content-0-3"]/div/mat-list/div[2]/div/app-preset-touring/div/mat-list/div/mat-card/div[1]/div[2]/div/div[2]/button[1]'
    )
list_add.click() # btn [추가]
time.sleep(0.5)
preset_no.clear()
preset_no.click()
preset_no.send_keys("2")
list_add.click()
time.sleep(0.5)
pyautogui.scroll(-700)
preset_no.clear()
preset_no.click()
preset_no.send_keys("3")
list_add.click()
time.sleep(0.5)
preset_no.clear()
preset_no.click()
preset_no.send_keys("4")
list_add.click()
time.sleep(0.5)
preset_no.clear()
preset_no.click()
preset_no.send_keys("5")
list_add.click()
time.sleep(0.5)
pyautogui.scroll(-700)
print('Preset 1,2,3,4,5 List Add')
preset_name1 = driver.find_element(By.ID, 'mat-input-27') # 프리셋명 (+3증가)
preset_name1.click()
preset_name1.send_keys('test Preset1!!!!')
preset_name2 = driver.find_element(By.ID, 'mat-input-30')
preset_name2.click()
preset_name2.send_keys('test Preset2!@#')
preset_name3 = driver.find_element(By.ID, 'mat-input-33')
preset_name3.click()
preset_name3.send_keys('test Preset3!테스트')
preset_name4 = driver.find_element(By.ID, 'mat-input-36')
preset_name4.click()
preset_name4.send_keys('test Preset4...1111')
preset_name5 = driver.find_element(By.ID, 'mat-input-39')
preset_name5.click()
preset_name5.send_keys('test Preset5555555')
print('Preset Name Add')

checkbox_1 = driver.find_element(By.ID, 'mat-checkbox-12')
checkbox_1.click()
checkbox_2 = driver.find_element(By.ID, 'mat-checkbox-13')
checkbox_2.click()
btn_down = driver.find_element(
    By.XPATH, '//*[@id="mat-tab-content-0-3"]/div/mat-list/div[2]/div/app-preset-touring/div/mat-list/div/mat-card/div[1]/div[2]/div/div[2]/button[4]'
    )
btn_down.click()
print('Preset 1,2 Check!\nError Popup: 한개의 목록을 선택하십시오!')
time.sleep(1)

checkbox_1.click() # 프리셋 1번 체크 해제, 프리셋2번 체크
btn_down.click()
btn_down.click()
btn_down.click()
btn_up = driver.find_element(
    By.XPATH, '//*[@id="mat-tab-content-0-3"]/div/mat-list/div[2]/div/app-preset-touring/div/mat-list/div/mat-card/div[1]/div[2]/div/div[2]/button[3]'
    )
btn_up.click() # 프리셋 2번 리스트4번으로 이동
checkbox_4 = driver.find_element(By.ID, 'mat-checkbox-15')
checkbox_4.click() # 프리셋 4번 체크
print('Preset 2 Move to Listline4')
checkbox_2.click()
btn_del = driver.find_element(
    By.XPATH, '//*[@id="mat-tab-content-0-3"]/div/mat-list/div[2]/div/app-preset-touring/div/mat-list/div/mat-card/div[1]/div[2]/div/div[2]/button[2]'
    )
btn_del.click()
print('Preset 4 Delete')

preset_eventzone = driver.find_element(
     By.XPATH, '//*[@id="mat-tab-content-0-3"]/div/mat-list/div[2]/div/app-preset-touring/div/mat-list/div/mat-card/div[2]/form/mat-table/mat-row[1]/mat-cell[6]/button'
    )
preset_eventzone.click() # 프리셋 1번 이벤트 영역 설정 페이지 진입

btn_cancel = driver.find_element(
    By.XPATH, '/html/body/app-root/app-sidenav-responsive/div/mat-sidenav-container/mat-sidenav-content/router-outlet/app-ai/div/mat-card/mat-list[1]/div/div/app-btn-cancel/button/span'
    )
btn_cancel.click() # 이벤트 영역 설정 페이지 [취소]
preset_eventzone.click()
btn_apply = driver.find_element(
    By.XPATH, '/html/body/app-root/app-sidenav-responsive/div/mat-sidenav-container/mat-sidenav-content/router-outlet/app-ai/div/mat-card/mat-list[1]/div/div/app-btn-apply/button/span'
    )
btn_apply.click()
time.sleep(2)
popup_apply = driver.find_element(By.XPATH, '//*[@id="mat-dialog-5"]/app-dialogs/div[2]/button')
popup_apply.click()
