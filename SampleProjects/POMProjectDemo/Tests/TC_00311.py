import time

from selenium import webdriver


import unittest



from SampleProjects.POMProjectDemo.Pages.headlineFollow import HeadlineFollow
from SampleProjects.POMProjectDemo.Pages.followLink import FollowLink

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

       def test_00311(self):
           follow = FollowLink(self.driver)
           follow.follow_link().click()
           time.sleep(5)
