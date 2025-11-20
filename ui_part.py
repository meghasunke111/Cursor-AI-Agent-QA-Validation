from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from config import EMAIL, PASSWORD

def ui_validate_event(event):
    print("\n🔵 UI Automation Started…")

    # ---------------- HEADLESS CHROME SETUP ----------------
    chrome_options = Options()
    chrome_options.add_argument("--headless")                # Run headless
    chrome_options.add_argument("--no-sandbox")              # Required for GitHub Actions
    chrome_options.add_argument("--disable-dev-shm-usage")   # Prevent limited resource errors
    chrome_options.add_argument("--window-size=1920,1080")   # Set viewport size

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                              options=chrome_options)

    driver.maximize_window()
    wait = WebDriverWait(driver, 15)
    ob = ActionChains(driver)

    # ---------------- LOGIN ----------------
    print("➡ Logging in...")
    driver.get("https://events.webmobi.com/auth/login")

    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='email']"))).send_keys(EMAIL)
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='password']"))).send_keys(PASSWORD)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Sign in']"))).click()

    wait.until(EC.url_contains("/dashboard"))
    print("✅ Login Successful")

    # ---------------- CREATE EVENT ----------------
    print("➡ Creating event through UI…")
    driver.get("https://events.webmobi.com/dashboard/create")
    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Create Event']"))).click()

    wait.until(EC.presence_of_element_located((By.XPATH, "//textarea[@data-slot='textarea']"))).send_keys("Hybrid Automation Test Event")
    ob.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    print("✅ Event Created Successfully in UI")

    # ---------------- VALIDATION ----------------
    print("➡ Validating event in UI…")
    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='My Events']"))).click()
    search = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search events...']")))
    search.send_keys('Hybrid Automation Test Event')
    sleep(2)

    results = driver.find_elements(By.XPATH, f"//*[contains(text(),'Hybrid Automation Test Event')]")
    if results:
        print("🎉 VALIDATION SUCCESS — Event found!")
    else:
        print("❌ VALIDATION FAILED — Event not visible in UI")

    driver.quit()
