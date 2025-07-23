import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, redirect, request, jsonify, render_template, url_for

DB_FILE = os.path.join(os.path.dirname(__file__), 'database.sqlite')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_FILE}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db = SQLAlchemy(app)


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Note {self.id}:{self.title}>'


@app.route('/')
def home():
    notes = Note.query.all()
    return render_template('home.html', notes=notes)

@app.route('/acerca-de')
def about():
    return "Esta es una aplicacion de prueba con flask."

@app.route('/contacto', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        return "Mensaje enviado con éxito.", 201
    return "Pagina de contacto. Puedes enviar un mensaje aquí."


@app.route('/api/info', methods=['GET'])
def api_info():
    return jsonify({
        "name": "Flask App",
        "version": "1.0.0",
        "description": "A simple"
    }), 200


@app.route('/confirmacion')
def confirmation():
    return "Confirmación de acción exitosa.", 200

@app.route('/crear-nota', methods=['GET', 'POST'])
def create_note():
    if request.method == 'POST':
        title = request.form.get('title', "")
        content = request.form.get('content', "")

        note_db = Note(title=title, content=content)

        db.session.add(note_db)
        db.session.commit()

        return redirect(url_for('home'))
    return render_template('note_form.html')


@app.route('/editar-nota/<int:id>', methods=['GET', 'POST'])
def edit_note(id: int):
    note = Note.query.get_or_404(id)
    if request.method == 'POST':
        title = request.form.get('title', "")
        content = request.form.get('content', "")

        note.title = title
        note.content = content

        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit_note_form.html', note=note)


@app.route('/eliminar-nota/<int:id>', methods=['POST'])
def delete_note(id: int):
    note = Note.query.get_or_404(id)
    db.session.delete(note)
    db.session.commit()
    return redirect(url_for('home'))
