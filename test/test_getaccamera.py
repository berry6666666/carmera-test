import pytest
from appium.webdriver.common.appiumby import AppiumBy
import time
import allure
import base64
# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder

from selenium.webdriver.common.actions.pointer_input import PointerInput
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import TimeoutException

class TestAppium:
    @allure.story("Test getac camera app")
    @allure.title("Test camera function")
    @allure.description("Take a photo and display the image file in Allure.")
    
    @allure.severity(allure.severity_level.CRITICAL)
    def test_getaccamera(self,driver):
        session_id = driver.session_id 
        # allure.dynamic.link(f"http://192.168.99.58:30002/dashboard/session/{session_id}", name="Appium Dashbaord")
        allure.dynamic.link(f"http://localhost:4723/dashboard/session/{session_id}", name="Appium Dashbaord")

        with allure.step("Take photo"):
            if WebDriverWait(driver, 5).until(EC.presence_of_element_located((AppiumBy.ID, "android:id/button1"))):
                driver.find_element(AppiumBy.ID, "android:id/button1").click()
            # driver.find_element(by=AppiumBy.ID,value="android:id/button1").click()
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((AppiumBy.ID, "com.getac.getaccamera:id/btn_take_photo"))).click()
            #driver.find_element(by=AppiumBy.ID, value='com.getac.getaccamera:id/btn_take_photo').click()
        time.sleep(5)
        # with allure.step("click WIFI button"):
        #    WebDriverWait(driver, 10).until(EC.presence_of_element_located((AppiumBy.ID, "com.example.init:id/btn_wifi"))).click()
        
        with allure.step("check file name"):
            driver.find_element(by=AppiumBy.ID, value='com.getac.getaccamera:id/preview_result').click()
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((AppiumBy.ID, "com.google.android.apps.photos:id/photos_overflow_icon"))).click()
            self.swipe_up(driver)

            #機型不同需更改位置
            # photo_path = driver.find_element(by=AppiumBy.XPATH,value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout[5]/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[4]/android.widget.LinearLayout/android.widget.TextView[2]").text
            # photo_file_name = driver.find_element(by=AppiumBy.XPATH,value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout[5]/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[3]/android.widget.LinearLayout/android.widget.TextView[1]").text
            # photo_file = base64.b64decode(driver.pull_file(photo_path+'/'+photo_file_name))

            #更後
            photo_path_name = driver.find_element(by=AppiumBy.XPATH,value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout[5]/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.widget.FrameLayout[4]/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[3]/android.widget.LinearLayout/android.widget.TextView[1]").text
            photo_file = base64.b64decode(driver.pull_file(photo_path_name))
        
        with allure.step("getac photo"):
            allure.attach(photo_file,
            #更前
            # name = photo_path,
            # attachment_type=allure.attachment_type.JPG)

            #更後
            name = photo_path_name,
            attachment_type=allure.attachment_type.JPG)

        with allure.step("swipe_down"):
            actions = ActionChains(driver)
            actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to_location(200, 161)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.move_to_location(193, 788)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
            time.sleep(1)



    def swipe_up(self,driver):
        size = driver.get_window_size()
        start_x = size['width'] // 2
        start_y = size['height'] // 2
        end_x = start_x
        end_y = int(size['height'] * 0.1)
        duration = 2  #800

        #原始
        # action = TouchAction(driver)
        # action.press(x=start_x, y=start_y).wait(duration).move_to(x=end_x, y=end_y).release().perform()

        #更版
        actions = ActionChains(driver)
        actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(x=start_x, y=start_y).pointer_down().pause(duration).move_to_location(x=end_x, y=end_y).release()
        actions.perform()


        # 檢查是否成功上滑
        try:
            WebDriverWait(driver, 10).until(                     
                # EC.presence_of_element_located((MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout[5]/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[4]/android.widget.LinearLayout/android.widget.TextView[2]')))
                EC.presence_of_element_located((MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout[5]/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.widget.FrameLayout[4]/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[3]/android.widget.LinearLayout/android.widget.TextView[1]')))
        except TimeoutException:
            pytest.fail("Failed to swipe up.")
 

        '''  
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(801, 701)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(806, 161)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
        time.sleep(1)
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(750, 691)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(755, 141)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
        time.sleep(1)

      
        el = self.driver.find_element(by=AppiumBy.XPATH, value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button[2]')
        el.click()
        time.sleep(3)
        screen_size = self.driver.get_window_size()
        print(screen_size['width'],screen_size['height'])
        # 創建五個 TouchAction 對象
        action1 = TouchAction(self.driver).press(x=100, y=100).wait(100).release()
        action2 = TouchAction(self.driver).press(x=200, y=200).wait(100).release()
        action3 = TouchAction(self.driver).press(x=300, y=300).wait(100).release()
        action4 = TouchAction(self.driver).press(x=400, y=400).wait(100).release()
        action5 = TouchAction(self.driver).press(x=500, y=500).wait(100).release()
        ma = MultiAction(self.driver)
        ma.add(action1, action2, action3, action4, action5)
        ma.perform()
        time.sleep(2)
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(18, 18)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(1183, 18)
        actions.w3c_actions.pointer_action.move_to_location(1183, 699)
        actions.w3c_actions.pointer_action.move_to_location(23, 699)
        actions.w3c_actions.pointer_action.move_to_location(23, 20)
        actions.perform()
        time.sleep(5)
        '''


        #wifi_status = self.driver.get_network_connection()['wifi']
        #self.assertTrue(wifi_status)

        # wifi_status = self.driver.execute_script('mobile: shell', {
        # 'command': 'dumpsys wifi | grep mWifiInfo',
        # 'args': []
        # })
        # print(wifi_status.lower())
        # if "disabled" in wifi_status.lower():
        #     return False, "Wi-Fi is disabled"
        # elif "enabled" in wifi_status.lower():
        #     return True, "Wi-Fi is enabled"
        # else:
        #     return False, "Unknown Wi-Fi state"