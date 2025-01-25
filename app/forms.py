"""Sign-up & log-in forms."""
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Optional, Regexp, NoneOf

# CommonPassword.txt
def get_common_passwords():
    """ GET LIST OF COMMON PASSWORDS """
    with open('CommonPassword.txt', 'r', encoding="utf-8" ) as file:
        return [line.strip() for line in file]


class SignupForm(FlaskForm):
    """User Sign-up Form."""
    common_passwords = get_common_passwords()

    # User Name
    user_name = StringField("Name", validators=[DataRequired()])
    user_email = StringField(
        "Email",
        validators=[
            Length(min=6),
            Email(message="Enter a valid email."),
            DataRequired(),
        ],
    )
    # Password
    user_password = PasswordField(
        "Password",
        validators=[
            DataRequired(),
            Length(min=12, message="Password must be at least 12 characters long."),
            Regexp(
            regex=r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]+$',
            message="Password must include at least 1 uppercase," +
                    "1 lowercase, 1 number, and 1 special character."
                    ),
            NoneOf(common_passwords, "Password is too common"),
        ],
    )
    user_password_confirm = PasswordField(
        "Confirm Password",
        validators=[
            DataRequired(),
            EqualTo("user_password", message="Passwords must match."),
        ],
    )
    
    # Website optional
    user_metadata_website = StringField("Website", validators=[Optional()])
    submit_button = SubmitField("Register")

# Update Password Form
class UpdateForm(FlaskForm):
    """User Update Form."""
    common_passwords = get_common_passwords()

    old_user_password = PasswordField("Old Password", validators=[DataRequired()])

    user_password = PasswordField(
        "New Password",
        validators=[
            DataRequired(),
            Length(min=12, message="Password must be at least 12 characters long."),
            Regexp(
            regex=r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]+$',
            message="Password must include at least 1 uppercase," +
                    "1 lowercase, 1 number, and 1 special character."
                ),
            NoneOf(common_passwords, "Password is too common"),
        ],
    )
    user_password_confirm = PasswordField(
        "Confirm Password",
        validators=[
            DataRequired(),
            EqualTo("user_password", message="Passwords must match."),
        ],
    )
    submit_button = SubmitField("Change Password")

# User Login
class LoginForm(FlaskForm):
    """User Log-in Form for existing users."""
    user_email = StringField(
        "Email",
        validators=[
            DataRequired(),
            Email(message="Enter a valid email.")
        ]
    )
    user_password = PasswordField("Password", validators=[DataRequired()])
    submit_button = SubmitField("Log In")
