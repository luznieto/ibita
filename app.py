from dbutils import db_connect
from dbutils import db_insert_user
from dbutils import db_find_all
from dbutils import MONGO_URI1
from dbocb import dbocb_connect
from dbocb import db_insert_ocb
from dbocb import dbocb_find_all
from dbocb import MONGO_URI2
from form import EmailForm
from form import LoginForm
from form import OCBForm
from flask import Flask
from flask import request
from flask import render_template


app = Flask(__name__)

users=db_connect(MONGO_URI1, 'mi_app', 'users')
ocbs=dbocb_connect(MONGO_URI2, 'mip_app', 'ocbs')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = EmailForm(request.form)
    flag = False
    name = None

    if len(form.errors):
        print(form.errors)
    if request.method == 'POST':
        email = form.email.data
        name = form.name.data
        if email != '' and name != '':
            print(f"Nombre capturado: {name}")
            print(f"Email capturado: {email}")
            user={
            "name": name,
            "email":email
            }
            r = db_insert_user(users, user)
            print("Inserción:",r)
            flag = True

    return render_template('index.html', flag=flag, name=name)


@app.route('/dashboard', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    login_error = False

    if len(form.errors):
        print(form.errors)
    if request.method == 'POST':
        if form.username.data == 'admin' and form.password.data == 'admin':
            registered = db_find_all(users)
            return render_template('tables.html', users=registered)
        if form.username.data == 'experto' and form.password.data == 'experto':
            registered = dbocb_find_all(users)
            return render_template('tables_ocb.html', users=registered)
        else:
            login_error = True
    return render_template('login.html', login_error=login_error)
def experto():
    form = OCBForm(request.form)
    flag = False
    name = None

    if len(form.errors):
        print(form.errors)
    if request.method == 'POST':
        agente = form.agente.data
        tipo = form.tipo.data
        descrip = form.descrip.data
        issue= form.issue.data
        culture = form.culture.data
        product = form.product.data
        certified = form.certified.data
        if agente != '' and tipo != '' and descrip != '' and issue != '' and culture != '' and product != '' and certified != '':
            ocb={
            "agente": agente,
            "tipo": tipo,
            "descrip": descrip,
            "issue": issue,
            "culture": culture,
            "product": product,
            "certified": certified
            }
            r = db_insert_ocb(ocbs, ocb)
            print("Insercion:",r)
            flag = True

    return render_template('tables_ocb.html', flag=flag, name=name)



@app.errorhandler(404)
def no_encontrado(error=None):
    return render_template("404.html", url=request.url)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
