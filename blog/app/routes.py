from app import app
from flask import render_template
from app.forms import LoginForm
 

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', user=user, posts=posts, title='home')


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', form=form, title='Sign In')




    


