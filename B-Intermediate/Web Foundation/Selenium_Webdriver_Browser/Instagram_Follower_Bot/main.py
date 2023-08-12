from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

INSTAGRAM_EMAIL = "***@gmail.com"
INSTAGRAM_PASSWORD = "******"
SIMILAR_ACCOUNT = "chefsteps"


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1024, 600)
        self.driver.maximize_window()
        self.driver.implicitly_wait(0.5)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        # Accepts cookies
        cookies = self.driver.find_element(By.CLASS_NAME, "bIiDR")
        cookies.click()
        time.sleep(1)

        # Adds the email and password
        email = self.driver.find_elements(By.CSS_SELECTOR, "input")
        email[0].send_keys(INSTAGRAM_EMAIL)
        password = email[1]
        password.send_keys(INSTAGRAM_PASSWORD)

        # Tries to log in
        log_in_button = self.driver.find_element(By.CSS_SELECTOR, ".y3zKF")
        log_in_button.click()
        time.sleep(8)

        # Saves the password for future logins
        save_password = self.driver.find_element(By.CSS_SELECTOR, ".yWX7d")
        save_password.click()
        time.sleep(3)

        alerts = self.driver.find_element(By.CSS_SELECTOR, "._a9_1")
        alerts.click()

    def find_followers(self):
        time.sleep(3)
        # Look for an account
        input_text = self.driver.find_element(By.CSS_SELECTOR, "._aauy")
        input_text.send_keys(SIMILAR_ACCOUNT)
        time.sleep(3)

        # To confirm certain action
        input_text.send_keys(Keys.ENTER)
        input_text.send_keys(Keys.ENTER)
        input_text.send_keys(Keys.ENTER)

        try:
            input_text.send_keys(Keys.ENTER)
        except ElementClickInterceptedException:
            pass
        time.sleep(3)

        # Go to the followers section
        followers = self.driver.find_elements(By.CSS_SELECTOR, "._aa_5")
        followers[1].click()

        # Make scroll
        scrolling = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/'
                                                       'div/div/div/div[2]/div/div/div[2]')
        for i in range(5):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrolling)
            time.sleep(2)

    def follow(self):
        # Gets all the buttons
        all_follows = self.driver.find_elements(By.CSS_SELECTOR, "._acas")

        # For each button in sees the text and follows the ones that are still not following
        for follow_button in all_follows:
            time.sleep(1)
            if follow_button.text == "Following" or follow_button.text == "Requested":
                print("Already following")
            else:
                follow_button.click()


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
