from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import connections
import links

driver_path = Service(links.cdrive_path)
driver = webdriver.Chrome(service=driver_path)
wait = WebDriverWait(driver, 10)
driver.implicitly_wait(10)

# Opening file for writing schelude
file = open('mystat_schelude.txt', 'w')

try:
    # Authentication
    driver.get(links.mystat_login)
    username = driver.find_element(By.ID, 'username') 
    password = driver.find_element(By.ID, 'password')
    username.send_keys(connections.user_name)
    password.send_keys(connections.password)
    driver.find_element(By.CLASS_NAME, 'login-action').click()

    # Waiting until page load
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'go-to-details'))) 

    # Going to schelude page
    driver.get(links.mystat_schelude)

    # Getting mount and active days in this mount
    mount = driver.find_element(By.CLASS_NAME, 'mount')
    active_days = driver.find_elements(By.CLASS_NAME, 'active-day')

    for i in active_days:
        # Clicks by active days
        i.click()

        # Close pop up active day
        wait.until(EC.element_to_be_clickable((By.XPATH, links.mystat_close_button))).click()
        
        # Write date from active day to file
        file.write(driver.find_element(By.XPATH, links.mystat_day_date).text + '\n')

        # Parsing all couples
        lesson = driver.find_elements(By.CLASS_NAME, 'lessons')

        # Write every couple in file
        for i in lesson:
            file.write(i.text + '\n\n')

    # Closing file after writing schelude
    file.close()
except Exception as error:
    print(f'Error - {error}')
finally:
    driver.close()
    driver.quit()