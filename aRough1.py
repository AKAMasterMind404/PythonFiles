#importing webdriver from selenium
from selenium import webdriver

#selecting Firefox as the browser
#in order to select Chrome
# webdriver.Chrome() will be used
driver = webdriver.Chrome(executable_path = 'C:/Users/Admin/Downloads/chromedriver.exe')

#URL of the website
url = "https://surveyheart.com/form/61f412c4c0f30029d1542fee"

#opening link in the browser
driver.get(url)

# start_survey_button = driver.find_element_by_xpath('//*[@id="start_survey_button"]')
# start_survey_button.click()