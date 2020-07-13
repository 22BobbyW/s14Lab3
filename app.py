from flask import Flask, render_template, request, redirect, url_for
#from flask_heroku import Heroku
from models.user import Db, User
from modules.forms import IDForm, UserForm, UpdateForm, MockForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/usersdb'

# app = Flask(__name__)
# heroku = Heroku(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "s14a-key"
Db.init_app(app)


@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)


@app.route('/adduser', methods=['GET', 'POST'])
def addUser():
    form = UserForm()

    if request.method == 'GET':
        return render_template('adduser.html', form=form)
    else:
        if form.validate_on_submit():
            first_name = request.form['first_name']
            age = request.form['age']
            new_user = User(first_name=first_name, age=age)
            Db.session.add(new_user)
            Db.session.commit()
            return redirect(url_for('index'))
        else:
            return render_template('adduser.html', form=form)


@app.route('/readuser', methods=['GET', 'POST'])
def readUser():
    form = IDForm()

    if request.method == 'GET':
        return render_template('idread.html', form=form)
    else:
        if form.validate_on_submit():
            id = request.form['user_id']
            user = User.query.filter_by(user_id=id).first()
            if user is None:
                return render_template("nouser.html")
            return render_template('readuser.html', user=user)
        else:
            return render_template('idread.html', form=form)


@app.route('/deleteuser', methods=['GET', 'POST'])
def deleteUser():
    form = IDForm()

    if request.method == 'GET':
        return render_template('deleteuser.html', form=form)
    else:
        if form.validate_on_submit():
            id = request.form['user_id']
            user = User.query.filter_by(user_id=id).first()
            if user is None:
                return render_template("nouser.html")
            Db.session.delete(user)
            Db.session.commit()
            return redirect(url_for('index'))
        else:
            return render_template('deleteuser.html', form=form)


@app.route('/updateuser', methods=['GET', 'POST'])
def updateUser():
    form = UpdateForm()

    if request.method == 'GET':
        return render_template('updateuser.html', form=form)
    else:
        if form.validate_on_submit():
            new_first_name = request.form['first_name']
            new_age = request.form['age']
            id = request.form['user_id']
            if User.query.filter_by(user_id=id).first() is None:
                return render_template("nouser.html")
            User.query.filter_by(user_id=id).update({'first_name': new_first_name, 'age': new_age})
            Db.session.commit()
            return redirect(url_for('index'))
        else:
            return render_template('updateuser.html', form=form)


@app.route('/generatemock', methods=['GET', 'POST'])
def generateMock():
    form = MockForm()

    if request.method == 'GET':
        return render_template('generatemock.html', form=form)
    else:
        num = request.form['number']
        for i in range(int(num)):
            name = 'USER' + str(i + 1)
            temp = User(first_name=name, age=100)
            Db.session.add(temp)
        Db.session.commit()
        return redirect(url_for('index'))

@app.route('/deletemock')
def deletemock():
    users = User.query.all()
    for user in users:
        name = user.first_name[0:4]
        if name == "USER":
            Db.session.delete(user)
    Db.session.commit()
    return redirect(url_for('index'))


@app.route('/adduser/<first_name>/<age>')
def addUserFromUrl(first_name, age):
    Db.session.add(User(first_name=first_name, age=age))
    Db.session.comit()
    return redirect(url_for('index'))
