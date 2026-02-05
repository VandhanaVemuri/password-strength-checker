from flask import Flask, render_template, request
from password_checker import check_strength

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        password = request.form["password"]
        strength, entropy, feedback = check_strength(password)

        result = {
            "strength": strength,
            "entropy": entropy,
            "feedback": feedback
        }

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
