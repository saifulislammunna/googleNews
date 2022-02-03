
import time

from selenium import webdriver
# from SampleProjects.POMProjectDemo.Pages.homePage import HomePage
import unittest
from SampleProjects.POMProjectDemo.Pages.featuredTopic import FeaturedTopic
from SampleProjects.POMProjectDemo.Pages.latestNews import LatestNews
from selenium.webdriver.common.by import By


class FeaturedTest(unittest.TestCase):

       @classmethod
       def setUpClass(cls):
           cls.driver = webdriver.Chrome(executable_path="E:\selenium-chrome-driver\chromedriver")
           cls.driver.maximize_window()


       def test_001(self):
           self.driver.get("https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en")
           time.sleep(2)

       def test_0021(self):
           # self.driver.find_element(By.XPATH,"//*[@id='gb']/div[2]/div[2]/div/form/div[1]/div/div/div/div/div[1]/input[2]").click()
           home_page = FeaturedTopic(self.driver)
           home_page.click_topic().click()
           time.sleep(2)

       def test_0022(self):
            news = LatestNews(self.driver)
            news.latest_news().click()
            time.sleep(2)

      
       # @classmethod
       # def tearDownClass(cls):
       #        cls.driver.quit()