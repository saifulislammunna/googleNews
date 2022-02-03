from SampleProjects.POMProjectDemo.Locators.locator import *
from SampleProjects.POMProjectDemo.Tests.TC_001 import BasePage

class SaveLater(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.locator = Locators

    def save_later(self):
         save = self.driver.find_element(*self.locator.save_later)
         return save