from SampleProjects.POMProjectDemo.Locators.locator import *
from SampleProjects.POMProjectDemo.Tests.TC_001 import BasePage

class FacebookLink(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.locator = Locators

    def facebook_link(self):
         facebook = self.driver.find_element(*self.locator.facebook_link)
         return facebook