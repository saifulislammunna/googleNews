from SampleProjects.POMProjectDemo.Locators.locator import *
from SampleProjects.POMProjectDemo.Tests.TC_001 import BasePage

class CopyLink(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.locator = Locators

    def copy_link(self):
        copy = self.driver.find_element(*self.locator.copy_link)
        return copy