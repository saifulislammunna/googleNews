from SampleProjects.POMProjectDemo.Locators.locator import *
from SampleProjects.POMProjectDemo.Tests.TC_001 import BasePage

class FollowLink(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.locator = Locators

    def follow_link(self):
        follow = headline = self.driver.find_element(*self.locator.follow_link)
        return follow