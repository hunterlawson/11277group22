from flask import render_template
from sunspot import app
from sunspot.forms import RegistrationForm, LoginForm

@app.route('/')
def home():
    return render_template('home.html', title='SunSpot - Home')

@app.route('/about')
def about():
    return render_template('about.html', title='SunSpot - About')

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    return render_template('login.html', title='SunSpot - Login', form=form)

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    return render_template('register.html', title='SunSpot - Register', form=form)

@app.route('/application')
def application():
    return render_template('application.html', title='SunSpot - App')

@app.route('/bookmarks')
def bookmarks():
    return render_template('bookmarks.html', title='SunSpot - Bookmarks')
