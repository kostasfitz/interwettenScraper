# interwetten scraper

import time
from datetime import datetime
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

# scraper setup
driver_path = 'C:\Drivers\chromedriver_win32\chromedriver.exe'
website = 'https://www.interwetten.gr/el/%ce%b1%ce%b8%ce%bb%ce%b7%cf%84%ce%b9%ce%ba%cf%8c-%cf%83%cf%84%ce%bf%ce%af%cf%87%ce%b7%ce%bc%ce%b1/%cf%83%ce%ae%ce%bc%ce%b5%cf%81%ce%b1/15'
driver = webdriver.Chrome(driver_path)
driver.get(website)

# close popups
time.sleep(2)
cookies_button = driver.find_element(by=By.XPATH, value="//button[@class='tru_iw__btn']")
cookies_button.click()

# create dataframe
dataframe = pd.DataFrame({'Date': [],
                          'Home': [],
                          'Away': [],
                          'HomeOdds': [],
                          'AwayOdds': []})

# find available games
time.sleep(1)
table = driver.find_element(by=By.XPATH, value="//table[@id='TBL_Content_TabbedKindOfSportList']")
rows = table.find_elements(by=By.XPATH, value="//td[@class='bets']")

for row in rows:
    info = row.get_attribute('innerText')
    info.strip()
    home, home_odds, *_, away, away_odds = info.split('\n')
    date = 'N/A' # will be fixed in later version
    data = [date, home, away, home_odds, away_odds]
    dataframe.loc[len(dataframe)] = data


# export data as csv
now = datetime.now()
datetime_str = now.strftime("%d%m%Y%H%M%S")
dataframe.to_csv(datetime_str+'.csv')

driver.close()
