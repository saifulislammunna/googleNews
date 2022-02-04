import time

from selenium import webdriver
from selenium.webdriver import ActionChains

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

       # def test_321(self):
       #
       #     actions = ActionChains(self.driver)
       #     saved = SaveLater(self.driver).save_later()
       #     actions.move_to_element(saved).perform()
           # saved.save_later().click()
           # time.sleep(5)
           # actions = ActionChains(self.driver)
           # actions.move_to_element("saved").click().perform()
           # hover = ActionChains(self.driver).move_to_element(element_to_hover_over)
           # time.sleep(5)
           # hover.perform()