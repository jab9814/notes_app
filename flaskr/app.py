from flask import Flask, request, jsonify


app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!" 

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