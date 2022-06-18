from selenium import webdriver
from bs4 import BeautifulSoup
import time 
import csv
from selenium.webdriver.common.by import By
#selenium is used to interact i.e. read/fetch data from a webpage
#bs4 is used for parsing things through html tags through a particular tag or id or listing all li tags in ul

START_URL = "https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"

browser = webdriver.Chrome("./chromedriver")
browser.get(START_URL)
time.sleep(10)
headers = ["name","light_years_from_earth","planet_mass","stellar_magnitude", "discovery_date"]

planet_data = []

def scrap(): 
    for i in range (0,201):


        soup = BeautifulSoup(browser.page_source, "html.parser")
        for ul_tag in soup.find_all("ul",attrs={"class":"exoplanet"}):
            li_tags = ul_tag.find_all("li")
            temp_list = []
            for index, li_tag in enumerate (li_tags):
                #enumerate helps to access the index of the element as well as the element itself
                if index == 0 :
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append("")
            planet_data.append(temp_list)
        browser.find_element(by=By.XPATH, value='//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
        #find_element(by=By.XPATH,value='//*[@id="primary_column"]/div[1]/div[2]/div[1]/div/nav/span[2]/a').click()

scrap()

with open('planet_data.csv', 'a+') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(planet_data)

