import time

from selenium import webdriver
import unittest
from SampleProjects.POMProjectDemo.Pages.headlineFollow import HeadlineFollow
from SampleProjects.POMProjectDemo.Pages.shareLink import ShareLink
from SampleProjects.POMProjectDemo.Pages.facebookLink import FacebookLink
class ShareTest(unittest.TestCase):

           @classmethod
           def setUpClass(cls):
               cls.driver = webdriver.Chrome(executable_path="E:\selenium-chrome-driver\chromedriver")
               cls.driver.maximize_window()

           def test_001(self):
               self.driver.get("https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en")
               time.sleep(5)

           def test_003(self):
               headline = HeadlineFollow(self.driver)
               headline.headline_follow().click()
               time.sleep(5)

           def test_00312(self):
               share = ShareLink(self.driver)
               share.share_link().click()
               time.sleep(7)
           def test_003122(self):
               facebook = FacebookLink(self.driver)
               facebook.facebook_link().click()
               time.sleep(5)