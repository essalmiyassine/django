# Django Project

This project is a foundational structure (socle) for Django applications. It is designed to help developers quickly set up a Django environment and begin building their web applications. The project is written entirely in Python.

## Available Commands

In the project directory, you can run:

### `python manage.py runserver`

To run the app in development mode. Open [http://127.0.0.1:8000](http://127.0.0.1:8000) to view it in the browser.
The page will reload if you make edits. You will also see any errors in the console.

### `python manage.py migrate`

To apply database migrations. Make sure to run this command after making changes to your models.

### `python manage.py makemigrations`

To create new migrations based on the changes you have made to your models.

### `python manage.py shell`

To start a Python interactive shell with Django's settings and models loaded.

## Installation

To get started with this project, you can either use a virtual environment or install dependencies directly.

### 1. Clone the repository

```bash
git clone https://github.com/essalmiyassine/django.git
```

### 2. (Optional) Create and activate a virtual environment

Using a virtual environment is recommended to isolate dependencies.

- Create a virtual environment:

  ```bash
  python -m venv env
  ```

- Activate the virtual environment:
  - On Windows:
    ```bash
    .\env\Scripts\activate
    ```
  - On macOS/Linux:
    ```bash
    source env/bin/activate
    ```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply migrations

```bash
python manage.py migrate
```

### 5. Start the development server

```bash
python manage.py runserver
```

## Usage

To use this project, follow the installation steps and start the development server.  
You can then access the application at [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your web browser.

