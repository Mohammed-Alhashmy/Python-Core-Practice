from flask import Flask, render_template

my_skill = Flask(__name__)



@my_skill.route("/")
def homepage():

    return render_template("homepage.html", pt="Home-Page", )

@my_skill.route("/about")
def about():

    return render_template("aboutpage.html", pt="About-Page", )

@my_skill.route("/myskill")
def myskill():

    return render_template("Test_myskill.html", pt="myskill-page", custom_css="myskill")


if __name__ == "__main__":
    my_skill.run(debug=True)