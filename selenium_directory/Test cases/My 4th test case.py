# import time
#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
#
#
# serv_obj = Service()
# driver = webdriver.Chrome(service=serv_obj)
# driver.implicitly_wait(10)
# driver.get("https://admin:123@the-internet.herokuapp.com/basic_auth")
# driver.maximize_window()
# time.sleep(5)
# # driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']").click()
# # time.sleep(5)
#
# # alertwindow= driver.switch_to.alert
# # print(alertwindow.text)
# # time.sleep(5)
# # alertwindow.send_keys("Welcome to Safe City")
# # # alertwindow.accept()
# # alertwindow.dismiss()
# # time.sleep(5)
# # driver.find_element()
#


# driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Confirm']").click()
#
# driver.switch_to.alert.accept()
#
# time.sleep(5)

from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.common.by import By


def test_click_and_hold(driver):
    driver.get('https://selenium.dev/selenium/web/mouse_interaction.html')

    clickable = driver.find_element(By.ID, "clickable")
    ActionChains(driver)\
        .click_and_hold(clickable)\
        .perform()

    sleep(0.5)
    assert driver.find_element(By.ID, "click-status").text == "focused"

