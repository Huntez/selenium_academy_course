from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import connections
import links

try:
    file = open(f'{input("File name : ")}.txt', 'r')
except FileNotFoundError:
    raise Exception("File not exist!")
else:
    email_list = [i for i in file]
    user_theme = input("Theme : ")
    user_message = input("Message : ")

driver_path = Service(links.cdrive_path)
driver = webdriver.Chrome(service=driver_path)
wait = WebDriverWait(driver, 20)
driver.implicitly_wait(20)

try:
    # Login into outlook
    driver.get(links.outlook_login)
    wait.until(EC.visibility_of_element_located((By.ID, 
    'i0116'))).send_keys(connections.outlook_login)
    wait.until(EC.element_to_be_clickable((By.ID, 'idSIButton9'))).click()
    wait.until(EC.visibility_of_element_located((By.ID, 
    'i0118'))).send_keys(connections.outlook_pass)
    wait.until(EC.element_to_be_clickable((By.ID, 'idSIButton9'))).click()
    wait.until(EC.element_to_be_clickable((By.ID, 'idBtn_Back'))).click()

    # Send message
    wait.until(EC.element_to_be_clickable((By.XPATH,
    links.outlook_send_btn))).click()
    
    for email in email_list:
        wait.until(EC.visibility_of_element_located((By.XPATH,
        links.outlook_recivers))).send_keys(email + ',')

    wait.until(EC.visibility_of_element_located((By.XPATH, 
    links.outlook_theme))).send_keys(user_theme)
    driver.find_element(By.CLASS_NAME,
    'elementToProof').send_keys(user_message)
    driver.find_element(By.XPATH, links.outlook_snd_msg).click()

except Exception as error:
    print(f'Error - {error}')
finally:
    driver.close()
    driver.quit()