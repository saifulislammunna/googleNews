from selenium.webdriver.common.by import By
from SampleProjects.POMProjectDemo.Locators.locator import *
from SampleProjects.POMProjectDemo.Tests.TC_001 import BasePage

class FeaturedTopic(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.locator = Locators


    def click_topic(self):
       search = self.driver.find_element(*self.locator.featured_topic_xpath)
       return search