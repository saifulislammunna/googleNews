from SampleProjects.POMProjectDemo.Locators.locator import *
from SampleProjects.POMProjectDemo.Tests.TC_001 import BasePage

class ShareFacebook(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.locator = Locators
    def news_title(self):
        newstitle = self.driver.find_element(*self.locator.news_title)
        return newstitle
    def share_facebook(self):
         sharefacebook = self.driver.find_element(*self.locator.share_icon)
         return sharefacebook
    def icon_facebook(self):
        iconfacebook = self.driver.find_element(*self.locator.book_icon)
        return iconfacebook