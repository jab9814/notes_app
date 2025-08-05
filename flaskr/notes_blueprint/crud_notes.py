from flaskr.models import db, Note
from flask import (
    redirect, 
    request, 
    render_template, 
    url_for, 
    Blueprint,
    flash
)


notes_bp = Blueprint('notes', __name__)


@notes_bp.route('/crear-nota', methods=['GET', 'POST'])
def create_note():

    """ Creacion de notas  """

    if request.method == 'POST':
        note_db = Note(
            title=request.form.get('title', ""),
            content=request.form.get('content', ""),
        )
        db.session.add(note_db)
        db.session.commit()
        flash(
            message='Nota creada con exito!', 
            category='success'
        )
        return redirect(url_for('home'))
    return render_template('note_form.html')


@notes_bp.route('/editar-nota/<int:id>', methods=['GET', 'POST'])
def edit_note(id: int):

    """ Edicion de notas  """

    note = Note.query.get_or_404(id)
    if request.method == 'POST':
        note.title = request.form.get('title', "")
        note.content = request.form.get('content', "")
        db.session.commit()
        flash(
            message='Nota actualizada con exito!', 
            category='success'
        )
        return redirect(url_for('home'))
    return render_template('edit_note_form.html', note=note)


@notes_bp.route('/eliminar-nota/<int:id>', methods=['POST'])
def delete_note(id: int):

    """ Borrar de notas  """
    
    note = Note.query.get_or_404(id)
    db.session.delete(note)
    db.session.commit()
    flash(
        message='Nota eliminada con exito!', 
        category='success'
    )
    return redirect(url_for('home'))

