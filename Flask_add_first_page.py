from flask import Flask

my_skill = Flask(__name__)



@my_skill.route("/")
def homepage():

    return("Hello To Our Page")

@my_skill.route("/about")
def about():

    return("This Is My Testing Page .")

if __name__ == "__main__":
    my_skill.run(debug=True)