import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService

# List of browsers and their respective WebDriver constructors and Service objects
browsers = [
    ("Chrome", webdriver.Chrome, ChromeService()),
    ("Firefox", webdriver.Firefox, FirefoxService()),
    ("Edge", webdriver.Edge, EdgeService())
]

for browser_name, browser_constructor, service in browsers:
    print(f"\n===== Running on {browser_name} =====")
    driver = browser_constructor(service=service)
    try:
        # 1️⃣ Open https://rahulshettyacademy.com
        driver.get("https://rahulshettyacademy.com")

        # 2️⃣ Print the title of the page
        print("Page Title:", driver.title)

        # 3️⃣ Wait 2 seconds, then navigate to Wikipedia
        time.sleep(2)
        driver.get("https://www.wikipedia.org")

        # 4️⃣ Maximize the browser window
        driver.maximize_window()

        # 5️⃣ Print the current URL of the page
        print("Current URL:", driver.current_url)

        # 6️⃣ Go back to https://rahulshettyacademy.com
        driver.back()
        time.sleep(2)  # Wait for the page to load

        # 7️⃣ Take a screenshot and save as rahul_homepage.png
        screenshot_name = "rahul_homepage.png"
        driver.save_screenshot(screenshot_name)
        print(f"Screenshot saved as {screenshot_name}")

    finally:
        # 8️⃣ Close the browser
        driver.quit()
