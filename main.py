PROMISED_DOWN = 150
PROMISED_UP = 10
EDGE_DRIVER_PATH = "C:\webdrivers\msedgedriver.exe"

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



# edge_options.add_argument("--disable-notifications")

# edge_options.page_load_strategy = 'eager'

class InternetSpeedTwitterBot:
  
  def __init__(self):

    self.edge_options = webdriver.EdgeOptions()
    self.edge_options.add_experimental_option("detach", True)
    self.edge_options.add_experimental_option("prefs", {
    "profile.default_content_setting_values.geolocation": 1,  # Allow location
    # "profile.default_content_setting_values.notifications": 1  # Allow notifications
    })
    self.service = Service("C:\webdrivers\msedgedriver.exe")
    self.driver = webdriver.Edge(options=self.edge_options, service=self.service)

  def get_internet_speed(self):
    self.driver.get("https://www.speedtest.net/")
    self.driver.find_element(By.XPATH, value="/html/body/div[5]/div[2]/div/div/div[2]/div/div/button[2]").click() 
    time.sleep()
    self.driver.find_element(By.XPATH, value="/html/body/div[3]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[1]/a").click()
    download = self.driver.find_element(By.XPATH, value="/html/body/div[3]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span").text
    upload = self.driver.find_element(By.XPATH, value="/html/body/div[3]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span").text
    print(download, upload)
    pass

  def get_internet_speed_(self):
    self.driver.get("https://www.speedtest.net/")
    allow = self.driver.find_element(By.XPATH, value="/html/body/div[5]/div[2]/div/div/div[2]/div/div/button[2]").click() 
    time.sleep(3)
    go = self.driver.find_element(By.XPATH, value="/html/body/div[3]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[1]/a").click()
    # x = self.driver.find_element(By.XPATH, value="/html/body/div[3]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/a").click()
    time.sleep(15)
    # x = self.driver.find_element(By.XPATH, value="/html/body/div[3]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/div/div[2]/a").click()
    x_ = self.driver.switch_to.active_element.find_element(By.XPATH, value="/html/body/div[3]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/div/div[2]/a").click()

    # x_ = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[3]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/a'))).click()
   
    download = self.driver.find_element(By.XPATH, value="/html/body/div[3]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span").text
    upload = self.driver.find_element(By.XPATH, value="/html/body/div[3]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span").text


  def tweet_at_provider(self):  

    pass



bot = InternetSpeedTwitterBot()
bot.get_internet_speed_()
time.sleep(5)