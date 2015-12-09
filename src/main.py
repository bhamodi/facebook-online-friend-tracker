# The Facebook Online Friend Tracker
# Author: Baraa Hamodi

import argparse
import csv
import os
import time

from datetime import datetime
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

def main():
  print('\nStarting script...')
  parser = argparse.ArgumentParser()
  parser.add_argument('--user', dest='facebook_username', required=True, help='the email that you login to facebook with')
  parser.add_argument('--pass', dest='facebook_password', required=True, help='the password that you login to facebook with')
  parser.add_argument('--path', dest='path_to_csv_file', required=True, help='the path to the csv file')

  args = parser.parse_args()
  facebook_username = args.facebook_username
  facebook_password = args.facebook_password
  path_to_csv_file = args.path_to_csv_file

  # Verify that the CSV file exists before scraping
  print('Verifying that the CSV file exists...')
  if os.path.exists(path_to_csv_file):
    print(path_to_csv_file + ' has been found.')
  else:
    print('[WARNING] ' + path_to_csv_file + ' does not exist. Creating a new CSV file now...')
    path_to_csv_file = os.path.join(os.getcwd(), 'facebook_online_friend_tracker_data.csv')
    with open(path_to_csv_file, 'w') as f:
      writer = csv.writer(f, lineterminator='\n')
      writer.writerow(['Timestamp', 'Number of Online Friends'])
      print('New CSV file created at: ' + path_to_csv_file)

  # Initialize Chrome WebDriver
  print('\nInitializing Chrome WebDriver...')
  driver = webdriver.Chrome()

  # Change default timeout and window size
  driver.implicitly_wait(120)
  driver.set_window_size(700, 700)

  # Go to www.facebook.com and log in using the provided credentials
  print('Logging into Facebook...')
  driver.get('https://www.facebook.com/')
  emailBox = driver.find_element_by_id('email')
  emailBox.send_keys(facebook_username)
  passwordBox = driver.find_element_by_id('pass')
  passwordBox.send_keys(facebook_password)
  driver.find_element_by_id('loginbutton').click()

  # Wait for Facebook to update the number of friends dynamically via an ajax call
  print('Waiting for Facebook to update friends list... (This takes approximately 2 minutes.)')
  script = '''var open = window.XMLHttpRequest.prototype.open;
              function openReplacement(method, url, async, user, password) {
                var syncMode = async !== false ? 'async' : 'sync';
                if (url === '/ajax/chat/buddy_list.php') {
                  var done = document.createElement('div');
                  done.id = 'doneScraping';
                  document.body.appendChild(done);
                }
                return open.apply(this, arguments);
              }
              window.XMLHttpRequest.prototype.open = openReplacement;'''
  driver.execute_script(script)
  try:
    doneScraping = driver.find_element_by_id('doneScraping')
    time.sleep(5)
  except NoSuchElementException:
    pass

  # Scrape the number of online friends
  onlineFriendsCount = driver.find_element_by_xpath('//*[@id="fbDockChatBuddylistNub"]/a/span[2]/span').text.strip('()')
  if onlineFriendsCount:
    onlineFriendsCount = int(onlineFriendsCount)
  else:
    onlineFriendsCount = 0
  print('\nDone! Detected ' + str(onlineFriendsCount) + ' online friends.')

  # Close Chrome WebDriver
  driver.close()

  # Get current time
  today = datetime.now().strftime('%Y/%m/%d %H:%M:%S')

  # Append row to the CSV file
  with open(path_to_csv_file, 'a') as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow([today, onlineFriendsCount])
    print('Added: ' + today + ' -> ' + str(onlineFriendsCount) + ' to the spreadsheet.')
