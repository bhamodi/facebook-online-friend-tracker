# The Facebook Online Friend Tracker
# Author: Baraa Hamodi

import argparse
import csv
import time

from datetime import datetime
from os.path import exists
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('--user', dest='facebook_username', required=True, help='the email that you login to Facebook with')
  parser.add_argument('--pass', dest='facebook_password', required=True, help='the password that you login to Facebook with')
  parser.add_argument('--path', dest='path_to_csv_file', required=True, help='the path to the csv file')

  args = parser.parse_args()
  facebook_username = args.facebook_username
  facebook_password = args.facebook_password
  path_to_csv_file = args.path_to_csv_file

  # Verify that the CSV file exists before scraping
  if not exists(path_to_csv_file):
    raise Exception(path_to_csv_file + ' does not exist. Please try again.')

  # Initialize Chrome WebDriver and change default timeout
  print('Initializing Chrome WebDriver...')
  driver = webdriver.Chrome()
  driver.implicitly_wait(180)

  # Go to www.facebook.com and log in using the provided credentials
  print('Logging into Facebook...')
  driver.get('https://www.facebook.com/')
  emailBox = driver.find_element_by_id('email')
  emailBox.send_keys(facebook_username)
  passwordBox = driver.find_element_by_id('pass')
  passwordBox.send_keys(facebook_password)
  passwordBox.send_keys(Keys.RETURN)

  # Wait for Facebook to update the number of friends dynamically
  print('Waiting for Facebook to update friends list... (This takes approximately 2 minutes.)')
  time.sleep(120)

  # Scrape the number of online friends
  onlineFriendsCount = int(driver.find_element_by_xpath('//*[@id="fbDockChatBuddylistNub"]/a/span[2]/span').text.strip('()'))
  print('Done! Detected ' + str(onlineFriendsCount) + ' online friends.')

  # Close Chrome WebDriver
  driver.close()

  # Get current time
  today = datetime.now().strftime('%Y/%m/%d %H:%M:%S')

  # Append row to the CSV file
  with open(path_to_csv_file, 'a') as f:
    writer = csv.writer(f)
    writer.writerow([today, onlineFriendsCount])
    print('Added: ' + today + ' -> ' + str(onlineFriendsCount) + ' to the spreadsheet.')

main()
