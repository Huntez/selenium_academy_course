from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from connections import cdrive_path

driver_path = Service(cdrive_path)
driver = webdriver.Chrome(service=driver_path)

try:
    driver.get("https://www.marvel.com")
    # file = open("marvel_characters.txt", "w")
    news_names = driver.find_elements(By.XPATH, '''//*[@id="two_column-6"]/div/div[1]/div/ul/
div[@class="mvl-card mvl-card--feed"]/div/div/p[2]/a''')
    href_list = [i.get_attribute("href") for i in news_names]
    for i in range(len(href_list)):
        driver.get(href_list[i])
        driver.get_screenshot_as_file(f"{i}.png")
except Exception as error:
    print(f"Error - {error}")
finally:
    driver.close()
    driver.quit()