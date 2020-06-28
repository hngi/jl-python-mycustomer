from flask import jsonify, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from config import db, bcrypt
from models.user import User
from endpoints.auth.forms import RegistrationForm, LoginForm


@users.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        auth = "You don't need to register you're authenticated"
        return jsonify(auth)
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        g = "login page"
        n = "Register again"
        return jsonify(g)
    return jsonify(n)


@users.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            a = "homepage"
            return jsonify(a)
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
            d = "Please check again"
    return jsonify(d)


@users.route("/logout")
def logout():
    logout_user()
    v = "You logout "
    return jsonify(v)



