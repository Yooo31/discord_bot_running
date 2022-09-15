from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

shop_list = ['hetm', 'amazon', 'darty']
global final_result
final_result = []

def open_shop(shop=""):
  print('start open_shop')

  driver.get("https://fr.igraal.com/codes-promo/" + shop) # Go to the url of the shop
  time.sleep(20)

def accept_cookies():
  print('start cookies')

  cookie_button = driver.find_element(By.ID, 'cookies-banner-btn-accept') # Find the button to accept cookies
  cookie_button.click()

def has_cashback() :
  print('start as cash_back')

  try:
    card = driver.find_element(By.XPATH, '//div[@data-ig-cashback-block]') # Find the card that contains the cashback

    if card:
      get_cashback()

  except:
    no_cashback()

def get_cashback():
  print('Cash back existant !')
  time.sleep(4)
  cash_back_value = driver.find_element(By.CLASS_NAME, "cashback_rate").text # Find the card that contains the cashback
  existing_cashback(cash_back_value)

def existing_cashback(cash_back_value):
  print(cash_back_value)
  driver.close() # Close the browser
  final_result.append(cash_back_value + ' / ')

def no_cashback():
  print('Non')
  driver.close() # Close the browser
  final_result.append('pas de cashback / ')

def start(shop) :
  chrome_options = Options()

  # Options to run without interface

  # chrome_options.add_argument("--no-sandbox")
  # chrome_options.add_argument("--headless")

  # Bypass the anti bot

  chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
  chrome_options.add_experimental_option('useAutomationExtension', False)
  chrome_options.add_argument("--disable-blink-features=AutomationControlled")

  # Create the driver

  global driver
  driver = webdriver.Chrome(executable_path="./chromedriver", options=chrome_options)

  # Launch the process

  open_shop(shop)
  accept_cookies()
  has_cashback()

def index():
  for actual_shop in shop_list:
    print('Check for ' + actual_shop)
    final_result.append(actual_shop + ' = ')
    start(actual_shop)

  answer_to_send = ''.join(str(x) for x in final_result)
  return(answer_to_send)