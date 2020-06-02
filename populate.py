from selenium import webdriver
from settings import *
from selenium.common.exceptions import NoSuchElementException
import time


def populate_form():
    """ takes in an instance of the camper class which contains the relevant
     information to register a camper for the trail """
    url = 'https://canypermits.nps.gov/index.cfm'
    driver = webdriver.Chrome('./chromedriver')
    driver.get(url)

    # first page
    while driver.current_url == 'https://canypermits.nps.gov/index.cfm':
        driver.refresh()
        elem = driver.find_element_by_name("StartMonth")
        elem.send_keys(SETTINGS_MONTH)

        elem = driver.find_element_by_name("StartDay")
        elem.send_keys(SETTINGS_DAY)

        elem = driver.find_element_by_name("StartYear")
        elem.send_keys(SETTINGS_YEAR)

        submit_button = driver.find_elements_by_xpath("//input[@value='Next']")[0]
        submit_button.click()
        time.sleep(1)

    # second page
    elem = driver.find_element_by_name("DestinationID")
    elem.send_keys('Island in the Sky')

    submit_button = driver.find_elements_by_xpath("//input[@value='Next']")[0]
    submit_button.click()

    # third page
    table = driver.find_element_by_class_name("sitetable")
    rows = table.find_elements_by_tag_name("tr")
    r = 2
    while r < 23:
        try:
            found_site = False
            cells = rows[r].find_elements_by_tag_name('td')
            for site in SETTINGS_CAMPSITES:
                if cells[0].text == site:
                    radio_button = cells[1].find_element_by_tag_name('input')
                    radio_button.click()
                    found_site = True
                    break
            if found_site:
                break
            r += 1
        except NoSuchElementException:
            continue

    submit_button = driver.find_elements_by_xpath(
        "//input[@value='Add Selected Sites']")[0]
    submit_button.click()

    # fourth page
    elem = driver.find_element_by_name("GroupCapacity_1")
    elem.send_keys(2)
    elem = driver.find_element_by_name("GroupCapacity_2")
    elem.send_keys(1)
    submit_button = driver.find_elements_by_xpath("//input[@value='Next']")[0]
    submit_button.click()

    # fifth page
    driver.find_element_by_class_name("button").click()

    # sixth page
    checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")
    for box in checkboxes:
        box.click()

    elem = driver.find_element_by_name("Value_3")
    elem.send_keys("Shafer Trail Road")

    elem = driver.find_element_by_name("Value_4")
    elem.send_keys("Top of Mineral Road Switchbacks")

    driver.find_element_by_class_name("button").click()

    # seventh page
    elem = driver.find_element_by_name("FirstName")
    elem.send_keys(SETTINGS_FIRST_NAME)
    elem = driver.find_element_by_name("LastName")
    elem.send_keys(SETTINGS_LAST_NAME)
    elem = driver.find_element_by_name("EmailAddress")
    elem.send_keys(SETTINGS_EMAIL)
    elem = driver.find_element_by_name("Address1")
    elem.send_keys(SETTINGS_ADDRESS_1)
    elem = driver.find_element_by_name("Address2")
    elem.send_keys(SETTINGS_ADDRESS_2)
    elem = driver.find_element_by_name("city")
    elem.send_keys(SETTINGS_CITY)
    elem = driver.find_element_by_name("state")
    elem.send_keys(SETTINGS_STATE)
    elem = driver.find_element_by_name("phone")
    elem.send_keys(SETTINGS_PHONE)
    elem = driver.find_element_by_name("zip")
    elem.send_keys(SETTINGS_ZIP)

    # driver.find_element_by_class_name("button").click()
    #
    # # eighth page
    # driver.find_elements_by_class_name("button")[1].click()

    # ninth page
    # driver.find_element_by_class_name("button").click()

    time.sleep(100)