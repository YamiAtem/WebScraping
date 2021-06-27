import time
from scrape import scrape

from selenium import webdriver

url = "https://exoplanets.nasa.gov/exoplanet-catalog/"
browser = webdriver.Chrome("chromedriver.exe")

print("Getting URL...")
browser.get(url)
print("Done Getting URL!")

print("\nWaiting for 10 seconds...")
time.sleep(10)
print("Done Waiting!")

prompt = input("Do you want to scrape? Y/N: ")

if prompt.lower() == "y" or prompt.lower() == "yes":
    print("\nScraping...")
    scrape(browser)
    print("Done Scraping!")
elif prompt.lower() == "n" or prompt.lower() == "no":
    print("\nOk, exiting app")

print("\nExiting app")
