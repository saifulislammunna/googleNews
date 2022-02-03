import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from SampleProjects.POMProjectDemo.Pages.homePage import HomePage
import unittest



from SampleProjects.POMProjectDemo.Pages.headlineFollow import HeadlineFollow
from SampleProjects.POMProjectDemo.Pages.shareLink import ShareLink
from SampleProjects.POMProjectDemo.Pages.copyLink import CopyLink
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
           time.sleep(5)

       def test_00313(self):
           copy = CopyLink(self.driver)
           copy.copy_link().click()
           time.sleep(5)

       def test_00314(self):
           self.driver.execute_script("window.open('');")
           time.sleep(5)
           self.driver.switch_to.window(self.driver.window_handles[1])
           self.driver.get("https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFZxYUdjU0FtVnVHZ0pWVXlnQVAB?ceid=US:en&oc=3")