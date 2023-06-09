import smtplib
from bs4 import BeautifulSoup
import requests

BUY_PRICE = 15.99
MY_EMAIL = "andreslicona27@gmail.com"
url = "https://www.amazon.es/Olympians-Children-Collection-Lightning-Labyrinth/dp/9124369225/?_encoding=UTF8&pd_rd_w=Nf7IL&content-id=amzn1.sym.8ddafe99-0303-437a-a80e-e4e34a8db807&pf_rd_p=8ddafe99-0303-437a-a80e-e4e34a8db807&pf_rd_r=CEG86BG3VH5NGWRY925G&pd_rd_wg=VY76M&pd_rd_r=0c9063e3-e10a-4421-9798-fe3a7969af36&ref_=pd_gw_ci_mcx_mr_hp_atf_m"

# Make the petition to the web
response = requests.get(url)
response.raise_for_status()  # Sees ir there was any problem with the petition

soup = BeautifulSoup(response.text, "html.parser")

# Obtains the title of the product
title = soup.find(id="productTitle").get_text().strip()
print(title)

# Obtains the price of the product
price = soup.find(id="priceblock_ourprice").get_text()
price = float(price.replace("€", "").replace(",", "."))

if price < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(MY_EMAIL, "alexander2001")
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
        )
