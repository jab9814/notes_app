from flask import Flask, redirect, request, jsonify, render_template, url_for


app = Flask(__name__)

@app.route('/')
def home():
    role = 'programador'
    notes = [
        {"id": 1, "title": "Nota 1", "content": "Contenido de la nota 1"},
        {"id": 2, "title": "Nota 2", "content": "Contenido de la nota 2"}
    ]
    return render_template('home.html', role=role, notes=notes)

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
        note = request.form.get('note', "No encontrada")
        return redirect(url_for('confirmation', note=note))
    return render_template('note_form.html')