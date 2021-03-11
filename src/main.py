# The Facebook Online Friend Tracker
# Author: Baraa Hamodi

import csv
import getpass
import os
import time
import json

from datetime import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

SLEEP = 10  # in seconds
IMPLICIT_WAIT = 20  # in seconds

# Enable tab completion for raw input.
try:
  import readline
  readline.parse_and_bind('tab: complete')
except ImportError:
  pass

# Support both Python 2.x and 3.x user input functions.
try:
  input = raw_input
except NameError:
  pass

def main():
  # load config
  config = json.load(open('./config.json'))
  print(config)
  # Prompt user for Facebook credentials.
  print('\nFacebook Online Friend Tracker starting...')
  facebook_username = input('Facebook username: ')
  facebook_password = getpass.getpass('Facebook password: ')

  interval_time = config['interval_time']
  print(f"interval_time {interval_time} minutes")
  interval_time = interval_time * 60

  # Prompt for the CSV file path and verify that the CSV file exists before scraping.
  path_to_csv_file = config['path_to_csv_file']
  print('Verifying that the CSV file exists...')
  if os.path.exists(path_to_csv_file):
    print(path_to_csv_file + ' has been found.')
  else:
    raise Exception(f'Cannot find csv file at {path_to_csv_file}')

  # Initialize Chrome WebDriver.
  print('\nInitializing Chrome WebDriver...')
  driver = webdriver.Chrome()

  # Change default timeout and window size.
  driver.implicitly_wait(IMPLICIT_WAIT)
  driver.set_window_size(700, 500)

  # Go to www.facebook.com and log in using the provided credentials.
  print('Logging into Facebook...')
  driver.get('https://www.facebook.com/')
  emailBox = driver.find_element_by_id('email')
  emailBox.send_keys(facebook_username)
  passwordBox = driver.find_element_by_id('pass')
  passwordBox.send_keys(facebook_password)

  wait = WebDriverWait(driver, 10)
  wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Accept All']"))).click()
  wait1 = WebDriverWait(driver, 10)
  wait1.until(EC.element_to_be_clickable((By.XPATH, "//button"))).click()

  while True:
    # Wait for Facebook to update the number of online friends.
    print(f'\nat astart of iteration, sleeping {SLEEP} seconds')
    time.sleep(SLEEP)

    # Scrape if online
    found_online = 0
    print('checking if online')
    try:
      is_online = driver.find_element_by_xpath("// *[text() = 'Lucjan Dybczak'] /../../../../../../ div / div / div / div / div / span")
      print('checked')
      if is_online:
        is_online = 1
        found_online = 1
    except:
      is_online = 0
    print('Done! Detected ' + str(is_online))

    # Get current time.
    today = datetime.now().strftime('%Y/%m/%d %H:%M:%S')

    # Append row to the CSV file.
    with open(path_to_csv_file, 'a') as f:
      writer = csv.writer(f, lineterminator='\n')
      writer.writerow([today, is_online])
      print('Added: ' + today + ' -> ' + str(is_online) + ' to the spreadsheet.')

    # Wait for next interval and increment iteration counter.
    time.sleep(interval_time - SLEEP - (1-found_online)*IMPLICIT_WAIT)
