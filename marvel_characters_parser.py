from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import links

# asks the user for the number of pages
pages_count = int(input("Page count : "))

driver_path = Service(links.cdrive_path)
driver = webdriver.Chrome(service=driver_path)
wait = WebDriverWait(driver, 10)
driver.implicitly_wait(10)

# File opening
file = open("marvel_characters.txt", "w")

# Lists for links
href_list, chrc_list = [], []

try:
    # Open marvel characters page
    driver.get(links.mv_characters)

    # Find next button on page
    next_button = driver.find_element(By.XPATH, links.next_button)

    # Parsing characters names and links on n pages
    for page_number in range(pages_count):
        character_names = wait.until(EC.visibility_of_all_elements_located
        ((By.XPATH, links.chr_name)))
        character_links = wait.until(EC.visibility_of_all_elements_located
        ((By.XPATH, links.chr_links)))
        
        # Generate lists with names and links
        chrc_list += [i.text for i in character_names]
        href_list += [i.get_attribute("href") for i in character_links]
        
        # Click on the next button
        next_button.click()

    for link_number in range(len(href_list)):
        # Going to every page in href list
        driver.get(href_list[link_number])
        
        # Parsing character bio
        category = driver.find_elements(By.XPATH, links.bio_ctg)
        info = driver.find_elements(By.XPATH, links.bio_info)

        # Writing result in file
        file.write("\n" + chrc_list[link_number] + " - " + href_list[link_number] + "\n")
        for ctg, inf in zip(category, info):
            file.write(ctg.text + " - " + inf.text + "\n")

    # Closing file after writing all data       
    file.close()
except Exception as error:
    print(f"Error - {error}")
finally:
    driver.close()
    driver.quit()