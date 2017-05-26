# -*- coding: utf-8 -*-
from selenium import selenium
import unittest, time, re

class remotetestscript(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("52.170.81.120", 4444, "*chrome", "https://mpnesp.learnondemand.net")
        self.selenium.start()
    
    def test_remotetestscript(self):
        sel = self.selenium
        sel.open("https://mpnesp.learnondemand.net/User/Login?ReturnUrl=%2f")
        sel.click("id=signInButton")
        sel.click("id=microsoftLogin")
        sel.wait_for_page_to_load("30000")
        sel.type("id=i0116", "alihhussain@hotmail.com")
        sel.click("id=idSIButton9")
        sel.type("id=i0118", "26*#adamhussain")
        sel.click("id=idSIButton9")
        sel.wait_for_page_to_load("30000")
        for i in range(60):
            try:
                if "All times shown in UTC." == sel.get_text("//div[@id='main']/div[5]"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("//a[contains(@href, '/TrainingKey/Redeem')]")
        sel.wait_for_page_to_load("30000")
        sel.type("id=TrainingKey", "7CC20587")
        sel.click("//input[@value='Redeem Training Key']")
        sel.wait_for_page_to_load("30000")
        sel.click("xpath=(//input[@value='Launch'])[12]")
        for i in range(60):
            try:
                if "Attention- When creating the extra VM after the sharepoint farm, you will get an insuffienct cores in subscription error." == sel.get_text("css=p > strong"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("xpath=(//button[@type='button'])[2]")
        sel.click("xpath=(//button[@type='button'])[3]")
        print(sel.get_text("css=span.pasteText"))
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
