from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pprint import pprint

# def max_page(driver):
#     pager = driver.find_element(by=By.CLASS_NAME, value='pager')
#     # print(pager.get_attribute('innerHTML'))
#     all_pages = pager.find_elements(by=By.CLASS_NAME, value='fleft')
#     last_page = all_pages[len(all_pages) - 1]
#     print(last_page.get_attribute('innerHTML'))
#     last_page_link = last_page.find_element(by=By.TAG_NAME, value='a')
#     last_page_link_child = last_page_link.find_element(by=By.TAG_NAME, value='span')
#     max_page = last_page_link_child.get_attribute('innerText')
#     # print(max_page)
#     return int(max_page)


def detail_product(result):
    try:
        result = driver.find_elements(by=By.CLASS_NAME, value='pad-hrz-xs')
        href = result.get_attribute('href') #get_attribute ??
        # print(href)
        return {'href': href}
    except NoSuchElementException:
        print('No details for this product')
        return None


driver = webdriver.Edge()
driver.get("http://emag.ro")
elem = driver.find_element(by=By.NAME, value="query")
elem.clear()
elem.send_keys("huawei p50")
elem.send_keys(Keys.RETURN)

url = driver.current_url
all_ads = []

offers_table = driver.find_element(by=By.ID, value='card_grid')
wrap_list = offers_table.find_elements(by=By.LINK_TEXT, value='Huawei P50 Pro') #data-name: Telefon .. Huawei P50 Pro
print(wrap_list)
for result in wrap_list:
    ad = detail_product(result)
    if ad is not None:
        all_ads.append(ad)

file = open('offers.txt', 'w')
file.write(str(all_ads))
file.close()

driver.close()