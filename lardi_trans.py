from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import connections
import links

first_country = input('First country : ')
second_country = input('Second country : ')
first_city = input('First city : ')
second_city = input('Second city : ')

if not first_country and second_country:
    raise Exception("Country reqired!")

file = open("lt_info_and_cost.txt", "w")

driver_path = Service(links.cdrive_path)
driver = webdriver.Chrome(service=driver_path)
wait = WebDriverWait(driver, 10)
driver.implicitly_wait(10)

try:
    driver.get(links.lt_gruz)

    if first_country:
        wait.until(EC.visibility_of_element_located((By.XPATH,  
        links.lt_send))).send_keys(first_country, Keys.ENTER)

    if second_country:
        wait.until(EC.visibility_of_element_located((By.XPATH,  
        links.lt_recive))).send_keys(second_country, Keys.ENTER)
    
    if first_city:
        fc_line = wait.until(EC.visibility_of_element_located((By.XPATH,  
        links.lt_city_send)))
        fc_line.send_keys(first_city)
        wait.until(EC.visibility_of_any_elements_located((By.CLASS_NAME,
        'css-82wl56-option'))), fc_line.send_keys(Keys.ENTER)

    if second_city:
        sc_line = wait.until(EC.visibility_of_element_located((By.XPATH,  
        links.lt_city_recive)))
        sc_line.send_keys(second_city)
        wait.until(EC.visibility_of_any_elements_located((By.CLASS_NAME,
        'css-82wl56-option'))), sc_line.send_keys(Keys.ENTER)

    driver.find_element(By.XPATH,links.lt_src_button).click()
    print(wait.until(EC.visibility_of_element_located((By.XPATH,
    links.lt_search_result))).text)
    
    driver.implicitly_wait(0)
    page_count = driver.find_elements(By.XPATH,
    links.lt_page_count)
    if len(page_count) == 1:
        page_count = int(page_count[0].text)
    else:
        page_count = 1

    for i in range(page_count):
        payments = [i.text for i in wait.until(
        EC.visibility_of_all_elements_located((By.XPATH,
        links.lt_cost))) if i.text != '']

        info = [i.text for i in wait.until(
        EC.visibility_of_all_elements_located((By.XPATH,
        links.lt_info))) if i.text != '']
        
        for cost, info in zip(payments, info):
            file.write(f'{cost} - {info}\n')

        if i != page_count:
            wait.until(EC.element_to_be_clickable((By.XPATH, 
            '//a[contains(@rel,"next")]'))).click()

    file.close()
except Exception as error:
    print(f'Error - {error}')
finally:
    driver.close()
    driver.quit()