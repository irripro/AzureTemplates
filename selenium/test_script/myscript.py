# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Myscript(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://change-this-to-the-site-you-are-testing/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_myscript(self):
        driver = self.driver
        driver.get("https://mpnesp.learnondemand.net/User/Login?ReturnUrl=%2f")
        self.assertEqual("Login - Learn On Demand LMS", driver.title)
        driver.find_element_by_id("signInButton").click()
        driver.find_element_by_id("microsoftLogin").click()
        driver.find_element_by_id("i0116").clear()
        driver.find_element_by_id("i0116").send_keys("alihhussain@hotmail.com")
        driver.find_element_by_id("idSIButton9").click()
        driver.find_element_by_id("i0118").clear()
        driver.find_element_by_id("i0118").send_keys("26*#adamhussain")
        driver.find_element_by_id("idSIButton9").click()
        for i in range(60):
            try:
                if "All times shown in UTC." == driver.find_element_by_xpath("//div[@id='main']/div[5]").text: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_xpath("//a[contains(@href, '/TrainingKey/Redeem')]").click()
        driver.find_element_by_id("TrainingKey").clear()
        driver.find_element_by_id("TrainingKey").send_keys("7CC20587")
        driver.find_element_by_xpath("//input[@value='Redeem Training Key']").click()
        driver.find_element_by_xpath("(//input[@value='Launch'])[12]").click()
        for i in range(60):
            try:
                if "Attention- When creating the extra VM after the sharepoint farm, you will get an insuffienct cores in subscription error." == driver.find_element_by_css_selector("p > strong").text: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_xpath("(//button[@type='button'])[2]").click()
        driver.find_element_by_xpath("(//button[@type='button'])[3]").click()
         = driver.find_element_by_css_selector("span.pasteText").text
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
