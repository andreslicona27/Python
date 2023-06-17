# Jinja in a render template created for python


from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)


@app.route('/')
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.datetime.now().year
    return render_template("index.html", num=random_number, year=current_year)


@app.route("/guess/<person_name>")
def guess(person_name):
    gender_url = f"https://api.genderize.io?name={person_name}"
    gender_response = requests.get(gender_url)
    gender_data = gender_response.json()
    gender = gender_data["gender"]

    age_url = f"https://api.agify.io?name={person_name}"
    age_response = requests.get(age_url)
    age_data = age_response.json()
    age = age_data["age"]

    return render_template("guess.html", name=person_name, gender=gender, age=age)


@app.route("/blog/<number>")
def get_blog(number):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_post = response.json()
    return render_template("blog.html", posts=all_post)


if __name__ == "__main__":
    app.run(debug=True)
