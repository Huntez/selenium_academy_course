from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from connections import cdrive_path

driver_path = Service(cdrive_path)
driver = webdriver.Chrome(service=driver_path)

try:
    driver.get("https://www.marvel.com")
    file = open("marvel_characters.txt", "w")
    tags = driver.find_elements(By.XPATH, '''//*[@id="two_column-6"]/div/div[1]
/div/ul/div[@class="mvl-card mvl-card--feed"]/div/div/p[1]''')
    news_names = driver.find_elements(By.XPATH, '''//*[@id="two_column-6"]/div/div[1]/div/ul/
div[@class="mvl-card mvl-card--feed"]/div/div/p[2]''')
    for tag, nwname in zip(tags, news_names):
        file.write(tag.text + " - " + nwname.text + "\n")
    file.close()
except Exception as error:
    print(f"Error - {error}")
finally:
    driver.close()
    driver.quit()