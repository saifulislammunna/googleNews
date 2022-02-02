
import time

from selenium import webdriver
# from SampleProjects.POMProjectDemo.Pages.homePage import HomePage
import unittest
from SampleProjects.POMProjectDemo.Pages.featuredTopic import FeaturedTopic
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
           self.featured = FeaturedTopic()
           time.sleep(5)
