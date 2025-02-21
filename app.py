from flask import Flask, render_template, request, make_response, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Replace with a strong, randomly generated secret key

# In-memory storage (replace with a database for persistence)
user_data = {}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        resp = make_response(redirect(url_for("drill")))
        resp.set_cookie("name", name)
        return resp
    return render_template("index.html")


@app.route("/drill", methods=["GET", "POST"])
def drill():
    name = request.cookies.get("name")
    if name is None:
        return redirect(url_for("index"))

    if name not in user_data:
        user_data[name] = {"correct": 0, "incorrect": 0}

    if request.method == "POST":
        answer = int(request.form["answer"])
        num1 = int(request.form["num1"])
        num2 = int(request.form["num2"])
        correct_answer = num1 * num2

        if answer == correct_answer:
            user_data[name]["correct"] += 1
        else:
            user_data[name]["incorrect"] += 1

        return render_template("results.html",
                               name=name,
                               correct=user_data[name]["correct"],
                               incorrect=user_data[name]["incorrect"],
                               answer=answer,
                               correct_answer=correct_answer,
                               num1=num1,
                               num2=num2)

    num1 = random.randint(1, 12)
    num2 = random.randint(1, 12)
    return render_template("drill.html",
                           name=name,
                           correct=user_data[name]["correct"],
                           incorrect=user_data[name]["incorrect"],
                           num1=num1,
                           num2=num2)



if __name__ == "__main__":
    app.run(debug=True)

