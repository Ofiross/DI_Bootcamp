import markdown
from flask import Flask, render_template
import markdown.extensions.fenced_code

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/lesson')
def lesson():
    readme_file = open("in-this-chapter.md", "r")
    exercise_template = markdown.markdown(
        readme_file.read(), extensions=["fenced_code"]
    )

    return exercise_template


@app.route('/exercise')
def exercise():
    with open("exercise.md", "r", encoding="utf-8") as input_file:
        text = input_file.read()
    html = markdown.markdown(text)

    return html


if __name__ == "__main__":
    app.run(port=5010)
