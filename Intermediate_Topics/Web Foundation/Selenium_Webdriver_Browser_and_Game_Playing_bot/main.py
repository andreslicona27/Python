from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Web for the documentation of selenium
# https://selenium-python.readthedocs.io
# Web for the documentation of the locating elements
# https://selenium-python.readthedocs.io/locating-elements.html

driver = webdriver.Chrome()
driver.get("https://www.amazon.es/Olympians-Children-Collection-Lightning-Labyrinth/dp/9124369225/?_encoding=UTF8&pd_rd_w=9PBzO&content-id=amzn1.sym.8ddafe99-0303-437a-a80e-e4e34a8db807&pf_rd_p=8ddafe99-0303-437a-a80e-e4e34a8db807&pf_rd_r=2QYQD8KABPJJ0HB2JYY4&pd_rd_wg=mq3jr&pd_rd_r=7311d0cd-8923-4c2e-8da6-943a81f1ffb5&ref_=pd_gw_ci_mcx_mr_hp_atf_m")

# price = driver.find_element(By.ID, "priceblock_ourprice")
# print(price.text)
#
# search_bar = driver.element(By.NAME, "q")
# print(search_bar.get_attribute("placeholder"))
#
# logo = driver.find_element(By.TAG_NAME, "python-logo")
#
# documentation_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
# print(documentation_link.text)

# CLICK A LINK
link = driver.find_element(By.PARTIAL_LINK_TEXT, "the text of the link")
link.click()

# SEARCH SOMETHING IN THE FILL
search = driver.find_element(By.NAME, "search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)



# Just closes a single tap
driver.close()
# Quit the entire browser
driver.quit()


