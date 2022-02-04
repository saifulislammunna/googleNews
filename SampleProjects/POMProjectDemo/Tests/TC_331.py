import time

from selenium import webdriver


import unittest

from SampleProjects.POMProjectDemo.Pages.celciusClick import CelciusClick


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

       def test_331(self):
           celcius = CelciusClick(self.driver)
           celcius.celcius_click().click()
           time.sleep(5)
