from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, lm
from forms import LoginForm, EditForm, RegistrationForm
from models import User, ROLE_USER, ROLE_ADMIN
from datetime import datetime


@lm.user_loader
def load_user(id):
    return User.query.get(id)

# @app.before_request
# def load_user():
#     if session["user_id"]:
#         user = User.query.filter_by(username=session["user_id"]).first()
#     else:
#         user = {"name": "Guest"}  # Make it better, use an anonymous User instead

#     g.user = user

@app.route('/')
@app.route('/index')
def index():
    # user = g.user
    posts = [
        { 
            'author': { 'username': 'John' }, 
            'body': 'This is a Dummy post!' 
        },
        { 
            'author': { 'username': 'Susan' }, 
            'body': 'Thi is a Dummy post too!!' 
        }
    ]
    return render_template('index.html',
        title = 'Home',
        user = 'ashok',
        posts = posts)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        flash('creating')
        user = User(username=form.username.data,email=form.email.data,password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Thanks for registering')
        return redirect(url_for('about'))
    return render_template('register.html', form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    # if g.user is not None and g.user.is_authenticated():
    #     return redirect(url_for('index'))
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(username=request.form['username']).first()
        if not user:
            flash('Invalid username')
        elif not user.check_password(request.form['password']):
            flash('Invalid password')
        else:
            session['user_id'] = user.id  # makes more sense than storing just a bool
            flash("Logged in successfully.")
            return redirect(request.args.get("next") or url_for("index"))
    return render_template("login.html", form=form)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('show_entries'))

@app.errorhandler(404)
def internal_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500
###################

@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username = username).first()
    if user == None:
        flash('User' + username + ' not found.')
        return redirect(url_for('index'))
    flash('found something' + user.username)
    posts = [
        { 'author': user, 'body': 'Dummy post #1' },
        { 'author': user, 'body': 'Dummy post #2' }
    ]
    return render_template('user.html',
        user = user,
        posts = posts)


@app.route('/edit', methods = ['GET', 'POST'])
#@login_required
def edit():
    form = EditForm()
    if request.method == 'POST' and form.validate():
        g.user.username = form.username.data
        g.user.about_me = form.about_me.data
        g.user.password = form.password.data
        db.session.add(g.user)
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('edit'))
    else:
        form.username.data = g.user.username
        form.about_me.data = g.user.about_me
    return render_template('edit.html',
        form = form)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

