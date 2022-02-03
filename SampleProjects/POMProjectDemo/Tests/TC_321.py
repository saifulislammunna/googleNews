import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

import unittest

from SampleProjects.POMProjectDemo.Pages.saveLater import SaveLater




class ShareTest(unittest.TestCase):

       @classmethod
       def setUpClass(cls):
           cls.driver = webdriver.Chrome(executable_path="E:\selenium-chrome-driver\chromedriver")
           cls.driver.maximize_window()


       def test_001(self):
           self.driver.get("https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en")
           time.sleep(5)

       def test_321(self):
           element_to_hover_over = SaveLater(self.driver)
           element_to_hover_over.
           # hover = ActionChains(self.driver).move_to_element(element_to_hover_over)
           # time.sleep(5)
           # hover.perform()