# facebook-online-friend-tracker

Track the number of online friends you have on Facebook at any given time!

## Prerequisites

To be able to use this tool, you will need to point have a Facebook account, an Excel sheet (`.xlsx`), and a server (or computer) that can run a cron job / scheduled task.

## Dependencies

This tool uses [Selenium](https://pypi.python.org/pypi/selenium) to scrape the data and [Openpyxl](https://pypi.python.org/pypi/openpyxl) to store the data in an Excel sheet.

## How to Setup

1.  Run: `pip install facebook-online-friend-tracker`
2.  Setup a [cron job](http://askubuntu.com/questions/2368/how-do-i-set-up-a-cron-job) to run the tool at a certain frequency. (I used 15 minute intervals).
3.  The command to run the tool is: `facebook-online-friend-tracker --user 'example@example.com' --pass 'your_password' --path 'path/to/spreadsheet.xlsx'`
4.  After a certain amount of time, you will be able to analyze the trend in the Excel sheet you specified. (I waited 2 full weeks before analyzing the data and finding the best time to post on Facebook.)
