from flask import Flask, render_template, request
import json

app = Flask(__name__)

# Load ingredient database
with open("ingredients.json") as f:
    ingredients_db = json.load(f)

def analyze_ingredients(ingredients, skin_type):
    results = []
    score = 10

    for ingredient in ingredients:
        ing = ingredient.strip().lower()

        if ing in ingredients_db:
            data = ingredients_db[ing]
            risk = data["risk"]

            # scoring logic
            if "clog pores" in risk:
                score -= 2
            elif "irritate" in risk:
                score -= 2
            elif "dry" in risk:
                score -= 1

            warning = None

            if skin_type == "acne" and "clog pores" in risk:
                warning = "⚠ Not recommended for acne-prone skin"

            if skin_type == "sensitive" and "irritate" in risk:
                warning = "⚠ May irritate sensitive skin"

            results.append({
                "name": ing.title(),
                "benefits": data["benefits"],
                "risk": risk,
                "warning": warning
            })

        else:
            results.append({
                "name": ing.title(),
                "benefits": [],
                "risk": "Unknown ingredient",
                "warning": None
            })

    if score < 0:
        score = 0

    return results, score


@app.route("/", methods=["GET", "POST"])
def index():

    results = None
    score = None

    if request.method == "POST":

        ingredients_input = request.form["ingredients"]
        skin_type = request.form["skin_type"]

        ingredients = ingredients_input.split(",")

        results, score = analyze_ingredients(ingredients, skin_type)

    return render_template("index.html",
                           results=results,
                           score=score)


if __name__ == "__main__":
    app.run(debug=True)