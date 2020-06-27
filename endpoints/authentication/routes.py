from flask import jsonify, url_for, flash, redirect, request
from flask_login import login_user, current_user, logout_user, login_required
from endpoints import db, bcrypt
from models.register import User
from endpoints.authentication.form import RegistrationForm, LoginForm


@users.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        a = "it is authenticated"
        return jsonify(a)
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('users.login'))
        b = "Your account has been Created..."
    return jsonify(b)


@users.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        c = "Your are authenticated "
        return  jsonify(c)
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            f = "You logged In "
            return jsonify(f)
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
            d = "Logged in Not successful"
    return jsonify(d)


@users.route("/logout")
def logout():
    logout_user()
    e = "You are out"
    return jsonify(e)
