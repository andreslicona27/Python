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
        td_elements = td_elements[3:]  # Exclude header rows

        for index, td in enumerate(td_elements):
            if index % 3 == 1:
                self.unknown_words.append(td.text)
            elif index % 3 == 2:
                self.known_words.append(td.text)

        self.words_driver.quit()

    def show_words(self):
        for word in self.unknown_words:
            print(word)

        for word in self.known_words:
            print(word)
