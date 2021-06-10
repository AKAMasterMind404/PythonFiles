# from yahoofinancials import YahooFinancials
#
# share='AAPL'
# a=YahooFinancials(share).get_financial_stmts('annual','balance')
# att=list(a['balanceSheetHistory'][share])
#
# print(att)
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# req = request(url='https://water.pcmcindia.gov.in/online_payment/waterbillpayment.html',method='get').text
#
# print('This is request')
# print(req)

url = 'https://finance.yahoo.com/screener/new'

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)

marketcapCloseButton = driver.find_element_by_xpath('//*[@id="screener-criteria"]/div[2]/div[1]/div[1]/div[2]/button')
marketcapCloseButton.click()

budget = driver.find_element_by_xpath('//*[@id="screener-criteria"]/div[2]/div[1]/div[1]/div[2]/div/div[2]/input')
budget.send_keys('500')

addSectorButton = driver.find_element_by_xpath(
    '//*[@id="screener-criteria"]/div[2]/div[1]/div[1]/div[3]/div/div[1]/div[2]/ul/li/div/div')
addSectorButton.click()
time.sleep(0.5)
basicMaterials = driver.find_element_by_xpath('//*[@id="dropdown-menu"]/div/div[2]/ul/li[1]/label')
consumerCyclical = driver.find_element_by_xpath('//*[@id="dropdown-menu"]/div/div[2]/ul/li[2]/label')
financialServices = driver.find_element_by_xpath('//*[@id="dropdown-menu"]/div/div[2]/ul/li[3]/label')
realEstate = driver.find_element_by_xpath('//*[@id="dropdown-menu"]/div/div[2]/ul/li[4]/label')
consumerDefensive = driver.find_element_by_xpath('//*[@id="dropdown-menu"]/div/div[2]/ul/li[5]/label')
healthcare = driver.find_element_by_xpath('//*[@id="dropdown-menu"]/div/div[2]/ul/li[6]/label')
utilities = driver.find_element_by_xpath('//*[@id="dropdown-menu"]/div/div[2]/ul/li[7]/label')
communication = driver.find_element_by_xpath('//*[@id="dropdown-menu"]/div/div[2]/ul/li[8]/label')
energy = driver.find_element_by_xpath('//*[@id="dropdown-menu"]/div/div[2]/ul/li[9]/label')
industrials = driver.find_element_by_xpath('//*[@id="dropdown-menu"]/div/div[2]/ul/li[10]/label')
technology = driver.find_element_by_xpath('//*[@id="dropdown-menu"]/div/div[2]/ul/li[11]/label')

time.sleep(1)

# basicMaterials.click()
# consumerCyclical.click()
# financialServices.click()
# realEstate.click()
# consumerDefensive.click()
healthcare.click()
# utilities.click()
# communication.click()
# energy.click()
# industrials.click()
# technology.click()
time.sleep(1)

findStocksButton = driver.find_element_by_xpath('//*[@id="screener-criteria"]/div[2]/div[1]/div[3]/button[1]')
time.sleep(1)
findStocksButton.click()
# time.sleep(4)