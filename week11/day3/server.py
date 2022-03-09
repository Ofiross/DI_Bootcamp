from flask import Flask, render_template

app = Flask(__name__)
articles = [
    {'title': 'somthing',
     'content': 'something2',
     'author': 'somehere'},
    {
        'title': 'somthing',
        'content': 'something2',
        'author': 'somehere'}]


@app.route('/homepage')
def welcome():
    return render_template('homepage.html')


@app.route('/articles')
def articles_list():
    return render_template('articles.html', articles=articles)


if __name__ == "__main__":
    app.run(port=5010)
