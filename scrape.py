import csv

from bs4 import BeautifulSoup


def scrape(browser):
    headings = ["Name", "Light Years from Earth", "Planet Mass", "Stellar Magnitude", "Discovery Date"]
    planet_data = []

    for i in range(0, 443):
        soup = BeautifulSoup(browser.page_source, "html.parser")
        for ul_tag in soup.find_all("ul", attrs={"class", "exoplanet"}):
            li_tags = ul_tag.find_all("li")
            temp_list = []
            for index, li_tag in enumerate(li_tags):
                if index == 0:
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append("")
            planet_data.append(temp_list)

        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
        print(f"Page {i} done")

    print("\nCreating CSV...")
    with open("final.csv", "w") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(headings)
        csv_writer.writerows(planet_data)

    print("Done creating CSV!")
