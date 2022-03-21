from selenium import webdriver
from selenium.webdriver.common.by import By
import time

google_forms_link = "https://docs.google.com/forms/d/e/1FAIpQLSdmYxZtTDSVa5a9w2cJ5pALwsAIc_XmOsrfKgmoeYMEwjXuvw/viewform?usp=sf_link"
zillow_link = "https://www.zillow.com/homes/Austin,-Texas_rb/"
chrome_driver_path = "C:/Users/robertp/Development/chromedriver.exe"


class ZillowManager:
    def __init__(self):
        self.driver = webdriver.Chrome(chrome_driver_path)
        self.driver.get(zillow_link)
        self.house_dict = {}
        self.url_array = []
        self.property_price_array = []
        self.property_address_array = []

    def house_search(self):
        self.driver.find_element(By.ID, "price").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="min-500000"]/button').click()
        self.driver.find_element(By.XPATH, '//*[@id="max-700000"]/button').click()
        time.sleep(1)
        self.driver.find_element(By.ID, "beds").click()
        self.driver.find_element(By.XPATH, '//*[@id="beds-form"]/fieldset[1]/div[1]/button[2]').click()
        self.driver.find_element(By.XPATH, '//*[@id="beds-form"]/fieldset[2]/div/button[2]').click()
        self.done_button = self.driver.find_element(By.XPATH,
                                                    '//*[@id="search-page-react-content"]/section/div[2]/div/div[3]/div/div/div/button').click()

    def data_scraper(self):
        time.sleep(3)
        self.property_prices = self.driver.find_elements(By.CLASS_NAME, "list-card-price")
        self.property_url = self.driver.find_elements(By.CSS_SELECTOR, 'a[class="list-card-link list-card-link-top-margin list-card-img"]')
        self.property_addresses = self.driver.find_elements(By.CSS_SELECTOR, 'address[class="list-card-addr"]')
        for url in self.property_url:
            self.url_array.append(url.get_attribute("href"))
        for prices in self.property_prices:
            self.property_price_array.append(prices.text)
        for addresses in self.property_addresses:
            self.property_address_array.append(addresses.text)
        time.sleep(3)







