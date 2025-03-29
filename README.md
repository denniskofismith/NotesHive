Simple Notes API

This is a RESTful API for managing notes with basic CRUD operations.

Features

Create, Read, Update, and Delete notes.

Tech Stack

Backend: Django

Database:  SQLite

Installation & Setup

Clone the Repository

git clone https://github.com/NotesHive/notes-api.git
cd notes-api

Install Dependencies

npm install

Start the Server

npm start

Server runs on http://localhost:8000

API Endpoints

Create a Note

POST /api/notes

Body:

{
  "title": "My First Note",
  "content": "This is a test note."
}

Get All Notes

GET /notes

Get a Note by ID

GET /notes/<int:id>

Update a Note

PUT /api/notes/<int:id>

Body:

{
  "title": "Updated Note",
  "content": "This note has been updated."
}

Delete a Note

DELETE /api/notes/<int:id>

Future Enhancements

User authentication

File attachments

Categorizing notes




