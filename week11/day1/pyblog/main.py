import flask

app = flask.Flask(__name__)

users = ['Bob', 'Alice']
art = ['art1', 'art2']


@app.route('/blog')
def greeting_users():
    for name in users:
        return f"Welcome {name}"


@app.route('/article')
def showing_art():
    for article in art:
        return f"Article: {article}"


@app.route('/sayBye/<name>')
def say_bye(name):
    return f'''
    <html>
        <head>
            <title>Students Platform</title>
        </head>
        <body>
            <h1>Hello, to all of our users {i for i in users}!</h1>
            <h1>thank!</h1>
        </body>
    </html>'''


if __name__ == "__main__":
    app.run(debug=True, port=5000)
