from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import links
import time

driver_path = Service(links.cdrive_path)
driver = webdriver.Chrome(service=driver_path)

try:
    file = open("marvel_characters.txt", "w")
    href_list, chrc_list = [], []
    driver.get(links.mv_characters)
    next_button = driver.find_element(By.XPATH, links.next_button)
    for page_number in range(2):
        time.sleep(5)
        character_names = driver.find_elements(By.XPATH, links.chr_name)
        character_links = driver.find_elements(By.XPATH, links.chr_links)
        href_list += [i.get_attribute("href") for i in character_links]
        chrc_list += [i.text for i in character_names]
        print(chrc_list)
        next_button.click()
    for link_number in range(len(href_list)):
        driver.get(href_list[link_number])
        category = driver.find_elements(By.XPATH, links.bio_ctg)
        info = driver.find_elements(By.XPATH, links.bio_info)
        file.write("\n" + chrc_list[link_number] + " - " + href_list[link_number] + "\n")
        for ctg, inf in zip(category, info):
            file.write(ctg.text + " - " + inf.text + "\n")
    file.close()
except Exception as error:
    print(f"Error - {error}")
finally:
    driver.close()
    driver.quit()