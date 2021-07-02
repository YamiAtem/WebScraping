import csv
import time

from selenium import webdriver

import tts
from scrape import scrape, scrape_hyperlink
from data_cleaning import data_cleaning

url = "https://exoplanets.nasa.gov/exoplanet-catalog/"
browser = webdriver.Chrome("chromedriver.exe")

tts.speak("Getting URL...", print_text=True)
browser.get(url)
tts.speak("Done Getting URL!", print_text=True)

tts.speak("Waiting for 10 seconds...", print_text=True)
time.sleep(10)
tts.speak("Done Waiting!", print_text=True)

headings = ["Name", "Light Years from Earth", "Planet Mass", "Stellar Magnitude", "Discovery Date", "Hyperlink",
            "Planet Type", "Planet Radius", "Orbital Radius", "Orbital Period", "Eccentricity"]
planet_data = []
new_planet_data = []

prompt = input("Do you want to scrape? Y/N: ")

if prompt.lower() == "y" or prompt.lower() == "yes":
    tts.speak("Scraping...", print_text=True)
    planet_data = scrape(browser, planet_data)
    tts.speak("Done Scraping!", print_text=True)

    for index, data in enumerate(planet_data):
        new_planet_data = scrape_hyperlink(data[5], new_planet_data)
        print(f"{index + 1} page done 2")

    final_planet_data = []
    for index, data in enumerate(planet_data):
        new_planet_data_element = new_planet_data[index]
        new_planet_data_element = [elem.replace("\n", "") for elem in new_planet_data_element]
        new_planet_data_element = new_planet_data_element[:7]
        final_planet_data.append(data + new_planet_data_element)

    print("\nCreating CSV...")
    with open("data.csv", "w") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(headings)
        csv_writer.writerows(final_planet_data)

    print("Done creating CSV!")
elif prompt.lower() == "n" or prompt.lower() == "no":
    prompt = input("Ok, do you want to clean data Y/N: ")


if prompt.lower() == "y" or prompt.lower() == "yes":
    tts.speak("Ok, Cleaning data", print_text=True)
    data_cleaning("final.csv", "main.csv")
    tts.speak("Done Cleaning data", print_text=True)
elif prompt.lower() == "n" or prompt.lower() == "no":
    pass
