from flask import Flask, render_template, request, redirect, url_for, session
from flask_login import UserMixin, current_user, login_required
import BI.user_controller as uc
import json
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Length, Email
import client.config as config

app = Flask(__name__)
app.config.from_object(config)


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8)])
    remember = BooleanField('Remember me')


@app.route('/')
def index():
    data = 'home'
    return render_template('index.html', data=data)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        pass
        # Check if user exists
        # If user exists redirect to in-page
        # else throw auth error / redir
    return render_template('templates/auth/temp_login.html', form=form)


@app.route('/adduser/<fname>/<lname>')
def adduser(fname, lname):
    userdata = {
            'name': fname,
            'email': lname
    }
    try:
        uc.add_user(userdata)
        return 'user successfully registered'
    except:
        return 'shit went sideways...'


# post form data
@app.route('/adduser', methods=['POST'])
def postman():
    fname = request.form.get('first')
    lname = request.form.get('last')
    return f'Hello {fname} {lname}'


# post json
@app.route('/post', methods=['POST'])
def index_post():
    data = request.data
    python_data = json.loads(data)
    print(python_data)

    # The response can be data collected from db.
    # ie resource ID in => resource entry out
    out_data = {
        'result': 'this was fun',
        'the things i got was': python_data['things']
    }

    response = app.response_class(
        response=json.dumps(out_data),
        status=200,
        mimetype='application/json'
    )
    return response

# just a demo for adding a user with requests args.
@app.route('/thisuser')
def users():
    name = request.args.get('name')
    return render_template('templates/users.html', name=name)


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard/dashboard.html')


@app.route('/sites')
def sites():
    return render_template('add_site.html')


@app.route('/account')
def account():
    return render_template('account_settings.html')


#
# @app.route('/login')
# def login():
#     return render_template('auth/login_boot.html')


@app.route('/register')
def register():
    return render_template('auth/register_boot.html')


@app.route('/reset_password')
def reset_password():
    return render_template('password_boot.html')



@app.errorhandler(404)
def handler404(e):
    return render_template('404.html', error=e)


@app.errorhandler(500)
def handler500(e):
    return render_template('500.html', error=e)



if __name__ == '__main__':
    app.run()
