from flask import Flask, render_template,request,session
from ext.db import configure_db
from ext.admin import configure_admin
from flask_babelex import Babel

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.secret_key='ddadahdhajhdajdhjaj'
configure_db(app)


configure_admin(app)
app.config['FLASK_ADMIN_SWATCH'] = 'slate'

babel = Babel(app)

@app.before_first_request
def before_f_request():
    app.db.create_all()

@babel.localeselector
def get_locale():
    if request.args.get('lang'):
        session['lang'] = request.args.get('lang')
    return session.get('lang', 'pt_BR')


@app.route('/')
def index():
    return render_template('index.html')


 