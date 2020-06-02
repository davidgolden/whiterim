from selenium import webdriver
import time


def populate_form(camper):
    """ takes in an instance of the camper class which contains the relevant
     information to register a camper for the trail """
    url = 'https://canypermits.nps.gov/index.cfm'
    driver = webdriver.Chrome('./chromedriver')
    driver.get(url)

    # first page
    while driver.current_url == 'https://canypermits.nps.gov/index.cfm':
        driver.refresh()
        elem = driver.find_element_by_name("StartMonth")
        elem.send_keys(camper.month)

        elem = driver.find_element_by_name("StartDay")
        elem.send_keys(camper.day)

        elem = driver.find_element_by_name("StartYear")
        elem.send_keys(camper.year)

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
        cells = rows[r].find_elements_by_tag_name('td')
        if cells[0].text == camper.campsite1:
            radio_button = cells[1].find_element_by_tag_name('input')
            if radio_button:
                radio_button.click()
                break
        elif cells[0].text == camper.campsite2:
            radio_button = cells[1].find_element_by_tag_name('input')
            if radio_button:
                radio_button.click()
                break
        r += 1

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
    elem.send_keys(camper.first_name)
    elem = driver.find_element_by_name("LastName")
    elem.send_keys(camper.last_name)
    elem = driver.find_element_by_name("EmailAddress")
    elem.send_keys(camper.email_address)
    elem = driver.find_element_by_name("Address1")
    elem.send_keys(camper.address1)
    elem = driver.find_element_by_name("Address2")
    elem.send_keys(camper.address2)
    elem = driver.find_element_by_name("city")
    elem.send_keys(camper.city)
    elem = driver.find_element_by_name("state")
    elem.send_keys(camper.state)
    elem = driver.find_element_by_name("phone")
    elem.send_keys(camper.phone)
    elem = driver.find_element_by_name("zip")
    elem.send_keys(camper.zip)

    driver.find_element_by_class_name("button").click()

    # eighth page
    driver.find_elements_by_class_name("button")[1].click()

    # ninth page
    driver.find_element_by_class_name("button").click()

    time.sleep(100)