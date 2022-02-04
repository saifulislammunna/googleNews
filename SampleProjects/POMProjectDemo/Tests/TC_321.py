import time

from selenium import webdriver
from selenium.webdriver import ActionChains

import unittest

from selenium.webdriver.common.by import By

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

           achains = ActionChains(self.driver)
           morebutton = SaveLater(self.driver).save_later()
           achains.move_to_element(morebutton).perform()
           time.sleep(5)
           morebutton.click()
           time.sleep(5)
           # morebutton = self.driver.find_element(By.XPATH,  "//*[@id='yDmH0d']/c-wiz/div/div[2]/div[2]/div/main/c-wiz/div[1]/div[1]/div[3]/div/div/article/div/menu/div/div")
           # achains = ActionChains(self.driver)
           # achains.move_to_element(morebutton).perform()
           # time.sleep(5)
           # self.driver.find_element(By.XPATH, "//*[@id='yDmH0d']/c-wiz/div/div[2]/div[2]/div/main/c-wiz/div[1]/div[1]/div[3]/div/div/article/div/menu/div/div").click()
           # time.sleep(5)
           # actions = ActionChains(self.driver)
       #     saved = SaveLater(self.driver).save_later()
       #     actions.move_to_element(saved).perform()
           # saved.save_later().click()
           # time.sleep(5)
           # actions = ActionChains(self.driver)
           # actions.move_to_element("saved").click().perform()
           # hover = ActionChains(self.driver).move_to_element(element_to_hover_over)
           # time.sleep(5)
           # hover.perform()
