# Jotter
#### Client management / progress notes for therapists.
An application for therapists / professionals to manage basic details of clients or patients and take progress notes or session notes. Notes can be shared with other users with appropriate permissions. Users can login to app. Admin / SuperUser can edit details and permissions. Something about privacy...

## Features:
- A User can login to the application, change their details
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
