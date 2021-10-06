from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('homePage.html', title='Home')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login')
def login():
    return "This is the login page"

@app.route('/app')
def app():
    return "This is the app page"

if __name__ == '__main__':
    app.run(debug=True)