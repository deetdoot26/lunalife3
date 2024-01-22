from flask import Flask, render_template

app = Flask(__name__)

# Sample data for demonstration purposes
chat_rooms = [
    {"id": 1, "name": "General Chat"},
    {"id": 2, "name": "Menstrual Health Support"},
    {"id": 3, "name": "Menopause Discussions"},
]

articles = [
    {"id": 1, "title": "Understanding Menopause", "content": "Article content goes here."},
]

product_recommendations = [
    {"id": 1, "name": "Menstrual Cup", "rating": 5},
]

@app.route("/")
def index():
    return render_template("index_basic.html", chat_rooms=chat_rooms, articles=articles, products=product_recommendations)

if __name__ == "__main__":
    app.run(debug=True)
