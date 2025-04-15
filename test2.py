from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Start WebDriver
driver = webdriver.Chrome()

# Open Clerk Login Page
driver.get("https://livedocs-sand.vercel.app/")  # Update if needed

input("Press Enter once you are on the dashboard...")  # Manual wait for dashboard

# Wait until the URL starts with "http://localhost:3000/documents/"
try:
    WebDriverWait(driver, 60).until(lambda d: d.current_url.startswith("https://livedocs-sand.vercel.app/documents/"))
    print(f"Successfully navigated to the document: {driver.current_url}")
except:
    print("Failed to detect navigation to a document!")

# Keep browser open for debugging
print("The browser will remain open. Manually close it when you're done.")
input("Press Enter to close the browser...")
driver.quit()
