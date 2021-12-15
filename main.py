# Generated by Selenium IDE
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import *

ids = ["130679","130947","130563","131044","131078","130691","131397","132198","131616","131564","131724","131933","131697","132458","132501","130947","132410","132374","132006","132283","131682","131684","131701","132166"]

for i in ids:
    driver = webdriver.Chrome("./chromedriver")
    driver.set_page_load_timeout(6000)
    driver.get("http://www.singolife.com/ProductInfoManage/PoductInfo.aspx?ProductId=840cb25f-d782-4499-a8c8-35b5204ca8df")
    driver.find_element(By.LINK_TEXT, "加入購物車").click()
    driver.switch_to.alert.accept()
    driver.find_element(By.ID, "TxtLanguage").click()
    driver.implicitly_wait(10)
    driver.find_element(By.ID, "Big5").click()
    driver.find_element(By.ID, "TxtCountry").click()
    driver.find_element(By.ID, "820f12e7-03dc-4386-ae84-b1aabd632a98").click()
    driver.find_element(By.ID, "TxtPhone").click()
    driver.find_element(By.ID, "TxtPhone").send_keys(i)
    driver.find_element(By.ID, "TxtPassWord").send_keys("123456")
    driver.find_element(By.CSS_SELECTOR, ".wait").click()
    driver.find_element(By.LINK_TEXT, "立即購買").click()
    assert driver.switch_to.alert.text == "確定立即購買？"
    driver.switch_to.alert.accept()

    msg_24g = driver.find_element_by_id("ChkAgree")
    driver.execute_script("arguments[0].click();", msg_24g)
        
    msg_25g = driver.find_element(By.CSS_SELECTOR, ".password")
    driver.execute_script("arguments[0].click();", msg_25g)
    try:
        print("try success1")
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "pass"))
        )
        element.click()
        print("try success2")
        element.send_keys("654321")
        driver.find_element(By.CSS_SELECTOR, "li:nth-child(2) > input").click()
        assert driver.switch_to.alert.text == "確定送出訂單?"
        print("try success3")
        driver.switch_to.alert.accept()
    except UnexpectedAlertPresentException:
        print("except in")
        try:
            print("UnexpectedAlertPresentException, ",alert=driver.switch_to.alert)
            if (alert.text=="當前時間段不允許購買,請晚點再來！"):
                print("沒貨了")
        except NoAlertPresentException :
            print("NoAlertPresentException")
    finally:
        print("Finally")
        time.sleep(20)
        driver.quit()