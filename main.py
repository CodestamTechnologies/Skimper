"""This script serves as an example on how to use Python 
   & Playwright to scrape/extract data from Google Maps"""

from playwright.sync_api import sync_playwright
from dataclasses import dataclass, asdict, field
import pandas as pd
import argparse
import os

@dataclass
class Business:
    """holds business data"""

    name: str = None
    address: str = None
    website: str = None
    phone_number: str = None
    reviews_count: int = None
    reviews_average: float = None
    latitude: float = None
    longitude: float = None


@dataclass
class BusinessList:
    """holds list of Business objects,
    and save to both excel and csv
    """

    business_list: list[Business] = field(default_factory=list)

    def dataframe(self):
        """transform business_list to pandas dataframe

        Returns: pandas dataframe
        """
        return pd.json_normalize(
            (asdict(business) for business in self.business_list), sep="_"
        )

    def save_to_excel(self, filename):
        """saves pandas dataframe to excel (xlsx) file

        Args:
            filename (str): filename
        """
        file_path = f"{filename}.xlsx"
        if os.path.exists(file_path):
            existing_data = pd.read_excel(file_path)
            updated_data = pd.concat([existing_data, self.dataframe()], ignore_index=True)
            updated_data.to_excel(file_path, index=False)
        else:
            self.dataframe().to_excel(file_path, index=False)

    def save_to_csv(self, filename):
        """saves pandas dataframe to csv file

        Args:
            filename (str): filename
        """
        file_path = f"{filename}.csv"
        if os.path.exists(file_path):
            existing_data = pd.read_csv(file_path)
            updated_data = pd.concat([existing_data, self.dataframe()], ignore_index=True)
            updated_data.to_csv(file_path, index=False)
        else:
            self.dataframe().to_csv(file_path, index=False)

def extract_coordinates_from_url(url: str) -> tuple[float,float]:
    """helper function to extract coordinates from url"""
    
    coordinates = url.split('/@')[-1].split('/')[0]
    # return latitude, longitude
    return float(coordinates.split(',')[0]), float(coordinates.split(',')[1])


def main():
    with sync_playwright() as p:
        with open('cities.txt', 'r+') as f:  # Open file for reading and writing
            cities = f.readlines()  # Read all lines

            for city in cities:
                city = city 
                # If scraping is successful, remove the city from the list
                try:
                    cities.remove(city)
                except ValueError:
                    pass
                f.seek(0)  # Move cursor to the beginning of the file
                f.writelines(cities)  # Write the modified list back to the file
                print(".")
                city = city.strip()  # Strip to remove leading/trailing whitespace and newline
                print(city)
                

                browser = p.chromium.launch(headless=True)
                page = browser.new_page()

                try:
                    page.goto("https://www.google.com/maps", timeout=60000)
                    page.goto("https://www.google.com/maps", timeout=60000)
                    # wait is added for dev phase. can remove it in production
                    # page.wait_for_timeout(5000)

                    page.locator('//input[@id="searchboxinput"]').fill(search_for + city)
                    # page.wait_for_timeout(3000)

                    page.keyboard.press("Enter")
                    # page.wait_for_timeout(5000)

                    # scrolling
                    page.hover('//a[contains(@href, "https://www.google.com/maps/place")]', timeout=5000)

                    # this variable is used to detect if the bot
                    # scraped the same number of listings in the previous iteration
                    previously_counted = 0
                    while True:
                        page.mouse.wheel(0, 10000)
                        page.wait_for_timeout(3000)

                        if (
                            page.locator(
                                '//a[contains(@href, "https://www.google.com/maps/place")]'
                            ).count()
                            >= total
                        ):
                            listings = page.locator(
                                '//a[contains(@href, "https://www.google.com/maps/place")]'
                            ).all()[:total]
                            listings = [listing.locator("xpath=..") for listing in listings]
                            print(f"Total Scraped: {len(listings)}")
                            break
                        else:
                            # logic to break from loop to not run infinitely
                            # in case arrived at all available listings
                            if (
                                page.locator(
                                    '//a[contains(@href, "https://www.google.com/maps/place")]'
                                ).count()
                                == previously_counted
                            ):
                                listings = page.locator(
                                    '//a[contains(@href, "https://www.google.com/maps/place")]'
                                ).all()
                                print(f"Arrived at all available\nTotal Scraped: {len(listings)}")
                                break
                            else:
                                previously_counted = page.locator(
                                    '//a[contains(@href, "https://www.google.com/maps/place")]'
                                ).count()
                                print(
                                    f"Currently Scraped: ",
                                    page.locator(
                                        '//a[contains(@href, "https://www.google.com/maps/place")]'
                                    ).count(),
                                )

                    business_list = BusinessList()

                    # scraping
                    for listing in listings:
                        try:
                            listing.click()
                            page.wait_for_timeout(5000)
                            
                            
                            name_xpath = '//*[@id="QA0Szd"]/div/div/div[1]/div[3]/div/div[1]/div/div/div[2]/div[2]/div/div[1]/div[1]'
                            address_xpath = '//*[@id="QA0Szd"]/div/div/div[1]/div[3]/div/div[1]/div/div/div[2]/div[7]/div[3]/button/div/div[2]/div[1]'
                            website_xpath = '//*[@id="QA0Szd"]/div/div/div[1]/div[3]/div/div[1]/div/div/div[2]/div[7]/div[5]/a/div/div[2]/div[1]'
                            phone_number_xpath = '//*[@id="QA0Szd"]/div/div/div[1]/div[3]/div/div[1]/div/div/div[2]/div[7]/div[7]/button/div'

                            business = Business()

                            if listing.locator(name_xpath).count() > 0:
                                business.name = listing.locator(name_xpath).all()[0].inner_text()
                            else:
                                business.name = ""
                            if page.locator(address_xpath).count() > 0:
                                business.address = page.locator(address_xpath).all()[0].inner_text()
                            else:
                                business.address = ""
                            if page.locator(website_xpath).count() > 0:
                                business.website = page.locator(website_xpath).all()[0].inner_text()
                            else:
                                business.website = ""
                            if page.locator(phone_number_xpath).count() > 0:
                                business.phone_number = page.locator(phone_number_xpath).all()[0].inner_text()
                            else:
                                business.phone_number = ""
                            
                            business.latitude, business.longitude = extract_coordinates_from_url(page.url)

                            business_list.business_list.append(business)
                        except Exception as e:
                            print(e)
                    # saving to both excel and csv just to showcase the features.
                    business_list.save_to_excel("google_maps_data")
                    business_list.save_to_csv("google_maps_data")

                except TimeoutError:
                    print(f"Timeout error occurred for {city}. Skipping...")
                    # If timeout occurs, append the city to the end of the file
                    browser.close()
                    continue

                browser.close()
                if 'str' in city:
                    break



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--search", type=str)
    parser.add_argument("-t", "--total", type=int)
    args = parser.parse_args()

    if args.search:
        search_for = args.search
    else:
        # in case no arguments passed
        # the scraper will search by defaut for:
        search_for = "Garage"


    # total number of products to scrape. Default is 5000
    if args.total:
        total = args.total
    else:
        total = 1000

    while True:
        try:
            main()
        except:
            pass
