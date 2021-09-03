# Jotter
#### Progress Notes / Client Management for therapists and professionals
An application for therapists / professionals to take basic progress or session notes as well as manage basic client information. Notes can be shared with other users with appropriate permissions. Users can login to app. Admin / SuperUser can edit details and permissions. Something about privacy...


## Features:
- A User (therapist / professional / admin) can login to the application, change their details
- A User can create a 'client' or 'patient'
- A SuperUser can change Client permissions for Users
- A Client will have a profile that has their information (Name, DOB, Address, Next of Kin etc)
- A User creates a SessionNote for a Client
- A SessionNote will have session information like description, time etc. (simple)
- A SessionNote can be edited, with tracked changes(?)
- A SessionNote 'recent history' can be viewed
- A User can generate SessionNote reports (all of time or between fixed dates)
- An intake form can be generated for a Client to fill out (via paper or digitally, no login required). Digital intake must be approved.
- Has a SuperUser Admin interface

---

## Models

### User / SuperUser
- Has permissions
- Id
- First Name
- Last Name
- Email Address (used for logins and app communication)
- Has many Clients
- Has many SessionsNotes


### Client (like product, person has no access)
- Id, First name, Last Name, Address (Street No, Unit No, Street, Suburb, State, Autocomplete(?))
- Emergency Contact - First Name, Last Name, Contact Ph
- Other Contact (allied health, doctor etc) - Name, Contact Ph, Contact Email, Description
- Profile Image(?)
- Funding type (list)
- Has many SessionNotes

### SessionNote
- Date of session (selectable)
- Time of session (selectable)
- Length of session
- Type of session (selectable -> therapy, allied health, etc.)
- Session Description (i.e. the actual session notes, longform text field, with rich-text(?))
- Created_at
- Updated_at
- Belongs to User
- Belongs to Client
- Has attachment (optional, short video, image, PDF)

---

## Technologies

### Backend
- Python
- Flask (API)
- Pipenv
- SQLAlchemy (flask-sqlalchemy)
- Marshmallow (flask-marshmallow)
- mashmallow-sqlalchmey
- Postgres (?) / SQLite

### Frontend
- ReactJS
- React-router-dom
- React Icons


## Instructions
This is still very much a WIP. So far, to get something happening with the backend:

Do you have to install requirements? Get the virtual environment up and running and install shit, but I think its included?
```bash
source /venv/bin/activate
pip install -r requirements.txt
```

To run the server you can:
```bash
flask run
```
or:
```bash
python3 app.py
```

For me to create the server, I had to open a python console from within the backend directory with ```python3``` and then:

```python
from app import db
db.create_all()
```

*Need to look at migrations*

To view current API endpoints, use Postman, or some other way to access APIs. Current JSON endpoints are:
http://localhost:5000/sessionnotes
A 'GET' request will return all session notes
A 'POST' request, with correct JSON parameters will enter a session note. Currently this is:

```json
{
    "client" : "Billy Joel",
    "session_type": "consulation",
    "length": 50,
    "notes": "I wonder if he will play Piano Man if I ask him? Maybe if I just wait until the third session..."
}
```

## TO DO
Everything. To be more specific, the things I need to learn about:
- Correctly implementing an API
- User login, authentication using Tokens across JSON
- Possibility of including Rich Text
- Migrations (alembic??)
- Virtually everything to do with React + Javascript