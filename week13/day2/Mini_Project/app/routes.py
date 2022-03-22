from flask import flash, redirect, render_template, url_for
from app import app, db
from app.models import User
from app.forms import New_user, Login

@app.route("/")
def index():
    all_users = User.query.all()
    users_lives_in = User.query.filter_by(city="Roscoeview")
    first_five = User.query.limit(5).all()
    zip_start_five = User.query.filter(User.zipcode.startswith('5'))
    return render_template('index.html', users=all_users, city=users_lives_in, zip=zip_start_five, first_five=first_five)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = Login()
    if form.validate_on_submit():
        name = form.name.data
        city = form.city.data
        all_users = User.query.all()
        if (name, city) in list(map(lambda person: (person.name, person.city), all_users)):
            flash('You are logged in.')
        else:
            flash('You need to sign up first')
            return redirect(url_for('add_user'))
    return render_template('login.html', form=form)




@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    form = New_user()
    if form.validate_on_submit():
        new_person = User(name=form.name.data,
                        street=form.street.data,
                        city=form.city.data,
                        zipcode=form.zipcode.data)
        db.session.add(new_person)
        db.session.commit()
        render_template('index.html')
    return render_template('add_user.html', form=form)
