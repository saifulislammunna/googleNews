from SampleProjects.POMProjectDemo.Locators.locator import *
from SampleProjects.POMProjectDemo.Tests.TC_001 import BasePage

class ShareLink(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.locator = Locators
    def share_link(self):
        share = self.driver.find_element(*self.locator.share_link)
        return share
