from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

INTERNET_PROMISED_DOWNLOAD = 100
INTERNET_PROMISED_UPLOAD = 15
TWITTER_EMAIL = ""
TWITTER_PASSWORD = ""
SPEED_TEST_URL = "https://www.speedtest.net/"
TWITTER_URL = "https://twitter.com/i/flow/login"


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.up = 10
        self.down = 2

    def get_internet_speed(self):
        self.driver.get(url=SPEED_TEST_URL)
        sleep(5)
        start_button = self.driver.find_element(by="css selector", value="a.js-start-test.test-mode-multi span.start-text")
        start_button.click()
        sleep(60)
        self.down = float(self.driver.find_element(by="css selector", value="span.result-data-large.number.result-data-value.download-speed").text)
        print("Down", self.down)
        self.up = float(self.driver.find_element(by="css selector", value="span.result-data-large.number.result-data-value.upload-speed").text)
        print(f"Up : {self.up}")
        self.driver.quit()

    def tweet_at_provider(self):
        self.driver.get(url=TWITTER_URL)
        sleep(60)

        email_button = self.driver.find_element(by="xpath", value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        email_button.send_keys(TWITTER_EMAIL)
        next_button = self.driver.find_element("css selector","#layers > div > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div.css-1dbjc4n.r-kemksi.r-6koalj.r-16y2uox.r-1wbh5a2 > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div > div > div > div:nth-child(6) > div")
        next_button.click()
        sleep(20)

        password_button = self.driver.find_element("css selector","#layers > div > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div.css-1dbjc4n.r-kemksi.r-6koalj.r-16y2uox.r-1wbh5a2 > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1dqxon3 > div > div > div.css-1dbjc4n.r-mk0yit.r-13qz1uu > div > label > div > div.css-1dbjc4n.r-18u37iz.r-16y2uox.r-1wbh5a2.r-1wzrnnt.r-1udh08x.r-xd6kpl.r-1pn2ns4.r-ttdzmv > div.css-901oao.r-1awozwy.r-6koalj.r-1qd0xha.r-1inkyih.r-16dba41.r-135wba7.r-bcqeeo.r-13qz1uu.r-qvutc0 > input")
        password_button.send_keys(TWITTER_PASSWORD)
        sleep(3)

        login = self.driver.find_element("css selector","#layers > div > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div.css-1dbjc4n.r-kemksi.r-6koalj.r-16y2uox.r-1wbh5a2 > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div.css-1dbjc4n.r-1isdzm1 > div > div.css-1dbjc4n > div > div > div > div")
        login.click()
        sleep(5)

        write_message = self.driver.find_element("css selector","#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div > div > div.css-1dbjc4n.r-kemksi.r-184en5c > div > div.css-1dbjc4n.r-kemksi.r-oyd9sg > div:nth-child(1) > div > div > div > div.css-1dbjc4n.r-1iusvr4.r-16y2uox.r-1777fci.r-1h8ys4a.r-1bylmt5.r-13tjlyg.r-7qyjyx.r-1ftll1t > div.css-1dbjc4n.r-184en5c > div > div > div > div > div > div.css-1dbjc4n.r-16y2uox.r-bnwqim.r-13qz1uu.r-1g40b8q > div > div > div > div > label > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2 > div > div > div > div > div > div.DraftEditor-editorContainer > div > div > div > div")
        write_message.send_keys(f"just a test {self.up}: {self.down}")
        sleep(2)

        tweet = self.driver.find_element("css selector","#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div > div > div.css-1dbjc4n.r-kemksi.r-184en5c > div > div.css-1dbjc4n.r-kemksi.r-oyd9sg > div:nth-child(1) > div > div > div > div.css-1dbjc4n.r-1iusvr4.r-16y2uox.r-1777fci.r-1h8ys4a.r-1bylmt5.r-13tjlyg.r-7qyjyx.r-1ftll1t > div:nth-child(3) > div > div > div:nth-child(2) > div.css-18t94o4.css-1dbjc4n.r-l5o3uw.r-42olwf.r-sdzlij.r-1phboty.r-rs99b7.r-19u6a5r.r-2yi16.r-1qi8awa.r-1ny4l3l.r-ymttw5.r-o7ynqc.r-6416eg.r-lrvibr > div > span > span")
        tweet.click()

auto_complaining_boot = InternetSpeedTwitterBot()
auto_complaining_boot.get_internet_speed()
auto_complaining_boot.tweet_at_provider()