import smtplib
import datetime as dt
import random

my_email = "andreslicona27@gmail.com"
password = "alexander2001"
now = dt.datetime.now()
weekday = now.weekday()

if weekday == 1:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readline()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )
