from SampleProjects.POMProjectDemo.Locators.locator import *
from SampleProjects.POMProjectDemo.Tests.TC_001 import BasePage

class CelciusClick(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.locator = Locators

    def celcius_click(self):
        celcius = self.driver.find_element(*self.locator.celsius_path)
        return celcius