from flask import render_template, url_for, flash, redirect, request, jsonify
from sunspot import app, bcrypt
from sunspot.forms import RegistrationForm, LoginForm
from sunspot.models import User, Bookmark, DoesNotExist, NotUniqueError
from flask_login import login_user, login_required, current_user, logout_user
import requests

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
        successful_login = False
        
        # Check if there is a user with the entered email address
        try:
            user = User.objects.get(email=email)
        except DoesNotExist:
            flash('Invalid username or password', 'warning')
            return render_template('login.html', title='SunSpot - Login', form=form)
        
        # Check if the password matches
        if bcrypt.check_password_hash(user.password, password) == False:
            flash('Invalid username or password', 'warning')
            return render_template('login.html', title='SunSpot - Login', form=form)
        
        # Login successful
        login_user(user, remember=form.remember.data)
        flash('Logged in successfully!', 'success')
        return redirect(url_for('home'))
        
    return render_template('login.html', title='SunSpot - Login', form=form)

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(email=form.email.data, username=form.username.data, password=hashed_password)
        
        try:
            user.save()
        except NotUniqueError:
            flash(f'Account already exists with email: {form.email.data}', 'danger')
            return render_template('register.html', title='SunSpot - Register', form=form)
        except:
            flash('An error occurred when creating your account', 'danger')
            return render_template('register.html', title='SunSpot - Register', form=form)
        
        flash(f'Account created for {form.username.data}', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html', title='SunSpot - Register', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return render_template('home.html', title='SunSpot - Home')

@app.route('/search')
@login_required
def search():
    return render_template('search.html', title='SunSpot - Search')

@app.route('/bookmarks')
@login_required
def bookmarks():
    return render_template('bookmarks.html', title='SunSpot - Bookmarks')

@app.route('/application')
def application():
    return render_template('application.html', title='SunSpot - Web Application')

@app.route('/api')
@login_required
def api():
    latitude = request.args.get('latitude', type=float)
    longitude = request.args.get('longitude', type=float)

    base_url = 'https://developer.nrel.gov/api/solar/solar_resource/v1'
    params = {
        'format': 'json',
        'api_key': app.config['SOLAR_API_KEY'],
        'lat': latitude,
        'lon': longitude
    }
    r = requests.get(base_url, params=params)

    return r.json()