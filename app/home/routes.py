""" ROUTES FOR MAIN """
#pylint: disable=E0401
from datetime import datetime
from flask import (
    render_template,
    Blueprint,url_for
)
import pandas as pd
from flask_login import current_user
from app.models import Message



main_blueprint= Blueprint(
    "main",
    __name__,
    template_folder="templates",
    static_folder="static"
)

# Default route, no user profile - will reroute
@main_blueprint.route('/', defaults={'path': ''})
@main_blueprint.route('/<path:path>')
def home(path):
    """ INDEX PAGE """
    date = datetime.now()
    if current_user.is_authenticated:
        user_name = current_user.name
    else:
        user_name = "Guest"
    
    
    # For Example Only Can Delete Later
    meteor = '<img src="static/img/meteor.svg" alt="Meteor">'
    cheese = '<img src="static/img/cheese.svg" alt="cheese">'
    cheeseburger = '<img src="static/img/cheese_burger.svg" alt="cheeseburger">'


    return render_template('home.jinja2', date=date, path=path,
                            user_name=user_name, meteor=meteor, cheese=cheese, cheeseburger=cheeseburger)

# Disply user login logs
@main_blueprint.route('/logs')
def logs():
    """ LOGS OF ALL LOGINS """
    # Queries the Message db
    messages = Message.query.all()
    # Prints the Message db in console
    print(messages)
    # Displays the results on logs.jinja2
    return render_template('logs.jinja2', messages=messages)

# Home route with user profile. Does not reroute.
@main_blueprint.route('/home')
def welcome():
    """ HOME ROUTE """
    
    if current_user.is_authenticated:
        # If the user is already logged in
        
        # Get user image
        user_image = current_user.get_images()
        
        #User info and greeting
        print(user_image)
        profile_image = '<img src="' + user_image + '"alt="Profile Image">'
        user_name = current_user.name
        
        # Extra Edit Buttons
        edit_password = '<a href="' + url_for('auth.update') + '">Update Password</a>'
        edit_profile = '<a href="' + url_for('main.home') + '">Edit Profile</a>' # Doesn't work

        #User info table
        user_header = [profile_image, ['nothing'], ['nothing']]
        info1 = [user_name, ['nothing'], ['nothing']]
        info2 = [edit_password, ['nothing'], ['nothing']]
        info3 = [edit_profile, ['nothing'], ['nothing']]

        # table
        source = [user_header, info1, info2, info3]
        
    else:
        #If not Logged in this happens
        user_name = "Guest"
    
    #Panda Data Frame for table
    d_f = pd.DataFrame(source, columns=None)
    
    # Make table HTML
    html_table = d_f.to_html(escape=False, index=False, header=False)
    
    
    # Return the rendered 'home.jinja2' template with dynamic data passed to it.
    return render_template(
        'home.jinja2',               # The name of the Jinja2 template file to render (HTML-like file in the templates directory).
        user_name=user_name,         # A variable passed to the template, containing the name of the current user.
        html_table=html_table,       # Another variable passed to the template, containing an HTML table structure as a string or rendered object.
    )

