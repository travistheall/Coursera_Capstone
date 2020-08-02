from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import pandas as pd

driver = webdriver.Chrome(executable_path='chromedriver.exe')
actions = ActionChains(driver)
driver.get("https://www.zillow.com/homes/baton-rouge_rb/")

pricelist = []
addrlist = []
detailslist = []

for x in range(20):
    elems = ['list-card-price',
             'list-card-addr',
             'list-card-details',
             'next']
    for elenNum, elem in enumerate(elems):
        found = None
        while not found:
            try:
                found = driver.find_elements_by_class_name(elem)
                for foundElem in found:
                    print(foundElem.text)
                print(elem, " is on the page")
            except NoSuchElementException:
                print(elem, " is not on the page")
                sleep(3)
                print('slept lets go again')
        print("Every house from", elem, "is on the page")
        stale = None
        while not stale:
            try:
                stale = driver.find_elements_by_class_name(elem)
                for staleElem in stale:
                    print(staleElem.text)
                print(elem, " is not stale")
            except StaleElementReferenceException:
                print(elem, "is stale")
                sleep(3)
                print('slept lets go again')

        print("Every house from", elem, "is not stale")
        for house in driver.find_elements_by_class_name(elem):
            if elenNum == 0:
                if house.count('Est. ') > 0:
                    house = house[len('Est. '):]
                pricelist.append(house.text)
            elif elenNum == 1:
                addrlist.append(house.text)
            elif elenNum == 2:
                detailslist.append(house.text)
            else:
                next = driver.find_element_by_class_name(elem)
                ActionChains(driver).move_to_element(next).perform()
                next.click()
                sleep(5)

from geopy.geocoders import Nominatim
import numpy as np

latlist = []
longlist = []
geolocator = Nominatim(user_agent="IBM_Explorer")
for addr in addrlist:
    try:
        location = geolocator.geocode(addr)
        latlist.append(location.latitude)
        longlist.append(location.longitude)
    except AttributeError:
        latlist.append(np.NAN)
        longlist.append(np.NAN)

forsale = pd.DataFrame(data={'Price': pricelist,
                             'Address': addrlist,
                             'Details': detailslist,
                             'Latitude': latlist,
                             "Longitude": longlist
                             })
forsale.to_excel(excel_writer='forsale.xlsx')
