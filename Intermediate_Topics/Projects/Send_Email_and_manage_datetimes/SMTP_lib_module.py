import smtplib
import datetime as dt

# --------------------------- SMTP ------------------------ #
# SMTP Simple Mail Transfer Protocol
# SMTP information
# gmail = smtp.gmail.com
# hotmail = smtp.live.com
# yahoo = smtp.mail.yahoo.com

my_email = "andreslicona27@gmail.com"
password = "alexander2001"
# Generate a new app password
# for it to work, go to gmail security and generate another way of verification and past here the password

with smtplib.SMTP("smtp.google.com") as connection:
    connection.starttls()  # makes the connection secure
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="testing@yahoo.com",
                        msg="Subject:Hello\n\nThis is the body of my email")

# connection.close() by adding the automatic close you can get rid of this line


# --------------------------- Date Time ------------------------ #

now = dt.datetime.now()  # get current date and time
year = now.year
month = now.month
day_of_Week = now.weekday()  # return a number

date_of_birth = dt.datetime(year=2001, month=6, days=27, hour=3)


