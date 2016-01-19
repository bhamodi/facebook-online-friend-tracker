facebook-online-friend-tracker
==============================

Track the number of online friends you have on Facebook at any given time! Check out my `results and conclusions`_ after running this script for two weeks!

Prerequisites
-------------

All you need to use this script is a Facebook account and a `CSV`_ file.

Dependencies
------------

This script is built in `Python`_. It uses `Selenium`_ and `Chromedriver`_ to scrape the number of online friends you have on Facebook.

How to Setup
------------

1. Have `Python`_ installed.
2. Install the script and all dependencies via `pip`_ by simply running: ``pip install facebook-online-friend-tracker``
3. The command to run the script is: ``facebook-online-friend-tracker``
4. After some time, you will be able to analyze the trend in the collected data. (I waited 2 full weeks before analyzing the data and finding the `best time to post on Facebook`_.)

.. _results and conclusions: https://blog.optimizely.com/2015/07/08/how-to-find-the-best-time-to-post-on-facebook/
.. _CSV: https://en.wikipedia.org/wiki/Comma-separated_values
.. _Python: https://www.python.org/
.. _Selenium: https://pypi.python.org/pypi/selenium
.. _Chromedriver: https://pypi.python.org/pypi/chromedriver_installer
.. _pip: https://pypi.python.org/pypi/facebook-online-friend-tracker
.. _best time to post on Facebook: https://blog.optimizely.com/2015/07/08/how-to-find-the-best-time-to-post-on-facebook/
