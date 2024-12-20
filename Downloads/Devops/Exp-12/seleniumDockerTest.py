from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

print("Test Execution Started")

# Set up Chrome options
options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')

# Initialize the remote WebDriver
driver = webdriver.Remote(
    command_executor='http://localhost:4444/wd/hub',
    options=options
)

# Maximize the window
driver.maximize_window()
time.sleep(2)

# Navigate to Testsigma
driver.get("https://www.testsigma.com/")
time.sleep(2)

# Locate the link by its text and click
try:
    driver.find_element(By.LINK_TEXT, "Testsigma Cloud").click()
    time.sleep(2)
except Exception as e:
    print(f"An error occurred: {e}")

# Close the browser
driver.close()
driver.quit()

print("Test Execution Completed Successfully!")