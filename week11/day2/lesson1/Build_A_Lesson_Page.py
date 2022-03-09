import markdown
from flask import Flask, render_template
import markdown.extensions.fenced_code

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/lesson')
def lesson():
    with open("in-this-chapter.md", "r", encoding="utf-8") as input_file:
        text = input_file.read()
    lesson_html = markdown.markdown(text)

    return lesson_html


@app.route('/exercise')
def exercise():
    with open("exercise.md", "r", encoding="utf-8") as input_file:
        text = input_file.read()
    exercise_html = markdown.markdown(text)

    return exercise_html


if __name__ == "__main__":
    app.run(port=5010)
