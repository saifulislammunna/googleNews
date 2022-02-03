from SampleProjects.POMProjectDemo.Locators.locator import *
from SampleProjects.POMProjectDemo.Tests.TC_001 import BasePage

class LatestNews(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.locator = Locators

    def latest_news(self):
        news = self.driver.find_element(*self.locator.latest_news_xpath)
        return news
