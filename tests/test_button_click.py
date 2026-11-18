"""
Automated Webpage Testing using Selenium
Lab Project 15: Button Click Event & Alert Interception
"""

import os
import sys
import time
import argparse
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def setup_driver(headless=True):
    chrome_options = Options()
    if headless:
        chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1280,800")
    
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    return driver


def run_tests(target_url=None):
    if not target_url:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        index_file = os.path.join(base_dir, "index.html")
        target_url = f"file:///{index_file.replace(os.sep, '/')}"

    print("=" * 65)
    print(" SELENIUM AUTOMATED TEST SUITE: PROJECT 15 (BUTTON CLICK EVENT)")
    print(f" Target URL: {target_url}")
    print(f" Timestamp:  {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 65)

    driver = setup_driver(headless=True)
    tests_passed = 0
    tests_failed = 0

    try:
        # Load webpage
        driver.get(target_url)
        wait = WebDriverWait(driver, 10)

        # Test 1: Page Title
        print("\n[TEST 1] Verifying Page Title...")
        title = driver.title
        assert "Button Click Event" in title, f"Expected 'Button Click Event' in title, got: '{title}'"
        print(f"  [PASS] Page Title is valid: '{title}'")
        tests_passed += 1

        # Test 2: Button Element Existence
        print("\n[TEST 2] Verifying Button Element Presence...")
        button = wait.until(EC.element_to_be_clickable((By.ID, "alert-button")))
        assert button is not None
        print(f"  [PASS] Found button with text: '{button.text}'")
        tests_passed += 1

        # Test 3: Click Event & Alert Interception (1st Click)
        print("\n[TEST 3] Triggering Button Click and Intercepting Alert...")
        button.click()

        # Wait for JavaScript alert dialog to open
        alert = wait.until(EC.alert_is_present())
        alert_text = alert.text
        print(f"  [INFO] Intercepted Alert Text: '{alert_text}'")

        expected_phrase = "Button was clicked successfully"
        assert expected_phrase in alert_text, (
            f"Expected alert to contain '{expected_phrase}', but received '{alert_text}'"
        )
        print("  [PASS] Alert text verified successfully.")

        # Accept / dismiss the alert dialog
        alert.accept()
        print("  [PASS] Alert dialog accepted.")
        tests_passed += 1

        # Test 4: Verify DOM Click Counter Incremented to 1
        print("\n[TEST 4] Verifying Click Counter Updated to 1...")
        time.sleep(0.3)
        counter_elem = driver.find_element(By.ID, "click-count")
        assert counter_elem.text.strip() == "1", f"Expected count '1', got '{counter_elem.text}'"
        print("  [PASS] Click counter updated to '1' in DOM.")
        tests_passed += 1

        # Test 5: Second Button Click & Counter Increment to 2
        print("\n[TEST 5] Testing Second Click Event & Counter Increment...")
        button.click()
        alert = wait.until(EC.alert_is_present())
        alert.accept()
        time.sleep(0.3)
        counter_elem = driver.find_element(By.ID, "click-count")
        assert counter_elem.text.strip() == "2", f"Expected count '2', got '{counter_elem.text}'"
        print("  [PASS] Second click successfully incremented counter to '2'.")
        tests_passed += 1

        # Test 6: Reset Counter Action
        print("\n[TEST 6] Testing Reset Counter Action...")
        reset_btn = driver.find_element(By.ID, "reset-button")
        reset_btn.click()
        time.sleep(0.3)
        counter_elem = driver.find_element(By.ID, "click-count")
        assert counter_elem.text.strip() == "0", f"Expected count '0' after reset, got '{counter_elem.text}'"
        print("  [PASS] Reset button successfully restored counter to '0'.")
        tests_passed += 1

    except AssertionError as ae:
        print(f"  [FAIL] Assertion failed: {ae}")
        tests_failed += 1
    except Exception as ex:
        print(f"  [ERROR] Test execution failed with exception: {ex}")
        tests_failed += 1
    finally:
        driver.quit()

    print("\n" + "=" * 65)
    print(f" TEST RUN SUMMARY: {tests_passed} PASSED | {tests_failed} FAILED")
    print("=" * 65)
    return tests_failed == 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Automated Selenium tests for Button Click Event")
    parser.add_argument("--url", help="Target URL (e.g., http://localhost:8000 or http://localhost:30015)")
    args = parser.parse_args()

    success = run_tests(args.url)
    sys.exit(0 if success else 1)
