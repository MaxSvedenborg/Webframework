from flask import *
import BI.user_controller as uc
import json

app = Flask(__name__)


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
@app.route('/postman', methods=['POST'])
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


@app.route('/thisuser')
def users():
    name = request.args.get('name')
    return render_template('users.html', name=name)


@app.errorhandler(404)
def handler404(e):
    return render_template('404.html', error=e)


@app.errorhandler(500)
def handler500(e):
    return render_template('500.html', error=e)


@app.route('/')
def index():
    return 'Greetings group six!'


"""@app.route('/login')
def login():
    return render_template('login_boot.html')"""


if __name__ == '__main__':
    app.run()
