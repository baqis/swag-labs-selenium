import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_success_login(self):
        # steps
        browser = self.browser  # buka web browser
        browser.get("https://www.saucedemo.com/")  # buka situs
        time.sleep(2)
        browser.find_element(
            By.ID, "user-name").send_keys("standard_user")  # isi email
        time.sleep(1)
        browser.find_element(By.ID, "password").send_keys(
            "secret_sauce")  # isi password
        time.sleep(1)
        # klik tombol sign in
        browser.find_element(By.ID, "login-button").click()
        time.sleep(1)

        # validasi
        response_data = browser.find_element(
            By.CLASS_NAME, "title").text

        self.assertEqual('Products', response_data)
        time.sleep(3)

    def test_b_failed_login_with_empty_password(self):
        # steps
        browser = self.browser  # buka web browser
        browser.get("https://www.saucedemo.com/")  # buka situs
        time.sleep(2)
        browser.find_element(
            By.ID, "user-name").send_keys("standard_user")  # isi email
        time.sleep(1)
        browser.find_element(By.ID, "password").send_keys(
            "")  # isi password
        time.sleep(1)
        # klik tombol sign in
        browser.find_element(By.ID, "login-button").click()
        time.sleep(1)

        # validasi
        response_data = browser.find_element(
            By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3').text

        self.assertEqual('Epic sadface: Password is required', response_data)
        time.sleep(3)

    def test_c_failed_login_with_empty_email_and_password(self):
        # steps
        browser = self.browser  # buka web browser
        browser.get("https://www.saucedemo.com/")  # buka situs
        time.sleep(2)
        browser.find_element(
            By.ID, "user-name").send_keys("")  # isi email
        time.sleep(1)
        browser.find_element(By.ID, "password").send_keys("")  # isi password
        time.sleep(1)
        # klik tombol sign in
        browser.find_element(By.ID, "login-button").click()
        time.sleep(1)

        # validasi
        response_data = browser.find_element(
            By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3').text

        self.assertEqual('Epic sadface: Username is required', response_data)
        time.sleep(3)

    def test_d_success_add_to_cart(self):
        # steps
        browser = self.browser  # buka web browser
        browser.get("https://www.saucedemo.com/")  # buka situs
        time.sleep(2)
        browser.find_element(
            By.ID, "user-name").send_keys("standard_user")  # isi email
        time.sleep(1)
        browser.find_element(By.ID, "password").send_keys(
            "secret_sauce")  # isi password
        time.sleep(1)
        # klik tombol sign in
        browser.find_element(By.ID, "login-button").click()
        time.sleep(1)
        browser.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        time.sleep(1)
        browser.find_element(By.ID, "shopping_cart_container").click()
        time.sleep(1)

        # validasi
        response_data = browser.find_element(
            By.CLASS_NAME, "title").text

        self.assertEqual('Your Cart', response_data)
        time.sleep(3)

    def test_e_success_logout(self):
        # steps
        browser = self.browser  # buka web browser
        browser.get("https://www.saucedemo.com/")  # buka situs
        time.sleep(2)
        browser.find_element(
            By.ID, "user-name").send_keys("standard_user")  # isi email
        time.sleep(1)
        browser.find_element(By.ID, "password").send_keys(
            "secret_sauce")  # isi password
        time.sleep(1)
        # klik tombol sign in
        browser.find_element(By.ID, "login-button").click()
        time.sleep(1)
        browser.find_element(By.ID, "react-burger-menu-btn").click()
        time.sleep(1)
        browser.find_element(By.ID, "logout_sidebar_link").click()
        time.sleep(1)

        # validasi
        response_data = browser.find_element(
            By.XPATH, '//*[@id="root"]/div/div[1]').text

        self.assertEqual('Swag Labs', response_data)
        time.sleep(3)

    def tearDown(self):
        self.browser.close()


if __name__ == "__main__":
    unittest.main()
