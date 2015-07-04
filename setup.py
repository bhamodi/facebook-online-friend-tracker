from setuptools import setup, find_packages

setup(
  name='facebook-online-friend-tracker',
  version='1.0.3',
  description='This tool tracks the number of online friends a user has on Facebook at a given time.',
  author='Baraa Hamodi',
  author_email='bhamodi@uwaterloo.ca',
  url='https://github.com/bhamodi/facebook-online-friend-tracker',
  license='MIT',
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
  ],
  include_package_data=True,
  packages=find_packages(),
  install_requires=[
    'selenium>=2.46.0',
    'openpyxl>=2.2.5',
  ],
  entry_points={
    'console_scripts': [
      'facebook-online-friend-tracker=src:main',
    ],
  },
)
