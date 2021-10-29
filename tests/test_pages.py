from sunspot import app

pages = ['/', '/about', '/application', '/login', '/register', '/bookmarks']

client = app.test_client()

def test_home():
    r = client.get('/')
    assert b'SunSpot - Home' in r.data

def test_about():
    r = client.get('/about')
    assert b'SunSpot - About' in r.data

def test_application():
    r = client.get('/application')
    assert b'SunSpot - App' in r.data

def test_login():
    r = client.get('/login')
    assert b'SunSpot - Login' in r.data

def test_register():
    r = client.get('/register')
    assert b'SunSpot - Register' in r.data

def test_bookmarks():
    r = client.get('/bookmarks')
    assert b'SunSpot - Bookmarks' in r.data