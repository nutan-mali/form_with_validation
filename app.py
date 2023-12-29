from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Email, Length, Regexp

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

class LeadForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired(), Regexp(r'^[a-zA-Z]+$', message='Only alphabets allowed')])
    email = StringField('Email', validators=[InputRequired(), Email()])
    phone = StringField('Phone Number', validators=[InputRequired(), Regexp(r'^[0-9]{10}$', message='Invalid Indian phone number')])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=6, max=12), Regexp(r'^[a-zA-Z0-9@#$%^&+=]+$', message='Invalid password')])

@app.route('/', methods=['GET', 'POST'])
def lead_form():
    form = LeadForm()

    if form.validate_on_submit():
        # For demonstration purposes, print lead information to the console
        print(f"Name: {form.name.data}")
        print(f"Email: {form.email.data}")
        print(f"Phone Number: {form.phone.data}")
        print(f"Password: {form.password.data}")

       
    return render_template('lead_form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
