from behave import *
import selenium
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager

#  found some issues with Chrome not being correctly found in system path,
#  this try/except logic will ensure the driver is at least cached while code is run

try:
    driver = Chrome()
except selenium.common.exceptions.WebDriverException:
    driver = Chrome(ChromeDriverManager().install())  # Found this in Stackoverflow  https://stackoverflow.com/a/52878725/13449108
finally:
    @given('User enters Jeffery')
    def step_imp(context):
        driver.get('http://127.0.0.1:5000')
        name_entry = driver.find_element_by_id('name')
        name_entry.send_keys('Jeffery')
        submit = driver.find_element_by_id('submit')
        submit.click()

    @then('Browser returns Hello Jeffery')
    def step_imp(context):
        response = driver.find_element_by_id('greet').text
        assert response == 'Hello Jeffery'


