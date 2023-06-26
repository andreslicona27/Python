from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
import time


class Anki:
    EMAIL_ACCOUNT = "liconatome27@gmail.com"
    PASSWORD = "Tome2001"
    CURRENT_URL = None
    anki_driver = webdriver.Chrome()
    anki_driver.get("https://ankipro.net")


    def __init__(self, deck, known_words, unknown_words):
        # Manage the waits for the getting elements
        wait = WebDriverWait(self.anki_driver, 5)

        # We give it the value in double "()" because the function is expecting a tuple
        get_started_button = wait.until(EC.presence_of_element_located(
            (By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div[1]/div[4]/div/div/div/div[1]/div[2]/div/a")))
        get_started_button.click()

        # Choosing the type of log in
        email_button = wait.until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div[2]/div[3]/a")))
        email_button.click()

        sign_in_link = wait.until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div[4]/div/a")))
        sign_in_link.click()

        # Email
        email_input = wait.until(EC.presence_of_element_located(
            (By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div[2]/div[1]/input")))
        email_input.send_keys(self.EMAIL_ACCOUNT)

        # Password
        password_input = wait.until(EC.presence_of_element_located(
            (By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/div[2]/div[2]/input")))
        password_input.send_keys(self.PASSWORD)

        enter_button = self.anki_driver.find_element(By.XPATH,
                                                     "/html/body/div[1]/div/div/div/div/div[2]/div/div[4]/div/div")
        enter_button.click()

        # self.CURRENT_URL = self.anki_driver.current_url
        # self.create_new_deck(self.anki_driver.current_url, deck)
        ###############################################################################################################
        #
        # # create_deck_button = self.anki_driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div/div/div[1]/div[3]/div/div/div")
        # create_deck_button = wait.until(EC.presence_of_element_located((By.NAME, "Create new deck")))
        # create_deck_button.click()
        # time.sleep(4)
        # try:
        #     # Adds name
        #     input_name = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[5]/div/div[2]/div/div/div[2]/div/div[3]/div[2]/div/div/div/div[3]/input")))
        #     input_name.send_keys(f"Andres-Licona {deck}")
        #
        #     # Create deck
        #     enter_button = self.anki_driver.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div/div/div[2]/div/div[3]/div[2]/div/div/div/input")
        #     enter_button.click()
        # except StaleElementReferenceException:
        #     print("we succed")
        #     input_name = wait.until(EC.presence_of_element_located(
        #         (By.XPATH, "/html/body/div[5]/div/div[2]/div/div/div[2]/div/div[3]/div[2]/div/div/div/div[3]/input")))
        #     input_name.send_keys(f"Andres-Licona {deck}")

        deck = self.anki_driver.find_element((By.XPATH, "/html/body/div[1]/div/div/div/div/div/div[2]/div/div/div/div/div/div[2]/div/div/div/div[2]"))
        deck.click()

        time.sleep(3)

        add_cards_button = self.anki_driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div")
        add_cards_button.click()

        time.sleep(3)

        front_side = self.anki_driver.find_element(By.XPATH, "/html/body/div[7]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/div[1]/div[2]/div/div/div[1]/div/p")
        back_side = self.anki_driver.find_element(By.XPATH, "/html/body/div[7]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div/p")
        add_word_button = self.anki_driver.find_element(By.XPATH, "/html/body/div[7]/div/div[2]/div/div/div[2]/div/div[1]/div[1]/div[3]/div")
        for known_word, unknown_word in zip(known_words, unknown_words):
            front_side.send_keys(unknown_word)
            back_side.send_keys(known_word)
            add_word_button.click()
            time.sleep(2)


    def create_new_deck(self, site, deck):
        self.anki_driver.get(site)
        create_button_deck = self.anki_driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div/div[1]/div[3]")
        create_button_deck.click()

        # Adds name
        time.sleep(4)
        input_name = self.anki_driver.find_element(By.XPATH, "/html/body/div[5]/div/div[2]/div/div/div[2]/div/div[3]/div[2]/div/div/div/div[3]/input")
        input_name.send_keys(f"Andres-Licona {deck}")

        # Create deck
        enter_button = self.anki_driver.find_element(By.XPATH, "/html/body/div[5]/div/div[2]/div/div/div[2]/div/div[3]/div[2]/div/div/div/input")
        enter_button.click()


    def add_words(self, known_words, unknown_words):
        # TODO verify if the word all ready exist in the deck
        deck = self.anki_driver.find_element((By.XPATH, "/html/body/div[1]/div/div/div/div/div/div[2]/div/div/div/div/div/div[2]/div/div/div/div[2]"))
        deck.click()

        time.sleep(3)

        add_cards_button = self.anki_driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div")
        add_cards_button.click()

        time.sleep(3)

        front_side = self.anki_driver.find_element(By.XPATH, "/html/body/div[7]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/div[1]/div[2]/div/div/div[1]/div/p")
        back_side = self.anki_driver.find_element(By.XPATH, "/html/body/div[7]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div/p")
        add_word_button = self.anki_driver.find_element(By.XPATH, "/html/body/div[7]/div/div[2]/div/div/div[2]/div/div[1]/div[1]/div[3]/div")
        for known_word, unknown_word in zip(known_words, unknown_words):
            front_side.send_keys(unknown_word)
            back_side.send_keys(known_word)
            add_word_button.click()
            time.sleep(2)
        pass
