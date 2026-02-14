from flask_sqlalchemy import SQLAlchemy
from enum import Enum
from datetime import datetime


db = SQLAlchemy()


class StatusEnum(Enum):
    Stand_by = 'Stand_by'
    Pending = 'Pending'
    Progress = 'Progress'
    Done = 'Done'
    Failed = 'Failed'


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    assigned_to = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    status = db.Column(db.Enum(StatusEnum), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f'<Note {self.id}:{self.title}>'
