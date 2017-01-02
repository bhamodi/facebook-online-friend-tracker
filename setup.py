from setuptools import setup, find_packages

setup(
  name='facebook-online-friend-tracker',
  version='2.0.1',
  description='This tool tracks the number of online friends a user has on Facebook at any given time.',
  long_description=open('README.rst').read(),
  url='https://github.com/bhamodi/facebook-online-friend-tracker',
  author='Baraa Hamodi',
  author_email='bhamodi@edu.uwaterloo.ca',
  license='MIT',
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 3',
    'Topic :: Internet :: Log Analysis',
    'Topic :: Software Development',
    'Topic :: Utilities',
  ],
  keywords='facebook online friend tracker python scraper selenium analysis optimization',
  packages=find_packages(),
  install_requires=[
    'chromedriver_installer>=0.0.4',
    'selenium>=3.0.2',
  ],
  entry_points={
    'console_scripts': [
      'facebook-online-friend-tracker=src:main',
    ],
  },
)
