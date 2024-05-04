from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Define XPath expressions
next_button_xpath = '//*[@id="page-container"]/div[1]/div/div[2]/ul[2]/li[2]/a'
iframe_xpath = '//*[@id="f1"]'
search_button_xpath = '//*[@id="eymDb_content"]/div/div[2]/div[1]/div/table/thead/tr/th[10]/i'
search_input_xpath = 'input.lui-search__input'
export_data_xpath = '//*[@id="export-data"]/span'
table_formatting_xpath = '//*[@id="data-export-settings-dialog"]/div[2]/div/label/div/span[1]'
export_button_xpath = '//*[@id="data-export-settings-dialog"]/div[3]/button[2]'
confirm_export_button_xpath = '//*[@id="export-dialog"]/div/div[3]/button'
previous_button_xpath = '//*[@id="page-container"]/div[1]/div/div[2]/ul[2]/li[1]/a'
deselect_state_button_xpath = '//*[@id="51a8c2f6-d3bb-47c1-a26a-c90ba022d788_content"]/div/div/button[2]'
select_points_button_xpath = '//*[@id="f256a7bd-98df-4dbe-81b8-1da6d19363fd_content"]/div/div/button[1]/span'
title_xpath = '//*[@id="eymDb_title"]'

def wait_and_click(driver, xpath):
    element = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    element.click()

def wait_and_send_keys(driver, selector, keys):
    element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
    element.send_keys(keys)

def switch_to_iframe(driver, xpath):
    iframe = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, xpath)))
    driver.switch_to.frame(iframe)

def switch_to_default_content(driver):
    driver.switch_to.default_content()

STATE = ['NSW', 'VIC', 'QLD', 'SA', 'WA', 'TAS', 'NT', 'ACT']

for state in STATE:
    for i in range(10):
        try:
            webdriver_service = Service('/usr/local/bin/chromedriver')
            options = Options()
            options.headless = True
            driver = webdriver.Chrome(service=webdriver_service, options=options)

            url = 'https://api.dynamic.reports.employment.gov.au/anonap/extensions/hSKLS02_SkillSelect_EOI_Data/hSKLS02_SkillSelect_EOI_Data.html'
            driver.get(url)

            # Click on the first "Next" button
            wait_and_click(driver, next_button_xpath)

            # Switch to iframe
            switch_to_iframe(driver, iframe_xpath)

            # Select date, occupation, and state
            date_path = f'//*[@id="ABAjc_content"]/div/div/div/div/div/div/div/div[2]/div[2]/div[2]/div/div[3]/div/div[{i + 1}]/div/div[1]/span/span'
            wait_and_click(driver, date_path)
            wait_and_click(driver, '//*[@id="af5ad612-d258-4a07-ae94-2b47525975a7_content"]/div/div/button[1]/span')
            wait_and_click(driver, '//*[@id="51a8c2f6-d3bb-47c1-a26a-c90ba022d788_content"]/div/div/button[1]/span')

            switch_to_default_content(driver)

            # Click on the second "Next" button
            wait_and_click(driver, next_button_xpath)

            # Switch back to iframe
            switch_to_iframe(driver, iframe_xpath)

            # Click on the search button
            wait_and_click(driver, search_button_xpath)

            # Input search value and press Enter
            wait_and_send_keys(driver, search_input_xpath, state)
            wait_and_send_keys(driver, search_input_xpath, Keys.ENTER)

            switch_to_default_content(driver)

            # Click on the "Previous" button
            wait_and_click(driver, previous_button_xpath)

            switch_to_iframe(driver, iframe_xpath)

            # Deselect state
            wait_and_click(driver, deselect_state_button_xpath)

            # Select points
            wait_and_click(driver, select_points_button_xpath)

            switch_to_default_content(driver)

            # Click on the second "Next" button again
            wait_and_click(driver, next_button_xpath)

            switch_to_iframe(driver, iframe_xpath)

            # Right-click on the title
            content_menu = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, title_xpath)))
            ActionChains(driver).move_to_element(content_menu).context_click().perform()

            # Click on "Export Data" button
            wait_and_click(driver, export_data_xpath)

            # Click on "Table Formatting" button
            wait_and_click(driver, table_formatting_xpath)

            # Click on "Export" button
            wait_and_click(driver, export_button_xpath)

            # Confirm export
            wait_and_click(driver, confirm_export_button_xpath)

            driver.quit()
        except Exception as e:
            print(e)
            continue