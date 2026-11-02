# SCOPE INDIA - Student Registration & Course Management System

## Project Overview

SCOPE INDIA is a Django-based web application developed using the MVT (Model-View-Template) architecture. The system allows students to register, create passwords, log in, view courses, and manage their profiles. It also includes dynamic Country-State-City selection using AJAX.

---

## Features

### Student Module
- Student Registration
- Create Password after Registration
- Login Authentication
- Logout Functionality
- Student Dashboard

### Course Module
- View Available Courses
- Course Information Display

### Contact Module
- Contact Form
- Email Integration using Django Mail

### Location Module
- Country Selection
- Dynamic State Dropdown (AJAX)
- Dynamic City Dropdown (AJAX)

### Profile Module
- Profile Image Upload
- Student Information Storage

### UI Features
- Responsive Bootstrap Design
- Professional Navbar
- Hover Effects
- Responsive Forms
- Modern Dashboard Interface

---

## Technologies Used

### Frontend
- HTML5
- CSS3
- Bootstrap 5
- JavaScript
- jQuery
- AJAX

### Backend
- Python
- Django

### Database
- SQLite3

### Other Libraries
- Pillow
- Django Email Backend

---

## Project Architecture

This project follows Django's MVT Architecture.

### Model
Database Structure

- Student
- Course
- Contact
- Country
- State
- City

### View
Business Logic

- Registration
- Login
- Dashboard
- Contact
- AJAX Functions

### Template
Frontend User Interface

- Home Page
- About Page
- Contact Page
- Register Page
- Login Page
- Dashboard Page

---

## Installation

### Clone Repository

```bash
git clone <repository_url>
```

### Move to Project Folder

```bash
cd project_name
```

### Create Virtual Environment

```bash
python -m venv project_env
```

### Activate Environment

```bash
project_env\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Create Superuser

```bash
python manage.py createsuperuser
```

### Run Server

```bash
python manage.py runserver
```

---

## Project Flow

Student Registration
↓
Create Password
↓
Login
↓
Dashboard
↓
View Courses
↓
Logout

---

## Database Models

### Student

- First Name
- Last Name
- Gender
- DOB
- Email
- Phone
- Country
- State
- City
- Avatar
- Password

### Course

- Course Name
- Duration
- Fee

### Contact

- Name
- Email
- Subject
- Message

### Country

- Country Name

### State

- State Name
- Country (Foreign Key)

### City

- City Name
- State (Foreign Key)

---

## AJAX Implementation

Used for dynamic dropdown loading.

### Country → State

```javascript
/load-states/
```

### State → City

```javascript
/load-cities/
```

---
