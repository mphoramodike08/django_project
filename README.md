# Django Sticky Notes Application

## Description
This is a Django-based sticky notes application that allows users to create, view, edit, and delete notes.

## Features
- Create notes
- View all notes
- Edit notes
- Delete notes
- Sphinx documentation support
- Docker support

## Project Structure
```text
sticky_notes_django_capstone_submission/
├── docs/
├── diagrams/
├── sticky_notes/
│   ├── manage.py
│   ├── notes/
│   └── sticky_notes/
├── .gitignore
├── Dockerfile
├── README.md
├── capstone.txt
└── requirements.txt
```

## Run with a Virtual Environment
1. Clone the repository:
   ```bash
   git clone https://github.com/mphoramodike08/sticky_notes_django.git
   cd sticky_notes_django
   ```
2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
3. Activate the virtual environment:
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Move into the Django project folder:
   ```bash
   cd sticky_notes
   ```
6. Apply migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
7. Run the development server:
   ```bash
   python manage.py runserver
   ```
8. Open the app at `http://127.0.0.1:8000/`.

## Run with Docker
1. Build the Docker image from the project root:
   ```bash
   docker build -t sticky-notes-app .
   ```
2. Run the container:
   ```bash
   docker run -p 8000:8000 sticky-notes-app
   ```
3. Open the app at `http://127.0.0.1:8000/`.

## Generate Sphinx Documentation
From the project root, run:
```bash
sphinx-build -b html docs docs/_build
```
Then open `docs/_build/index.html` in your browser.

## Notes
- Do not commit secrets or environment files to a public repository.
- Use `.gitignore` to exclude virtual environments, local databases, and editor files.
