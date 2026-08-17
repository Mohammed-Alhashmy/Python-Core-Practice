from flask import Flask, render_template

mylist=[("Python", 70), ("Html", 40), ("CSS", 23)]


my_skill = Flask(__name__)

@my_skill.route("/")
def homepage():

    return render_template("homepage.html", pt="Home-Page", )

@my_skill.route("/about")
def about():

    return render_template("aboutpage.html", pt="About-Page", )

@my_skill.route("/add")
def add():

    return render_template("Test_myskill.html", 
                           pt="myskill-page", 
                           custom_css="myskill")

@my_skill.route("/myskills")
def addskills():

    return render_template("myskills.html", 
                           pt="Skills-Page",
                           custom_css1="skill_page",
                           page_head="My Skills", 
                           description="Here is my skills page ",
                           myData=mylist)


if __name__ == "__main__":
    my_skill.run(debug=True)