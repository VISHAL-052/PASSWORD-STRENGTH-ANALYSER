from flask import Flask, render_template, request
from analyzer import (
    check_password,
    calculate_entropy,
    is_common_password,
    has_pattern,
    suggest_password
)

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    result = ""
    entropy = ""
    common = False
    pattern = False
    suggestion = ""

    if request.method == "POST":

        password = request.form["password"]

        result = check_password(password)

        entropy = calculate_entropy(password)

        common = is_common_password(password)

        pattern = has_pattern(password)

        suggestion = suggest_password()

    return render_template(
        "index.html",
        result=result,
        entropy=entropy,
        common=common,
        pattern=pattern,
        suggestion=suggestion
    )

if __name__ == "__main__":
    app.run(debug=True)