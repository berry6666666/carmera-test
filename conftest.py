import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
import warnings
import time
import os
import base64
import allure
import requests

def pytest_addoption(parser):
    parser.addoption("--udid", action="store", help="UDID of the device")
    parser.addoption("--platform-version", action="store", help="Platform version of the device")


def pytest_collection_modifyitems(config, items):
    for item in items:
        # 修改测试/套件的名称
        udid = config.getoption("--udid")
        item.name = udid
        item._nodeid = udid

# options = UiAutomator2Options()
# options.platform_name= 'Android'
# options.device_name='RKCXXZ0140'
# options.app_package='com.getac.getaccamera'
# options.app_activity='com.getac.getaccamera.MainActivity'


appium_server_url = 'http://localhost:4723'
# appium_server_url ='http://192.168.99.58:30002' # for kubernetes pod nodePort

@pytest.fixture(scope="function")
def driver(request):
    udid = request.config.getoption("--udid")
    platform_version = request.config.getoption("--platform-version")
    

    warnings.simplefilter("ignore")
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=DeprecationWarning)
        capabilities = dict(
        platformName='Android',
        automationName='uiautomator2',
        platformVersion=platform_version,
        udids=udid,
        # appPackage='com.android.settings',
        # appActivity='.Settings',
        appPackage='com.getac.getaccamera',
        appActivity='com.getac.getaccamera.MainActivity',
        ensureWebviewsHavePages=True,
        nativeWebScreenshot=True, # ensures that Appium waits for a web page to load completely before interacting with it.
        newCommandTimeout=60, # sets the maximum amount of time Appium will wait for a new command from the client before terminating the session. 
        connectHardwareKeyboard=True, # enables the use of a physical keyboard for typing text inputs during test automation.
        videoResolution= "1920x1080"
        )
        driver = webdriver.Remote(appium_server_url, capabilities)
        #driver.start_recording_screen()
        # driver.start_recording_screen()


    allure.dynamic.feature(f"{driver.capabilities['deviceName']} {driver.capabilities['automationName']} on {driver.capabilities['platformName']}")

    yield driver

    session = driver.session_id

    driver.quit()

    #time.sleep(1)

    url = "http://localhost:4723/dashboard/api/sessions/" + session + "/video/download"
    # url = "http://192.168.99.58:30002/dashboard/api/sessions/" + session + "/video/download"
    response = requests.get(url)

    #video_rawdata = driver.stop_recording_screen()

    #create video file
    video_name = time.strftime("%Y_%m_%d_%H%M%S") + ".mp4"
    with open(video_name, "wb") as file:
        file.write(response.content)
    #filepath = os.path.join("/home/blocka/appium/appium-docker-android/media/",video_name+".mp4")
    #filepath = os.path.join("/test/assets/",video_name+".mp4")

    #save video to allure
    with open(video_name, "rb") as video_file:
      allure.attach(video_file.read(), name="video", attachment_type=allure.attachment_type.MP4)
    #driver.quit()

@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    if not os.path.exists("allure-results"):
        os.makedirs("allure-results")
    if not os.path.exists(os.path.join(os.getcwd(), "allure-results","environment.properties")):
        with open(os.path.join(os.getcwd(),"allure-results" ,"environment.properties"), "w") as f:
                for key, value in metadata.items():
                    f.write(f"{key}={value}\n")