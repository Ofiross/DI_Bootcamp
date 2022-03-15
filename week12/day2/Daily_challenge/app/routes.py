import flask
from flask import redirect, render_template, request, url_for
from app import app
from app.forms import PersonalInfoForm, EducationInfoForm, CareerInfoForm, OtherInfoForm, ProjectsInfoForm
import json

@app.route("/")
def index():
    return flask.render_template('index.html')

@app.route("/Personal")
def personal():
    personal_info = PersonalInfoForm()
    return flask.render_template('personal.html', form=personal_info)

@app.route('/createPersonal', methods = ['POST'])
def personalInfo():
    result = request.form
    with open ('files/cv_data.json', 'r+') as f:
        data = json.load(f)
        data.update(result)
        f.truncate(0)
        f.seek(0)
        json.dump(data, f)
    return redirect(url_for('preview'))

@app.route("/Education")
def education():
    edu = EducationInfoForm()
    return flask.render_template('edu.html', form=edu)

@app.route('/createEducation', methods = ['POST', 'GET'])
def educationInfo():
    result = request.form
    with open ('files/cv_data.json', 'r+') as f:
        data = json.load(f)
        data.update(result)
        f.truncate(0)
        f.seek(0)
        json.dump(data, f)
        return redirect(url_for('preview'))

@app.route("/Career")
def career():
    career = CareerInfoForm()
    return flask.render_template('career.html', form=career)

@app.route('/createCareer', methods = ['POST', 'GET'])
def careerInfo():
    result = request.form
    with open ('files/cv_data.json', 'r+') as f:
        data = json.load(f)
        data.update(result)
        f.truncate(0)
        f.seek(0)
        json.dump(data, f)
        return redirect(url_for('preview'))

@app.route("/Other")
def other():
    other = OtherInfoForm()
    return flask.render_template('other.html', form=other)

@app.route('/createOther', methods = ['POST', 'GET'])
def otherInfo():
    result = request.form
    with open ('files/cv_data.json', 'r+') as f:
        data = json.load(f)
        data.update(result)
        f.truncate(0)
        f.seek(0)
        json.dump(data, f)
        return redirect(url_for('preview'))

@app.route("/Projects")
def projects():
    projects = ProjectsInfoForm()
    return flask.render_template('projects.html', form=projects)

@app.route('/createProjects', methods = ['POST'])
def projectsInfo():
    result = request.form
    with open ('files/cv_data.json', 'r+') as f:
        data = json.load(f)
        data.update(result)
        f.truncate(0)
        f.seek(0)
        json.dump(data, f)
        return redirect(url_for('preview'))


@app.route('/preview')
def preview():
    with open ('files/cv_data.json', 'r') as f:
        data = json.load(f)
    return render_template('preview.html', info=data)

@app.route('/preview_two')
def preview_two():
    with open ('files/cv_data.json', 'r') as file:
        cv_data = json.load(file)
    return render_template('previewTwo.html', info=cv_data)

