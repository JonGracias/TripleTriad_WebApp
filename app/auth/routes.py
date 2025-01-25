""" ROUTES FOR AUTHENTICATION """
from typing import Optional
#pylint: disable=E0401
from flask import Blueprint, Response, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_user, logout_user

# All the different forms
from app.forms import LoginForm, SignupForm, UpdateForm

# The User and Message database Model and the db (database)
from app.models import User, db, Message

# login_manager from __init__.py
from app import login_manager

auth_blueprint = Blueprint(
    "auth",
    __name__,
    template_folder="templates",
    static_folder="static"
)

# Signup form
@auth_blueprint.route("/signup", methods=["GET", "POST"])
def signup() -> Response:
    """ 
    VIEW FOR NEW USERS TO SIGN UP

    GET: Serve sign-up page.
    POST: Validate form, create account, redirect user to home
    """
    form = SignupForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(email=form.user_email.data).first()
        # Checks if user exists
        if existing_user is None:
            user = User(name=form.user_name.data,
                        email=form.user_email.data,
                        website=form.user_metadata_website.data)
            user.set_password(form.user_password.data)
            user.set_profile_image("static/img/user-alt-1-svgrepo-com.svg")
            db.session.add(user)
            db.session.commit()
            login_user(user)
            print(user)
            #reroutes to the home with profile if everything is okay
            return redirect('/home')
        # Else A flash message appears
        flash("A user already exists with that email address.")

    # Else back to the signup page
    return render_template(
        "signup.jinja2",
        title="Create an Account.",
        form=form,
        template="signup-page",
        body="Sign up for a user account.",
    )

@auth_blueprint.route("/update", methods=["GET", "POST"])
def update() -> Response:
    """ 
    VIEW FOR USERS TO UPDATE PASSWORD

    GET: Serve Update page.
    POST: Validate form, update password, redirect user to home
    """
    form = UpdateForm()
    if form.validate_on_submit():
        if current_user.is_authenticated:
            print("Setting User")
            user = current_user
            print(user)
            print(user.check_password(password=form.old_user_password.data))
            if user.check_password(password=form.old_user_password.data):
                print("Password Check")
                user.set_password(form.user_password.data)
                db.session.add(user)
                db.session.commit()
                return redirect('/home')
        flash("Invalid credentials or user not logged in.")

    return render_template(
        "update.jinja2",
        title="Update Password.",
        form=form,
        template="upate-page",
        body="Update Password.",
    )


@auth_blueprint.route("/login", methods=["GET", "POST"])
def login() -> Response:
    """
    LOG-IN PAGE

    GET: Serve Log-in page.
    POST: Validate form and redirect user to home

    :returns: Response
    """
    if current_user.is_authenticated:
        return redirect('/home')
    
    # Define Form
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.user_email.data).first()
        if user and user.check_password(password=form.user_password.data):
            login_user(user)
            next_page = request.args.get("next")
            return redirect(next_page or ('/home'))
        log_message = f"Failed login attempt for email: {form.user_email.data}"
        message = Message(content=log_message)
        db.session.add(message)
        db.session.commit()
        print(message.content)
        flash("Invalid username/password combination")

    return render_template(
        "login.jinja2",
        form=form,
        title="Log In",
        template="login-page",
        body="Log in with your User account.",
    )

@auth_blueprint.route("/logout", methods=["GET"])
def logout() -> Response:
    """
    LOG-OUT
    """
    if current_user.is_authenticated:
        logout_user()

    return redirect(url_for("main.home"))

@login_manager.user_loader
def load_user(user_id: int) -> Optional[User]:
    """ CHECK IF LOGGED IN """
    return User.query.get(user_id)

@login_manager.unauthorized_handler
def unauthorized() -> Response:
    """ REDIRECT TO LOGIN """
    flash("You must be logged in to view that page.")
    return redirect(url_for("auth.login"))
