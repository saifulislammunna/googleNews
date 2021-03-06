from SampleProjects.POMProjectDemo.Locators.locator import *
from SampleProjects.POMProjectDemo.Tests.TC_001 import BasePage

class NarrowSearch(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.locator = Locators

    def narrow_search(self):
        narrow = self.driver.find_element(*self.locator.narrow_search)
        return narrow