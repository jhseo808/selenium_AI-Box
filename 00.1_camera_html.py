from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

import time
import unittest
import HtmlTestRunner
import os

try:
    os.makedirs('D:\Auto_test')
    print('Auto테스트 파일이 생성되었습니다.')
except FileExistsError as a:
    print(a)


class AIBoxTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        options = Options()
        options.add_experimental_option("detach", True)
        service = Service(executable_path=ChromeDriverManager().install())
        cls.driver = webdriver.Chrome(service=service, options=options)
        cls.driver.implicitly_wait(3)
        cls.driver.maximize_window()
       
        cls.driver.get('http://172.16.6.230/web/#/web/auth')
        action = ActionChains(cls.driver)
        cls.driver.find_element(By.CLASS_NAME, 'mat-form-field-infix')
        (action.send_keys('admin').key_down(Keys.TAB).send_keys('Pass0001!').pause(1).key_down(Keys.ENTER).perform())
        time.sleep(3)
   
    def test_cam_del(self):
        driver =self.driver
        driver.get('http://172.16.6.230/web/#/web/camera-setting')
    
        for i in range(1, 5):
            ch_xpath = f"/html/body/app-root/app-sidenav-responsive/div/mat-sidenav-container/mat-sidenav-content/app-camera-setting/div/mat-card/form/mat-table/mat-row[{2*i-1}]/mat-cell[1]/button"
            driver.find_element(By.XPATH, ch_xpath).click()
            # print(f'Ch{i} delete')

        driver.find_element(By.CSS_SELECTOR, \
           'body > app-root > app-sidenav-responsive > div > mat-sidenav-container > mat-sidenav-content > app-camera-setting > div > mat-card > form > div > app-btn-apply > button'\
               ).click()
        print('All Ch delete complete!\n------------------------------------------------------------')
        time.sleep(5)
    
    def test_cam_reg(self):
        driver = self.driver
        action = ActionChains(driver)
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
        
        
        
    @classmethod
    def tearDownClass(cls):
        pass
        # cls.driver.close()
        # cls.driver.quit()
        # print('test complete')
        
if __name__ == '__main__':
    runner = HtmlTestRunner.HTMLTestRunner(output='report')
    suite = unittest.TestLoader().loadTestsFromTestCase(AIBoxTest)
    runner.run(suite)
