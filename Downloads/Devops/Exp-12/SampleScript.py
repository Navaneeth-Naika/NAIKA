import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

print("Test Execution Started")

# Set Edge options
options = webdriver.EdgeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--start-maximized')  # Start with a maximized window
options.add_argument('--disable-gpu')  # Disable GPU hardware acceleration
options.add_argument('--force-device-scale-factor=1')  # Force software rendering
# options.add_argument('--headless')  # Uncomment for headless mode

# Provide the path to msedgedriver.exe
driver_path = r"C:\Users\naika\Downloads\Devops\Exp-12\msedgedriver.exe"  # Update the path if necessary

# Initialize Edge WebDriver using the path to the driver
driver = webdriver.Edge(service=Service(driver_path), options=options)

# Maximize the browser window
driver.maximize_window()

# Navigate to the registration page served by the Docker container
driver.get("http://localhost:8087/index.html")
print("Navigating to the form...")

try:
    # Wait for the form to load and check for the first name field
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "firstName")))
    print("Form loaded successfully!")

    # Fill the registration form
    driver.find_element(By.ID, "firstName").send_keys("Test User")
    driver.find_element(By.ID, "lastName").send_keys("Ruthvik")
    driver.find_element(By.ID, "email").send_keys("test@gmail.com")
    driver.find_element(By.ID, "phone").send_keys("1234567892")

    # Wait for the submit button to be clickable before submitting
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))

    # Submit the form
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    print("Form submitted.")

    # Wait for the confirmation message (from JavaScript)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "successMessage"))
    )

    # Verify the confirmation message
    confirmation_message = driver.find_element(By.ID, "successMessage").text
    if "Thank you for registering!" in confirmation_message:
        print("Test Passed!")
    else:
        print("Test Failed! Message not as expected.")

except Exception as e:
    print("Test Failed! Error message:", e)

finally:
    # Ensure the driver quits properly even if the test fails
    try:
        time.sleep(2)  # Wait a bit before closing to ensure no premature closure
        driver.quit()  # End the WebDriver session
        print("Browser closed successfully.")
    except Exception as e:
        print("Error while closing the browser:", e)

print("Test Execution Completed Successfully!")
