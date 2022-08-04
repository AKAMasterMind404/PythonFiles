import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains as ac

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.mathsisfun.com/games/towerofhanoi.html')

time.sleep(1.5)

d1=d2=d3=d4=d5=d6=d7=d8=None

try:
    d1=driver.find_element_by_xpath('//*[@id="disks"]/div[1]')
    d2=driver.find_element_by_xpath('//*[@id="disks"]/div[2]')
    d3=driver.find_element_by_xpath('//*[@id="disks"]/div[3]')
    d4=driver.find_element_by_xpath('//*[@id="disks"]/div[4]')
    d5=driver.find_element_by_xpath('//*[@id="disks"]/div[5]')
    d6=driver.find_element_by_xpath('//*[@id="disks"]/div[6]')
    d7=driver.find_element_by_xpath('//*[@id="disks"]/div[7]')
    d8=driver.find_element_by_xpath('//*[@id="disks"]/div[8]')
except:
    pass

total_disks=3

add_disks_bt=driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/button[2]')
remove_disks_bt=driver.find_element_by_xpath('//*[@id="dnBtn"]')

for i in range(total_disks-3):
    add_disks_bt.click()
    time.sleep(0.1)

if d1:
    # print(d1.top)
    ex=d1.location['x']
    ey=d1.location['y']
    ac(driver).drag_and_drop_by_offset(d1, 50, 50).perform()