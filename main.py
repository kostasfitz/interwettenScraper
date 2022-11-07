# interwetten scraper


from tennis_scrape import tennis_scrape


# scraper setup
driver_path = 'C:\Drivers\chromedriver_win32\chromedriver.exe'
website = 'https://www.interwetten.gr/en/sport/leaguelist?leagueIds=408826,407726'

tennis_scrape(driver_path, website)
