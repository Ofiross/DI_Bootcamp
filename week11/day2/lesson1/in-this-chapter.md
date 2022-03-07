# Routing
## Table Of Contents
* What You Will Learn
    * URL Converters
    * flask.url_for
    * flask.redirect
    * More on url_for
    * Feedbacks
---
## What You Will Learn
* Routing
* url_for
* redirect
---
## URL Converters

When you define a route in Flask, you can specify parts of it that will be converted into Python variables and passed to the view function.
```
@app.route('/user/<username>')
def profile(username):
    pass
```
Whatever is in the part of the URL labeled will get passed to the view as the username argument. You can also specify a converter to filter the variable before it’s passed to the view.
```
@app.route('/user/id/<int:user_id>')
def profile(user_id):
    pass
```
In this code block, the URL http://myapp.com/user/id/hello will return a 404 status code – not found. This is because the part of the URL that is supposed to be an integer is actually a string.

---

## Flask.Url_for
<mark>flask.url_for</mark> is a flask function that return the url mapped with a given view. Thus if you change the name of the url in the route decorator of the function, you don’t have to change it in every line of code.

<mark>url_for</mark> can also be used in templates.

<strong>Example (create a button that redirect to index):</strong>

```
<a href="/index"> Index </a>                    // Wrong usage

<a href={{ url_for('index_func') }}> Index </a> // Right usage
```
For more on <mark>url_for</mark>, [see here](https://flask.palletsprojects.com/en/1.0.x/api/#flask.url_for)

---

## Flask.Redirect
<mark>flask.redirect</mark> function return a response that redirect to another url, you can use it with <mark>url_for</mark>.Example of a view that redirect to the index:__

```
import flask

@app.route("/home")
def index():
    return "Hello Everyone"

@app.route("/nowhere")
def redirecting_view():
    return flask.redirect(flask.url_for('index')) # Redirect the user to the /home route
```
---

## More On Url_for
To build a URL to a specific function, use the url_for() function. It accepts the name of the function as its first argument and any number of keyword arguments, each corresponding to a variable part of the URL rule. Unknown variable parts are appended to the URL as query parameters.

Why would you want to build URLs using the URL reversing function
<mark>url_for()</mark> instead of hard-coding them into your templates?

* Reversing is often more descriptive than hard-coding the URLs.
* You can change your URLs in one go instead of needing to remember to manually change hard-coded URLs.
* URL building handles escaping of special characters and Unicode data transparently.
* The generated paths are always absolute, avoiding unexpected behavior of relative paths in browsers.
* If your application is placed outside the URL root, for example, in /myapplication instead of /, url_for()properly handles that for you.

For example, here we use the test_request_context() method to try out url_for(). test_request_context() tells Flask to behave as though it’s handling a request even while we use a Python shell. See Context Locals.
```
from flask import Flask, escape, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return 'indexPage'

@app.route('/login')
def login():
    return 'loginPage'

@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(escape(username))

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))

# >> In the terminal
/                                                                           
/loginPage                                                                  
/loginPage?next=%2F                                                         
/user/John%20Doe  
```

---
## <strong><font color="green">Exercise</font></strong>
<p style="color:blue">
<font color="green"> Create a template called homepage.html
Create a route called blog, that welcomes your users (use the template homepage.html)
Create a template called articles.html
Create a route called blog/articles, that display a list of articles inside the articles.html. This list must be a dictionnary with some keys (title, content, author) and values. This dictionary must be passed from the route, to the template file
Add a button "Go back to homepage" to the template articles.html, that redirects the user to the /blog route.
Create a new route called profile. The developer didn't finish this route, so instead of giving an error to the user, redirect him to the /blog route
Run your app

---