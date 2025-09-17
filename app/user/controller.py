from flask import render_template, redirect, request, jsonify, flash, url_for
from flask_login import login_user, logout_user, login_required, current_user
from . import user_bp
import app.models as models
from app.user.forms import UserForm, LoginForm


@user_bp.route('/user')
@user_bp.route('/')
@login_required
def index():
    users = models.Users.all()
    return render_template('index.html', data=users,title='Home',something='something')

@user_bp.route('/user/register', methods=['POST','GET'])
@login_required
def register():
    form = UserForm(request.form)
    if request.method == 'POST' and form.validate():
        user = models.Users(email=form.email.data, password=form.password.data,username=form.username.data)
        user.add()
        flash('User registered successfully!', 'success')
        return redirect('/')
    else:
        return render_template('signup.html', form=form)

@user_bp.route("/user/delete", methods=["POST"])
@login_required
def delete():
    id = request.form['id']
    if models.Users.delete(id):
        return jsonify(success=True,message="Successfully deleted")
    else:
        return jsonify(success=False,message="Failed")

@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('user.index'))

    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = models.Users.get_by_username(form.username.data)
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            flash('Logged in successfully!', 'success')

            next_page = request.args.get('next')
            if not next_page or not next_page.startswith('/'):
                next_page = url_for('user.index')
            return redirect(next_page)
        else:
            flash('Invalid username or password', 'error')

    return render_template('login.html', form=form, title='Login')

@user_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out', 'info')
    return redirect(url_for('user.login'))          