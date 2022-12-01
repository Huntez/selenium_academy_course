from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
import links

driver_path = Service(links.cdrive_path)
driver = webdriver.Chrome(service=driver_path)

try:
    driver.get(links.mv_characters)
    next_button = driver.find_element(By.XPATH, links.next_button)
    file = open("marvel_characters.txt", "w")
    for i in range(1):
        character_names = driver.find_elements(By.XPATH, links.chr_name)
        character_links = driver.find_elements(By.XPATH, links.chr_links)
        href_list = [i.get_attribute("href") for i in character_links]
        chrc_list = [i.text for i in character_names]
        for j in range(len(href_list)):
            driver.get(href_list[j])
            category = driver.find_elements(By.XPATH, links.bio_ctg)
            info = driver.find_elements(By.XPATH, links.bio_info)
            file.write("\n" + chrc_list[j] + " - " + href_list[j] + "\n")
            for ctg, inf in zip(category, info):
                file.write(ctg.text + " - " + inf.text + "\n")
        driver.get(links.mv_characters)
        next_button.click()
    file.close()
except Exception as error:
    print(f"Error - {error}")
finally:
    driver.close()
    driver.quit()