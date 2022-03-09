from multiprocessing.dummy import current_process
from flask import Flask, render_template
import colors_data

app = Flask(__name__)


@app.route('/Homepage')
def homepage():
    colors = colors_data.load_database()
    blue = colors[0]
    red = colors[1]
    green = colors[2]
    yellow = colors[3]
    return render_template("index.html", blue_bg=blue, red_bg=red, green_bg=green, yellow_bg=yellow)


@app.route('/Color/<bg_color>')
def color(bg_color):
    colors = colors_data.load_database()
    current_color = [
        dictionary for dictionary in colors if dictionary["BgColor"] == bg_color]

    return render_template("color.html", background=current_color)


if __name__ == ("__main__"):
    app.run(debug=True, port=6542)
