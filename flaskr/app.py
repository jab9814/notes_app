from flaskr.config import Config
from flaskr.models import db, Note
from flaskr.notes.routes import notes_bp
from flask import Flask, request, render_template


app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
app.register_blueprint(notes_bp)


@app.route('/acerca-de')
def about():
    return "Esta es una aplicacion de prueba con flask."


@app.route('/contacto', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        return "Mensaje enviado con éxito.", 201
    return "Pagina de contacto. Puedes enviar un mensaje aquí."


@app.route('/')
def home():
    notes = Note.query.all()
    return render_template('home.html', notes=notes)

