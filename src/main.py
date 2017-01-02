# The Facebook Online Friend Tracker
# Author: Baraa Hamodi

import csv
import getpass
import os
import time

from datetime import datetime
from selenium import webdriver

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
  # Prompt user for Facebook credentials.
  print('\nFacebook Online Friend Tracker starting...')
  facebook_username = input('Facebook username: ')
  facebook_password = getpass.getpass('Facebook password: ')

  # Prompt user for script interval time and convert to seconds.
  while True:
    interval_time = int(input('How often would you like to check how many friends are online? Enter a number between 5 and 30 minutes: '), 10)
    if interval_time >= 5 and interval_time <= 30:
      break
    else:
      print('The number you entered was not between 5 and 30.')
  interval_time = interval_time * 60

  # Prompt user for total run time and convert to seconds.
  while True:
    total_time = int(input('How long would you like to run this tool for? Enter a number between 1 and 720 hours: '), 10)
    if total_time >= 1 and total_time <= 720:
      break
    else:
      print('The number you entered was not between 1 and 720.')
  total_time = total_time * 3600

  # Prompt for the CSV file path and verify that the CSV file exists before scraping.
  path_to_csv_file = input('Path to the CSV file: ')
  print('Verifying that the CSV file exists...')
  if os.path.exists(path_to_csv_file):
    print(path_to_csv_file + ' has been found.')
  else:
    print('[WARNING] ' + path_to_csv_file + ' does not exist. Creating a new CSV file now...')
    path_to_csv_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'facebook_online_friend_tracker_data.csv')
    with open(path_to_csv_file, 'w') as f:
      writer = csv.writer(f, lineterminator='\n')
      writer.writerow(['Timestamp', 'Number of Online Friends'])
      print('New CSV file created at: ' + path_to_csv_file)

  # Compute total number of iterations and initialize iteration counter.
  number_of_iterations = total_time / interval_time
  iteration = 0

  # Initialize Chrome WebDriver.
  print('\nInitializing Chrome WebDriver...')
  driver = webdriver.Chrome()

  # Change default timeout and window size.
  driver.implicitly_wait(120)
  driver.set_window_size(700, 500)

  # Go to www.facebook.com and log in using the provided credentials.
  print('Logging into Facebook...')
  driver.get('https://www.facebook.com/')
  emailBox = driver.find_element_by_id('email')
  emailBox.send_keys(facebook_username)
  passwordBox = driver.find_element_by_id('pass')
  passwordBox.send_keys(facebook_password)
  driver.find_element_by_id('loginbutton').click()

  while iteration < number_of_iterations:
    # Wait for Facebook to update the number of online friends.
    print('\nWaiting for Facebook to update friends list... (This takes approximately 3 minutes.)')
    time.sleep(180)

    # Scrape the number of online friends.
    onlineFriendsCount = driver.find_element_by_xpath('//*[@id="fbDockChatBuddylistNub"]/a/span[2]/span').text.strip('()')
    if onlineFriendsCount:
      onlineFriendsCount = int(onlineFriendsCount)
    else:
      onlineFriendsCount = 0
    print('Done! Detected ' + str(onlineFriendsCount) + ' online friends.')

    # Get current time.
    today = datetime.now().strftime('%Y/%m/%d %H:%M:%S')

    # Append row to the CSV file.
    with open(path_to_csv_file, 'a') as f:
      writer = csv.writer(f, lineterminator='\n')
      writer.writerow([today, onlineFriendsCount])
      print('Added: ' + today + ' -> ' + str(onlineFriendsCount) + ' to the spreadsheet.')

    # Wait for next interval and increment iteration counter.
    time.sleep(interval_time - 180)
    iteration += 1

  # Close Chrome WebDriver.
  driver.quit()
