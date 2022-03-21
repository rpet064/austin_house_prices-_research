from zillow_manager import ZillowManager
import pandas as pd

zillow_link = "https://www.zillow.com/homes/Austin,-Texas_rb/"

def zillow_module_manager():
    zm = ZillowManager()
    zm.house_search()
    zm.data_scraper()
    house_df = pd.DataFrame({"house_prices": zm.property_price_array, "house_addresses": zm.property_address_array,
                             "house_links": zm.url_array})
    house_df.to_csv('austin_house_data.csv')

zillow_module_manager()




