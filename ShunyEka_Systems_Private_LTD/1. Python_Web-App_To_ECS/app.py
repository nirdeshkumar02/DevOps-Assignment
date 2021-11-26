from flask import Flask, render_template
import os
import random

app = Flask(__name__)

# list of Hello World images
images = [
    "https://i.giphy.com/media/h408T6Y5GfmXBKW62l/giphy.webp",
    "https://i.giphy.com/media/1Rj3Q1yvQDFU74otiA/giphy.webp",
    "https://i.giphy.com/media/HEURGne9Vj856oivkD/giphy.webp"
]


@app.route("/")
def index():
    url = random.choice(images)
    return render_template("index.html", url=url)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
