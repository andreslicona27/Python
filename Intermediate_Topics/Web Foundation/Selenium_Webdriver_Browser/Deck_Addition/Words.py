from selenium import webdriver
from selenium.webdriver.common.by import By


class Words:
    def __init__(self, site):
        # Site where the words come from
        self.words_driver = webdriver.Chrome()
        self.words_driver.get(site)

        self.unknown_words = []
        self.known_words = []

    def get_words(self):
        # Get the words into two different arrays
        td_elements = self.words_driver.find_elements(By.TAG_NAME, "td")
        del td_elements[:3]  # Delete header
        cont = 0
        for index, td in enumerate(td_elements):
            if cont == 3:
                cont = 0

            if cont == 1:
                self.unknown_words.append(td.text)
            if cont == 2:
                self.known_words.append(td.text)

            cont += 1

    def show_words(self):
        for word in self.unknown_words:
            print(word)

        for word in self.known_words:
            print(word)
