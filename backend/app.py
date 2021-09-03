from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from datetime import datetime
import os

# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Init db
db = SQLAlchemy(app)
# Init Marshmallow
ma = Marshmallow(app)

# SessionNote Model
class SessionNote(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)

    length = db.Column(db.Integer)
    session_type = db.Column(db.String)
    notes = db.Column(db.Text)
    client = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow())

    def __init__(self, length, session_type, notes, client):

        self.length = length
        self.session_type = session_type
        self.notes = notes
        self.client = client
    


# SessionNoteSchema Schema
class SessionNoteSchema(ma.Schema):
    class Meta:
        fields = ('id', 'length', 'session_type',
                  'notes', 'created_at', 'client')


# Init Schema
session_note_schema = SessionNoteSchema()
session_notes_schema = SessionNoteSchema(many=True)


# Create a SessionNote
@app.route('/sessionnotes', methods=['POST'])
def add_note():

    length = request.json['length']
    session_type = request.json['session_type']
    notes = request.json['notes']
    client = request.json['client']

    new_session_note = SessionNote(length, session_type, notes, client)

    db.session.add(new_session_note)
    db.session.commit()

    return session_note_schema.jsonify(new_session_note)

# Get all SessionNotes
@app.route('/sessionnotes', methods=['GET'])
def get_all_notes():
    all_notes = SessionNote.query.all()
    return session_notes_schema.jsonify(all_notes)




# Run server
if __name__ == "__main__":
    app.run(debug=True)