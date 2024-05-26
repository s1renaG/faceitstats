from selenium import webdriver
from selenium.webdriver.safari.service import Service
from selenium.webdriver.common.by import By
import pandas as pd


class PlayerDataScraper:

    def __init__(self, url):
        self.url = url
        self.data = []

    def scrape_data(self):
        try:
            safari_service = Service('/usr/bin/safaridriver')
            driver = webdriver.Safari(service=safari_service)
            driver.get(self.url)
            stats_elements = driver.find_elements(By.CLASS_NAME, 'summaryStatBreakdown')

            if not stats_elements:
                driver.quit()
                return None

            for stats_element in stats_elements:
                sub_header = stats_element.find_element(By.CLASS_NAME, 'summaryStatBreakdownSubHeader').text
                value = stats_element.find_element(By.CLASS_NAME, 'summaryStatBreakdownDataValue').text
                description = stats_element.find_element(By.CLASS_NAME, 'summaryStatBreakdownDescription').text
                self.data.append({"sub_header": sub_header, "value": value, "description": description})

            driver.quit()
            return self.data

        except Exception as e:
            print(f'failed: {e}')
            return None

    def tidy_write_in(self):
        df = pd.DataFrame(self.data)
        with open('stats.cvs', 'a') as file:
            file.write(str(df))
        return


for _ in range(2):
    url = input('- ')
    player_scraper = PlayerDataScraper(url)
    data = player_scraper.scrape_data()
    if data is not None:
        player_scraper.tidy_write_in()
