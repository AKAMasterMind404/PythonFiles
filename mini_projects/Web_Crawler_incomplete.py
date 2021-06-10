import time
from cryptography.fernet import Fernet
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.webdriver.chromedriver import Chromedriver
# req = request(url='https://water.pcmcindia.gov.in/online_payment/waterbillpayment.html',method='get').text
#
# print('This is request')
# print(req)

key = Fernet.generate_key()
cipher_suite = Fernet(key)

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://water.pcmcindia.gov.in/online_payment/waterbillpayment.html')

time.sleep(1.5)

myConsumerID=27061

inp=driver.find_element_by_xpath('//*[@id="loadingwaterpay"]/div/div[1]/div[1]/div[2]/form/div/input')
inp.send_keys(myConsumerID)

button=driver.find_element_by_xpath('//*[@id="loadingwaterpay"]/div/div[1]/div[1]/div[2]/form/div/span/button')
button.click()

time.sleep(2)

captcha=driver.find_element_by_xpath('//*[@id="mainCaptcha"]')
captcha=captcha.text[0::2] # A b 4 t U
print(captcha)

textfieldCaptcha=driver.find_element_by_xpath('//*[@id="txtInput"]')
captcha_button=driver.find_element_by_xpath('//*[@id="Button1"]')

textfieldCaptcha.send_keys(captcha)
time.sleep(1.5)
captcha_button.click()

amount_tf=driver.find_element_by_xpath('//*[@id="maindata"]/div/section/div/div[2]/div[1]/div/form/span/div/input')
time.sleep(1.5)

amount_to_be_paid=driver.find_element_by_xpath("//*[@id=\"maindata\"]/div/section/div/div[2]/div[1]/div/ul/li/span[2]/h2").text
print(amount_to_be_paid)

if not amount_to_be_paid:
    amount_to_be_paid=1

amount_tf.send_keys(amount_to_be_paid)

pay_bt=driver.find_element_by_xpath('//*[@id="maindata"]/div/section/div/div[2]/div[1]/div/form/span/div/span/button')

pay_bt.click()

time.sleep(2.5)

mobile_tf=driver.find_element_by_xpath('//*[@id="mobile"]')
mobile_tf.clear() #To clear the text fields
mobile_tf.send_keys('8668692436')

email_td=driver.find_element_by_xpath('//*[@id="email"]')
email_td.clear()
email_td.send_keys('atharvkarbhari123@gmail.com')

bt=driver.find_element_by_xpath('//*[@id="myModal"]/div/div/div[3]/button')
time.sleep(1.5)
bt.click()

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://pgi.billdesk.com/pgidsk/ProcessPayment;jsessionid=00007tXpFXbO16TrjBsHQ91GWmQ:1a7ou2u29?wpage=ueB4jSgJZlXl6bB1Gt6XvVGd')

card_no=driver.find_element_by_xpath('//*[@id="cnumber"]')
card_no.send_keys('4029855037909435')

expiry_month=driver.find_element_by_xpath('//*[@id="expmon"]')
expiry_month.click()
expiry_month.send_keys('04')
expiry_month.click()

# expiry_year=driver.find_element_by_xpath('document.querySelector("#expyr")')
# expiry_year.click()
# expiry_year.send_keys('2023')
# expiry_year.click()


cvv_tf=driver.find_element_by_xpath('//*[@id="cvv2"]')
cvv_tf.send_keys('000')
#
card_holder=driver.find_element_by_xpath('//*[@id="cname2"]')
card_holder.send_keys('ATHARV KARBHARI')

make_payment=driver.find_element_by_xpath('//*[@id="proceedForm"]')
click=driver.find_element_by_xpath('//*[@id="proceedForm"]').click()