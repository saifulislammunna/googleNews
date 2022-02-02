import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="E:\selenium-chrome-driver\chromedriver")


driver.maximize_window()
driver.get("https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en")

time.sleep(2)

driver.quit()