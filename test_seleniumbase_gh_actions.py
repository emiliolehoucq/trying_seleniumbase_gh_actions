import logging
from seleniumbase import Driver
from selenium.webdriver.common.by import By
import time

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

driver = Driver(uc=True, headless=True) # https://chatgpt.com/share/671910a0-68a4-8004-937f-2b5d74be0f6d

driver.get("https://www.higheredjobs.com/faculty/search.cfm?JobCat=62")

time.sleep(5)

logging.info(driver.page_source)

# get all the links
links = driver.find_elements(By.TAG_NAME, "a")
urls = [link.get_attribute("href") for link in links]
# filter URLs to those that have "details.cfm?JobCode=" in them
urls = [url for url in urls if url and "details.cfm?JobCode=" in url]
logging.info(f"Number of URLs found: {len(urls)}")
logging.info(f"First 5 URLs: {urls[:5]}")
# this seems to get all the URLs across all pages--not just the first page

url_job = urls[5]
driver.get(url_job)

time.sleep(5)

logging.info(driver.page_source)

logging.info("Done")