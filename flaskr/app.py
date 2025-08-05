from flaskr.models import db, Note
from flask import Flask, render_template
from flaskr.config_db_sqlite import ConfigDB
from flaskr.notes_blueprint.info_pages import info_bp
from flaskr.notes_blueprint.crud_notes import notes_bp


app = Flask(__name__)
app.config.from_object(ConfigDB)
db.init_app(app)
app.register_blueprint(notes_bp)
app.register_blueprint(info_bp)


@app.route('/')
def home():
    notes = Note.query.all()
    return render_template('home.html', notes=notes)
