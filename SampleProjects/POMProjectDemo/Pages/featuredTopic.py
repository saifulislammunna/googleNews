from selenium.webdriver.common.by import By
from SampleProjects.POMProjectDemo.Locators.locator import Locators

class FeaturedTopic():

    # def __init__(self, driver):
    #     self.driver = driver
    #


    def click_topic(self):
        self.driver.find_element(By.XPATH, Locators.featured_topic_xpath).click()