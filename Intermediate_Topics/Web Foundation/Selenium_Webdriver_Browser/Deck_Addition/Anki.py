from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class Anki:
    EMAIL_ACCOUNT = "andreslicona27@icloud.com"
    PASSWORD = "Aalt2001"

    def __init__(self):
        self.anki_driver = webdriver.Chrome()
        self.anki_driver.get("https://ankipro.net")

        # The handles that switch windows
        window_handles = self.anki_driver.window_handles
        # Time that the code is going to wait
        wait = WebDriverWait(self.anki_driver, 4)

        # TODO ADD ALL THE CODE FOR IT TO LOG IN IN THE APP
        # We give it the value in double "()" because the function is expecting a tuple
        get_started_button = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div[1]/div[4]/div/div/div/div[1]/div[2]/div/a")))
        get_started_button.click()

        apple_button = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div[2]")))
        apple_button.click()

        # We save the current window
        main_window = self.anki_driver.current_window_handle

        # APPLE LOG IN
        # We change the window
        self.anki_driver.switch_to.window(window_handles[-1])

        # Email
        email_input = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/oauth-init/div[1]/div/oauth-signin/div/apple-auth/div/div[1]/div/sign-in/div/div[1]/div[1]/div/div/div[1]/div/div/input")))
        email_input.send_keys(self.EMAIL_ACCOUNT)

        enter_button = self.anki_driver.find_element(By.ID, "sign-in")
        enter_button.click()

        # Password
        password_input = wait.until(EC.presence_of_element_located((By.ID, "password_text_field")))
        password_input.send_keys(self.PASSWORD)

        enter_button.click()

        self.anki_driver.switch_to.window(main_window)

        continue_button = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/oauth-init/div[1]/div/oauth-profile/div/div/idms-step/div/div/div/div[3]/idms-toolbar/div/div/div/button[1]")))
        continue_button.click()


    def create_new_deck(self, deck):
        pass


    def add_words(self, deck, unknown_words, known_words):
        # TODO verify if the word all ready exist in the deck
        pass
