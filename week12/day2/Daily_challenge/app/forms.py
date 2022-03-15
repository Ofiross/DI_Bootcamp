from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length, Email
from wtforms.widgets import TextArea, RangeInput

class PersonalInfoForm(FlaskForm):
    firstName = StringField('First Name', validators=[DataRequired(), Length(min=2, max=20)])
    lastName = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=20)])
    birthDay = IntegerField('Birth Day', validators=[DataRequired(), Length(min=1, max=2)])
    birthMonth = IntegerField('Birth Month', validators=[DataRequired(), Length(min=1, max=2)])
    birthYear = IntegerField('Birth Year', validators=[DataRequired(), Length(min=4, max=4)])
    description = StringField('description', validators=[DataRequired(), Length(min=4, max=15)])
    address = StringField('description', validators=[DataRequired(), Length(min=4, max=15)])
    city = StringField('description', validators=[DataRequired(), Length(min=4, max=15)])
    zip = StringField('description', validators=[DataRequired(), Length(min=4, max=15)])
    country = StringField('description', validators=[DataRequired(), Length(min=4, max=15)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone Number', validators=[DataRequired(), Length(min=9, max=12)])
    submit = SubmitField('Submit')

class EducationInfoForm(FlaskForm):

    institute_name = StringField('institute', validators=[DataRequired(), Length(min=4, max=25)])
    education = StringField('Education', validators=[DataRequired(), Length(min=4, max=25)])
    education_start = IntegerField('Start year', validators=[DataRequired(), Length(min=4, max=4)])
    education_end =  IntegerField('End year', validators=[DataRequired(), Length(min=4, max=4)])
    education_info = StringField(u'Text', widget=TextArea(), validators=[DataRequired(), Length(min=10, max=150)])
    
    institute2_name = StringField('institute', validators=[Length(min=4, max=25)])
    education2 = StringField('Education2 Optional', validators=[Length(min=4, max=25)])
    education2_start = IntegerField('Start year', validators=[Length(min=4, max=4)])
    education2_end =  IntegerField('End year', validators=[Length(min=4, max=4)])
    education2_info = StringField(u'Text', widget=TextArea(), validators=[Length(min=10, max=150)])

    institute3_name = StringField('institute', validators=[Length(min=4, max=25)])
    education3 = StringField('Education3 Optional', validators=[Length(min=4, max=25)])
    education3_start = IntegerField('Start year', validators=[Length(min=4, max=4)])
    education3_end =  IntegerField('End year', validators=[Length(min=4, max=4)])
    education3_info = StringField(u'Text', widget=TextArea(), validators=[Length(min=10, max=150)])

    language = StringField('language', validators=[Length(min=4, max=10)])
    language_level =  IntegerField('level', validators=[Length(min=1, max=1)])
    language2 = StringField('language', validators=[Length(min=4, max=10)])
    language2_level =  IntegerField('level', validators=[Length(min=1, max=1)])
    language3 = StringField('language', validators=[Length(min=4, max=10)])
    language3_level =  IntegerField('level', validators=[Length(min=1, max=1)])
    language4 = StringField('language', validators=[Length(min=4, max=10)])
    language4_level =  IntegerField('level', validators=[Length(min=1, max=1)])

    submit = SubmitField('Submit')

class CareerInfoForm(FlaskForm):
    work = StringField('Work Experience', validators=[DataRequired(), Length(min=4, max=25)])
    work_title = StringField('Job Title', validators=[DataRequired(), Length(min=4, max=25)])
    work_start = IntegerField('Start year', validators=[DataRequired(), Length(min=4, max=4)])
    work_end =  IntegerField('End year', validators=[Length(min=4, max=4)])
    work_info = StringField(u'Text', widget=TextArea(), validators=[DataRequired(), Length(min=10, max=150)])

    work2 = StringField('Work2 Experience', validators=[Length(min=4, max=25)])
    work2_title = StringField('Job Title', validators=[Length(min=4, max=25)])
    work2_start = IntegerField('Start year', validators=[Length(min=4, max=4)])
    work2_end =  IntegerField('End year', validators=[Length(min=4, max=4)])
    work2_info = StringField(u'Text', widget=TextArea(), validators=[Length(min=10, max=150)])

    work3 = StringField('Work3 Experience', validators=[Length(min=4, max=25)])
    work3_title = StringField('Job Title', validators=[Length(min=4, max=25)])
    work3_start = IntegerField('Start year', validators=[Length(min=4, max=4)])
    work3_end =  IntegerField('End year', validators=[Length(min=4, max=4)])
    work3_info = StringField(u'Text', widget=TextArea(), validators=[Length(min=10, max=150)])

    career_sum = StringField(u'Text', widget=TextArea(), validators=[Length(min=10, max=150)])

    submit = SubmitField('Submit')

class OtherInfoForm(FlaskForm):
    skill = StringField('Skills', validators=[DataRequired(), Length(min=3, max=15)])
    skill_level = IntegerField('Level', widget=RangeInput(step=10), validators=[DataRequired(), Length(min=10, max=100)])
    
    skill2 = StringField('Skills', validators=[Length(min=3, max=15)])
    skill2_level = IntegerField('Level', widget=RangeInput(step=10), validators=[DataRequired(), Length(min=10, max=100)])
    
    skill3 = StringField('Skills', validators=[Length(min=3, max=15)])
    skill3_level = IntegerField('Level', widget=RangeInput(step=10), validators=[DataRequired(), Length(min=10, max=100)])
    
    skill4 = StringField('Skills', validators=[Length(min=3, max=15)])
    skill4_level = IntegerField('Level', widget=RangeInput(step=10), validators=[DataRequired(), Length(min=10, max=100)])
    
    skill5 = StringField('Skills', validators=[Length(min=3, max=15)])
    skill5_level = IntegerField('Level', widget=RangeInput(step=10), validators=[DataRequired(), Length(min=10, max=100)])

    hobbies = StringField('Hobbies', validators=[Length(min=3, max=15)])
    hobbies2 = StringField('Hobbies', validators=[Length(min=3, max=15)])
    hobbies3 = StringField('Hobbies', validators=[Length(min=3, max=15)])
    hobbies4 = StringField('Hobbies', validators=[Length(min=3, max=15)])
    hobbies5 = StringField('Hobbies', validators=[Length(min=3, max=15)])

    other = StringField('Other Contact Information', widget=TextArea() ,validators=[ Length(min=1, max=150)])

    submit = SubmitField('Submit')

class ProjectsInfoForm(FlaskForm):
    project = StringField('Hobbies', validators=[Length(min=3, max=15)])
    project_info = StringField(u'Text', widget=TextArea(), validators=[Length(min=10, max=150)])

    project2 = StringField('Hobbies', validators=[Length(min=3, max=15)])
    project2_info = StringField(u'Text', widget=TextArea(), validators=[Length(min=10, max=150)])
    
    project3 = StringField('Hobbies', validators=[Length(min=3, max=15)])
    project3_info = StringField(u'Text', widget=TextArea(), validators=[Length(min=10, max=150)])
    
    project4 = StringField('Hobbies', validators=[Length(min=3, max=15)])
    project4_info = StringField(u'Text', widget=TextArea(), validators=[Length(min=10, max=150)])

    submit = SubmitField('Submit')