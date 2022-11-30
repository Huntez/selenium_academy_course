from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from connections import cdrive_path

driver_path = Service(cdrive_path)
driver = webdriver.Chrome(service=driver_path)

try:
    driver.get("https://www.marvel.com/characters")
    character_names = driver.find_elements(By.XPATH, '''//*[@id="filter_grid-7"]/div/
div[3]/div[2]/div[@class="mvl-card mvl-card--explore"]/a/div[2]/p''')
    character_links = driver.find_elements(By.XPATH, '''//*[@id="filter_grid-7"]/div/
div[3]/div[2]/div[@class="mvl-card mvl-card--explore"]/a''')
    file = open("marvel_characters.txt", "w")
    href_list = [i.get_attribute("href") for i in character_links]
    for name, link in zip(character_names, href_list):
        file.write(name.text + " - " + link + "\n")
    file.close()
except Exception as error:
    print(f"Error - {error}")
finally:
    driver.close()
    driver.quit()