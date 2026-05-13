from flask import Flask, render_template, request
from recommend import recommend_movies

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    recommendations = None

    if request.method == "POST":

        user_id = int(request.form["user_id"])

        context = int(request.form["context"])

        recommendations = recommend_movies(
            user_id,
            context
        )

    return render_template(
        "index.html",
        recommendations=recommendations
    )

if __name__ == "__main__":
    app.run(debug=True)