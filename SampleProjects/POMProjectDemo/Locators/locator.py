from selenium.webdriver.common.by import By


class Locators():


   #search page objects
   featured_topic_xpath=(By.XPATH,"//*[@id='gb']/div[2]/div[2]/div/form/div[1]/div/div/div/div/div[1]/input[2]")
   latest_news_xpath = (By.XPATH, "// *[ @ id = 'nngdp4014']")
   narrow_search = (By.XPATH, "//*[@id='gb']/div[2]/div[2]/div/form/button[2]")
   headlines_click = (By.XPATH, "//*[@id='i45']/div[1]/h2/span/a")
   share_link = (By.XPATH, "/html/body/c-wiz[2]/div/div[2]/c-wiz/div/div[1]/div[2]/div[2]/span/div")
   copy_link = (By.XPATH, "/html/body/div[12]/div[2]/div/div/div[3]/div[2]/div[1]")
