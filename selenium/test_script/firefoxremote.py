from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
 
# create a new Firefox session
driver = driver = webdriver.Remote(
    command_executor='http://52.170.81.120:4444/wd/hub',
    desired_capabilities=DesiredCapabilities.FIREFOX)
#driver=webdriver.Firefox()
driver.implicitly_wait(30)
 
# navigate to the application home page
driver.get("https://mpnesp.learnondemand.net/User/Login?ReturnUrl=%2f")
driver.find_element_by_id('signInButton').click()
driver.implicitly_wait(60)
driver.find_element_by_id('microsoftLogin').click()
driver.implicitly_wait(60)
driver.find_element_by_id('i0116').send_keys("alihhussain@hotmail.com")
driver.implicitly_wait(60)
driver.find_element_by_id('idSIButton9').click()
driver.implicitly_wait(60)
driver.find_element_by_id("i0118").send_keys("26*#adamhussain")
driver.implicitly_wait(60)
driver.find_element_by_id('idSIButton9').click()
driver.implicitly_wait(60)
driver.find_element_by_css_selector('a.trainingKeyRedemptionLink').click()
driver.implicitly_wait(60)
driver.find_element_by_id('TrainingKey').send_keys("7CC20587")
driver.find_element_by_xpath("//div[@id='content']/form[1]/div[2]/input[1]").click()
driver.implicitly_wait(60)
driver.find_element_by_xpath("//div[@id='main']/div[3]/div[2]/div[2]/div[3]/div[1]/div[2]/div[2]/div[1]/input[1]").click()
driver.implicitly_wait(60)
#driver.find_element_by_class_name("openInNewWindow").find_element_by_xpath("//div[@class='launchButtons'])/input[1]").click()
# close the browser window
#driver.quit()