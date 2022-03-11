from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pprint import pprint


def max_page(driver):
    pager = driver.find_element(by=By.CLASS_NAME, value='pager')
    # print(pager.get_attribute('innerHTML'))
    all_pages = pager.find_elements(by=By.CLASS_NAME, value='fleft')
    last_page = all_pages[len(all_pages) - 1]
    print(last_page.get_attribute('innerHTML'))
    last_page_link = last_page.find_element(by=By.TAG_NAME, value='a')
    last_page_link_child = last_page_link.find_element(by=By.TAG_NAME, value='span')
    max_page = last_page_link_child.get_attribute('innerText')
    # print(max_page)
    return int(max_page)


def parse_result(result):
    try:
        details_link = result.find_element(by=By.CLASS_NAME, value='detailsLink')
        href = details_link.get_attribute('href')
        print(href)
        return {'href':href}
    except NoSuchElementException:
        print('No details for this product')
        return None


driver = webdriver.Chrome()
driver.get("http://olx.ro")
# assert "Python" in driver.title
elem = driver.find_element(by=By.NAME, value="q")
elem.clear()
elem.send_keys('logitech g29')
elem.send_keys(Keys.RETURN)

last_page = max_page(driver)
url = driver.current_url
# print(url)

all_ads = []

for page in range(1, last_page + 1):
    driver.get(url + f'?page={page}')
    driver.implicitly_wait(3)
    offers_table = driver.find_element(by=By.ID, value='offers_table')
    wrap_list = offers_table.find_elements(by=By.CLASS_NAME, value='wrap')
    # print(len(wrap_list))
    for result in wrap_list:
        ad = parse_result(result)
        if ad is not None:
            all_ads.append(ad)

# pprint(all_ads)
file = open('offers.txt', 'w')
file.write(str(all_ads))
file.close()

driver.close()
