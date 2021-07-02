import time

import requests
from bs4 import BeautifulSoup


def scrape(browser, planet_data):
    for i in range(1, 443):
        while True:
            time.sleep(2)
            soup = BeautifulSoup(browser.page_source, "html.parser")
            current_page_num = int(soup.find_all("input", attrs={"class", "page_num"})[0].get("value"))
            print(current_page_num)
            if current_page_num < i:
                browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
            elif current_page_num > i:
                browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[1]/a').click()
            else:
                break
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

            hyper_link_tag = li_tags[0]
            temp_list.append("https://exoplanets.nasa.gov" + hyper_link_tag.find_all("a", href=True)[0]["href"])
            planet_data.append(temp_list)

        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
        print(f"Page number {i} done")

    return planet_data


def scrape_hyperlink(hyperlink, new_planet_data):
    try:
        page = requests.get(hyperlink)
        soup = BeautifulSoup(page.content, "html.parser")
        temp_list = []

        for tr_tags in soup.find_all("tr", attrs={"class": "fact_row"}):
            td_tags = tr_tags.find_all("td")

            for td_tag in td_tags:
                try:
                    temp_list.append(td_tag.find_all("div", attrs={"class", "value"})[0].contents[0])
                except:
                    temp_list.append("")

        new_planet_data.append(temp_list)
    except:
        time.sleep(1)
        scrape_hyperlink(hyperlink, new_planet_data)

    return new_planet_data
