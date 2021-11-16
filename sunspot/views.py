from flask import render_template, url_for, flash, redirect
from sunspot import app, bcrypt
from sunspot.forms import RegistrationForm, LoginForm
from sunspot.models import User, Bookmark

@app.route('/')
def home():
    return render_template('home.html', title='SunSpot - Home')

@app.route('/about')
def about():
    return render_template('about.html', title='SunSpot - About')

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        password = form.password.data
        email = form.email.data
        
        # Get the user from the DB with the entered email address
        # test
        email_users = User.objects(email=email)
        password_match = False
        for email_user in email_users:
            if email_user != None:
                password_match = bcrypt.check_password_hash(email_user.password, password)
            elif password_match == False:
                flash('Invalid username or password')
                return render_template('login.html', title='SunSpot - Login', form=form)
        
        return redirect(url_for('home'))
        
    return render_template('login.html', title='SunSpot - Login', form=form)

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(email=form.email.data, username=form.username.data, password=hashed_password)
        user.save()
        flash(f'Account created for {form.username.data}', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html', title='SunSpot - Register', form=form)

@app.route('/search')
def search():
    return render_template('search.html', title='SunSpot - Search')

@app.route('/bookmarks')
def bookmarks():
    return render_template('bookmarks.html', title='SunSpot - Bookmarks')

@app.route('/application')
def application():
    return render_template('application.html', title='SunSpot - Web Application')

