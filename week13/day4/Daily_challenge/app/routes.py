from flask import flash, redirect, render_template, url_for
from app import app, db
from app.forms import Search_person, Search_number
from app.models import Person, Phonenumber


@app.route("/")
def index():
    all_people = Person.query.all()
    return render_template('index.html', people=all_people)


@app.route('/search_phone', methods=['POST', 'GET'])
def number():
    form = Search_number()
    if form.validate_on_submit():
        phone = form.phone_number.data
        all_numbers = Phonenumber.query.all()
        if phone in list(map(lambda number: (number.number), all_numbers)):
            return redirect(url_for("byphone", phone_number=phone))
        else:
            flash('Number not found in phonebook!!!')
    return render_template('search_person.html', form=form)



@app.route('/search_person', methods=['POST', 'GET'])
def person():
    form = Search_person()
    if form.validate_on_submit():
        name = form.name.data
        all_people = Person.query.all()
        if name in list(map(lambda person: (person.name), all_people)):
            return redirect(url_for("byperson", name=name))
        else:
            flash('Could not find this person in phonebook!!!')
    return render_template('search_phone.html', form=form)


@app.route("/person/phone<phone_number>")
def byphone(phone_number):
    person_id = Phonenumber.query.filter_by(number=phone_number).first().master
    person = Person.query.filter_by(id=person_id).first()
    return render_template('person.html', number=phone_number, person_info=person)




@app.route("/person/name<name>")
def byperson(name):
    person = Person.query.filter_by(name=name).first()
    return render_template('number.html', person_info=person, name=name)