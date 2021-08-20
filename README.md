# Online Bookstore Scrpaing Using Python Selenium
This source code scrapes the title and the price of a search word from an Korean online bookstore 'Aladin'(https://www.aladin.co.kr/home/welcome.aspx). The search word can be manipulated by the user.

### Chrome Version Check
 - Open Chrome
 - At the upper-right corner, click More > Help > Chrome Info

### Chromedriver Download
Download a chromedriver for your OS.
 - link : https://sites.google.com/a/chromium.org/chromedriver/downloads

### Directories
 - src: source files including,
     - config.yml : configurations setting for driver and search word
     - ConfigLoader.py : Loads config.yml
     - scraper.py : Includes class(Scraper) and creates instance variables.
     - Main.py : Creates instance 'scraper' and saves the result in dataframe.
     - run.sh : Shell script that runs Main.py