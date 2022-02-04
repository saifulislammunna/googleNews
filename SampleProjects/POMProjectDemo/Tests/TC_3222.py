import time

from selenium import webdriver
from selenium.webdriver import ActionChains

import unittest

from selenium.webdriver.common.by import By

from SampleProjects.POMProjectDemo.Pages.shareFacebook import ShareFacebook




class ShareFacebookTest(unittest.TestCase):

       @classmethod
       def setUpClass(cls):
           cls.driver = webdriver.Chrome(executable_path="E:\selenium-chrome-driver\chromedriver")
           cls.driver.maximize_window()


       def test_001(self):
           self.driver.get("https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en")
           time.sleep(3)

       def test_3222(self):
           achains = ActionChains(self.driver)
           morebutton = ShareFacebook(self.driver).news_title()
           achains.move_to_element(morebutton).perform()
           time.sleep(3)
           shareicon = ShareFacebook(self.driver).share_facebook()
           shareicon.click()
           time.sleep(5)
           clickicon = ShareFacebook(self.driver)
           clickicon.icon_facebook().click()
           time.sleep(3)