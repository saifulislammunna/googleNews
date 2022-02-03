import time

from selenium import webdriver
# from SampleProjects.POMProjectDemo.Pages.homePage import HomePage
import unittest

from selenium.webdriver.common.by import By


class BasePage(object):

       @classmethod
       def setUpClass(cls):
           cls.driver = webdriver.Chrome(executable_path="E:\selenium-chrome-driver\chromedriver")
           cls.driver.maximize_window()


       def __init__(self):
            self.driver.get("https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en")
            time.sleep(2)

       # def test_0021(self):
       #     self.driver.find_element(By.XPATH,
       #                              "//*[@id='gb']/div[2]/div[2]/div/form/div[1]/div/div/div/div/div[1]/input[2]").click()
       #     time.sleep(2)

       # @classmethod
       # def tearDownClass(cls):
       #       cls.driver.quit()