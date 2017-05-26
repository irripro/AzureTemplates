# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Testing(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://mpnesp.learnondemand.net"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_ing(self):
        driver = self.driver
        driver.get("https://mpnesp.learnondemand.net/User/Login?ReturnUrl=%2f")
        self.assertEqual("Login - Learn On Demand LMS", driver.title)
        driver.find_element_by_id("signInButton").click()
        self.assertEqual("Sign in to your Microsoft account", driver.title)
        driver.find_element_by_id("i0116").clear()
        driver.find_element_by_id("i0116").send_keys("alihhussain@hotmail.com")
        driver.find_element_by_id("i0118").clear()
        driver.find_element_by_id("i0118").send_keys("26*#adamhussain")
        driver.find_element_by_id("idSIButton9").click()
        driver.find_element_by_id("idSIButton9").click()
        self.assertEqual("Continue", driver.title)
        self.assertEqual("Current Training Ali Hussain - Learn On Demand LMS", driver.title)
    
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
