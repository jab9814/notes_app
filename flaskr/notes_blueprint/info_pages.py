from flask import (
    request, 
    Blueprint
)


info_bp = Blueprint('info', __name__)


@info_bp.route('/acerca-de')
def about():
    return "Esta es una aplicacion de prueba con flask."


@info_bp.route('/contacto', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        return "Mensaje enviado con éxito.", 201
    return "Pagina de contacto. Puedes enviar un mensaje aquí."
