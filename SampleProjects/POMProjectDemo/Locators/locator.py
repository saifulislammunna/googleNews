from selenium.webdriver.common.by import By


class Locators():


   #search page objects
   featured_topic_xpath=(By.XPATH,"//*[@id='gb']/div[2]/div[2]/div/form/div[1]/div/div/div/div/div[1]/input[2]")
   latest_news_xpath = (By.XPATH, "// *[ @ id = 'nngdp4014']")
   narrow_search = (By.XPATH, "//*[@id='gb']/div[2]/div[2]/div/form/button[2]")
   headlines_click = (By.XPATH, "//*[@id='i45']/div[1]/h2/span/a")
   # // *[ @ id = 'nngdp144'] / div / div / div / div[2]