<h1 align="center">B Management System</h1>

## Pages

- Dashboard
- Login
- Register
- User Profile
- Edit and Delete Users
- Groups Dashboard
- Edit, and Delete Groups
- REST API
- Pop-up Notification

## Key Features

- Modern design
- Responsive
- Multi dynamic page website
- Smooth navigation
- Handling advanced database
- Developed powerful backend

## Tech Stack

- HTML
- CSS (Bootstrap)
- JavaScript (AJAX, JQuery)
- Python (Django)
- MySQL

## Run Locally

Create a database in our system named `bms_db` with username and password `root`

Download the zip file of the project or clone it.

```bash
  git clone https://github.com/imriadutta/bms.git
```

After that run these following commands sequentially.

```bash
  pip install -r "requirements.txt"
  python manage.py makemigrations
  python manage.py migrate
```

And to start the server, run the below command.

```bash
  python manage.py runserver
```
