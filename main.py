PROMISED_DOWN = 150
PROMISED_UP = 10
EDGE_DRIVER_PATH = "C:\webdrivers\msedgedriver.exe"

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
import time
# edge_options.add_argument("--disable-notifications")
# edge_options.page_load_strategy = 'eager'


class InternetSpeedTwitterBot:
  def __init__(self):
    self.edge_options = webdriver.EdgeOptions()
    self.edge_options.add_experimental_option("detach", True)
    self.edge_options.add_argument("--disable-notifications")
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
    time.sleep(30)
    try:
      wait = WebDriverWait(self.driver, 10)
      dismiss_button = wait.until(
          EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/a"))
      )
      dismiss_button.click()
      print("Modal dismissed.")
    except Exception as e:
      print(f"Failed to dismiss modal: {e}")

    
    yield self.driver.find_element(By.XPATH, value="/html/body/div[3]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span").text
    yield self.driver.find_element(By.XPATH, value="/html/body/div[3]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span").text
    # print(f'download: {x_}, upload: {y_}')
    # return download, upload

  def tweet_at_provider(self, down, up):
    self.driver.get("https://x.com/")
    time.sleep(3)
    sign_in = self.driver.find_element(By.XPATH, value="/html/body/div/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[3]/a").click()
    time.sleep(3)
    username = self.driver.find_element(By.XPATH, value="/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input").send_keys("szymonbryniak8@gmail.com")
    time.sleep(3)
    next = self.driver.find_element(By.XPATH, value="/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]").click()
    time.sleep(6)
    username_redirect = self.driver.find_element(By.TAG_NAME, value="input").send_keys("SzymonB1401")
    next = self.driver.find_element(By.XPATH, value="/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/button").click()
    time.sleep(5)
    password = self.driver.find_element(By.XPATH, value="/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input").send_keys('Password_12354!')
    time.sleep(3)
    log_in = self.driver.find_element(By.XPATH, value="/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button").click()
    time.sleep(3)
    enter_post = self.driver.find_element(By.XPATH, value="/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div").send_keys(f"download: {down}, up: {up}")
    time.sleep(2)
    post = self.driver.find_element(By.XPATH, value="/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button").click()
    time.sleep(2)
    try:
      got_it = self.driver.find_element(By.XPATH, value="/html/body/div[1]/div/div/div[1]/div[3]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div[3]/button").click()
    except:
      print('got it not found')


bot = InternetSpeedTwitterBot()
gen = bot.get_internet_speed_()
bot.tweet_at_provider(next(gen), next(gen))
time.sleep(5)
