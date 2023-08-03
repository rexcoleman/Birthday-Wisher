from datetime import datetime
import pandas
import random
import smtplib
import os

MY_EMAIL = "rexdevtext@gmail.com"
MY_PASSWORD_ = os.environ.get('MY_PASSWORD_')
MY_PORT = os.environ.get('MY_PORT')

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
# print(birthdays_dict)

if today_tuple in birthdays_dict:
    print("yes")
    birthday_person = birthdays_dict[(today_tuple)]
    print(birthday_person)
    print(type(birthday_person))
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    print(file_path)
    with open(file_path) as letter_file:
        contents = letter_file.read()
        print(contents)
        contents = contents.replace("[NAME]", birthday_person["name"])
        print(contents)

    with smtplib.SMTP("smtp.gmail.com", port=int(MY_PORT)) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD_)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday\n\n{contents}"
        )
    connection.close()


    # with smtplib.SMTP("smtp.gmail.com", port=587) as connection: