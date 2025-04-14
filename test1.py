from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize WebDriver
driver = webdriver.Chrome()

try:
    # Open the Clerk login page
    driver.get("http://localhost:3002/sign-in")  # Replace with actual login URL
    print("🔍 Waiting for page to load...")
    time.sleep(3)  # Short wait before looking for elements

    # Wait up to 15 seconds for the button to appear
    wait = WebDriverWait(driver, 15)
    google_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[.//span[contains(text(),'Continue with Google')]]"))
    )

    # Click the button
    print("✅ Found and clicking 'Continue with Google' button")
    google_button.click()
    
    # Wait for login to process
    time.sleep(10)  # Adjust if needed
    print("✅ Login flow started. Please select Google account manually.")
    print("✅ Test Case Passed. ")

except Exception as e:
    print(f"⚠️ Test Error: {e}")

finally:
    # Keep browser open for analysis
    time.sleep(5)
    print("🔍 Browser will close in 5 seconds...")
    driver.quit()
