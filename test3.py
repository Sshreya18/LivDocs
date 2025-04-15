from selenium import webdriver
import time

# Set up WebDriver (Chrome in this case)
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
driver = webdriver.Chrome(options=options)

# URL to test
url = "https://livedocs-sand.vercel.app/"  # Change to your app's URL

# Start timer before loading page
start_time = time.time()

# Load the page
driver.get(url)

# End timer after load
end_time = time.time()

# Calculate load time
load_time = end_time - start_time
print(f"⏱️ Page Load Time: {load_time:.2f} seconds")

# Optional: Wait a bit and close
time.sleep(2)
driver.quit()
