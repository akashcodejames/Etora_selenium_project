import time
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = uc.Chrome()
USERNAME = "ddrroorr"
driver.get(f"https://www.etoro.com/people/{USERNAME}/stats")
elements = driver.find_elements(By.XPATH, "//div[@class='performance-chart-slot year desk']")
# xtr = driver.find_elements(By.XPATH, "//div[@class='expand-button']/span[2]")
# xtr.click()
values = driver.find_elements(By.XPATH, "//div[@automation-id='cd-user-stats-performance-chart-slot-amount-month']")

show_more_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, "//span[@automation-id='cd-user-stats-performance-chart-show-more-text']"))
)

# Click the 'Show More' button
show_more_button.click()
years = []
for element in elements:
    year = element.text
    years.append(year)
    # print(year)
lst = [[] for _ in range(len(years))]
i = 0
lst_index = 0
for element in values:
    (lst[lst_index]).append(element.text
                            )
    # print(element.text)
    if i == 11:
        i = 0
        lst_index += 1
    else:
        i += 1
reversed_lst = [sublist[::-1] for sublist in lst]
reversed_lst = [[float(val) if val != '' else 0 for val in sub] for sub in reversed_lst]

months = list(range(1, 13))

result_dict = {}

for year, data in zip(years, reversed_lst):
    year_dict = {}
    for month, value in zip(months, data):
        year_dict[month] = value
    result_dict[int(year)] = year_dict
print(result_dict)
while True:
    pass
