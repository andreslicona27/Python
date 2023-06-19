from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time



class Anki:
    TWILIO_ACCOUNT_SID = "AC0f1ad169e2f8d71d25da14b2aa4df730"
    TWILIO_AUTH_TOKEN = "a3c3a075a456cf8e7b187b36c129e609"

    def __init__(self):
        anki_driver = webdriver.Chrome()
        anki_driver.get("https://ankipro.net")

        # TODO ADD ALL THE CODE FOR IT TO LOG IN IN THE APP
        # INCLUDING THE VERIFICATION OF APPLE


    def create_new_deck(self, deck):
        pass


    def add_words(self, deck, unknown_words, known_words):
        # TODO verify if the word all ready exist in the deck
        pass
