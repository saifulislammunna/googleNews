
import time

from selenium import webdriver
# from SampleProjects.POMProjectDemo.Pages.homePage import HomePage
import unittest
from SampleProjects.POMProjectDemo.Pages.narrowSearch import NarrowSearch


class NarrowTest(unittest.TestCase):

       @classmethod
       def setUpClass(cls):
           cls.driver = webdriver.Chrome(executable_path="E:\selenium-chrome-driver\chromedriver")
           cls.driver.maximize_window()


       def test_001(self):
           self.driver.get("https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en")
           time.sleep(2)

       def test_0023(self):
           confined = NarrowSearch(self.driver)
           confined.narrow_search().click()