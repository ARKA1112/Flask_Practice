#Home page route

from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Arka'}
    return '''
<html>
    <head>
        <title>Home Page - Microblog</title>
    </head>
    <body>
        <h1>Hello, ''' + user['username'] + '''!</h1>
        <a href="http://www.google.in">Google_in</a>
    </body>
</html>'''