from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', title='SunSpot - Home')

@app.route('/about')
def about():
    return render_template('about.html', title='SunSpot - About')

@app.route('/login')
def login():
    return render_template('login.html', title='SunSpot - Login')

@app.route('/application')
def application():
    return render_template('application.html', title='SunSpot - App')

@app.route('/bookmarks')
def bookmarks():
    return render_template('bookmarks.html', title='SunSpot - Bookmarks')

if __name__ == '__main__':
    app.run(debug=True)