from flaskr.models import db, Note, StatusEnum
from datetime import datetime
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
        start_date = datetime.strptime(request.form.get('start_date'), '%Y-%m-%d').date()
        end_date = datetime.strptime(request.form.get('end_date'), '%Y-%m-%d').date()
        
        if start_date > end_date:
            flash('La fecha de inicio no puede ser mayor que la fecha de finalización', 'error')
            return render_template('note_form.html', form_data=request.form)

        note_db = Note(
            assigned_to=request.form.get('assigned_to', ""),
            title=request.form.get('title', ""),
            content=request.form.get('content', ""),
            status=StatusEnum(request.form.get('status')),
            start_date=start_date,
            end_date=end_date
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
        start_date = datetime.strptime(request.form.get("start_date"), '%Y-%m-%d').date()
        end_date = datetime.strptime(request.form.get("end_date"), '%Y-%m-%d').date()
        
        if start_date > end_date:
            flash('La fecha de inicio no puede ser mayor que la fecha de finalización', 'error')
            return render_template('edit_note_form.html', note=note)
            
        updates = {
            'title': request.form.get('title', ""),
            'content': request.form.get('content', ""),
            'assigned_to': request.form.get("assigned_to", ""),
            'status': StatusEnum(request.form.get("status")),
            'start_date': start_date,
            'end_date': end_date
        }
        
        for field, value in updates.items():
            setattr(note, field, value)
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

