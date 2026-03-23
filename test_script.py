from selenium import webdriver
from selenium.webdriver.common.by import By
from self_healing import SelfHealing

def test_google_search():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")

    elements = ["name=q", "name=search", "id=searchBox"]
    healer = SelfHealing(elements)

    locator = "name=search_box"  # Broken locator
    fixed = healer.heal(locator)

    if fixed:
        by, value = fixed.split("=")
        search_box = driver.find_element(By.NAME, value)
        search_box.send_keys("AI Testing")

    driver.quit()
