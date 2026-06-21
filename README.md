# TeeMusic Recording Studio Website

## 📌 Project Overview

This project is a responsive portfolio and booking website developed for **teeMusic Recording Studio** using the Flask web framework. The system was created as part of a student web development assignment to demonstrate front-end and back-end web development concepts using Python, Flask, SQLAlchemy, JavaScript, jQuery, HTML5, and CSS3.

The website allows users to:

* Browse studio information and services
* View artists and studio content
* Submit studio bookings
* Subscribe to newsletters
* Interact with dynamic content without page reloads

The project follows recommended web development practices including:

* Separation of concerns
* Template inheritance
* Responsive design
* Dynamic rendering using Jinja2 templates

---

# 🌐 Website Pages

The application includes the following pages:

* Home
* About
* Services
* Artists
* Events
* Bookings

---

# 🛠 Technologies Used

## Backend

* Flask – Web framework
* Python 3

## Frontend

* HTML5
* CSS3
* JavaScript
* jQuery – AJAX and DOM manipulation
* Bootstrap Icons – Icons and loading animations

---

# 🎨 Design Features

* Responsive layout
* Fixed navigation header
* Dynamic active navigation highlighting
* External CSS styling
* Reusable template layouts
* Scroll animations
* Responsive grid system using custom CSS
* Modern UI styling
* Smooth navigation experience

---

# ⚡ Interactive Features

## Image Slider

The website includes a JavaScript-powered image slider with:

* Automatic slide transitions
* Dots navigation
* Pause on hover
* Responsive behavior

---

# 🧠 Python Programming Concepts Demonstrated

The project demonstrates clear understanding of Python programming concepts including:

* Python lists and dictionaries
* Object-oriented programming
* Conditional statements
* Form validation
* Dynamic data manipulation
* CRUD operations
* Flask routing
* Template rendering using Jinja2

---

# 🧩 Flask Features Implemented

## Flask Routing

Dynamic routes were implemented for all pages.

## Template Inheritance

The application uses Jinja2 template inheritance with:

* `base.html`
* `{% extends %}`
* `{% block content %}`

This minimizes duplicate code and improves maintainability.

## POST Request Handling

Forms use Flask POST routes to:

* Process booking submissions
* Process newsletter subscriptions
* Handle delete operations

---

# 📁 Project Structure

```text
flask_project/
│
├── app.py
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── about.html
│   ├── services.html
│   ├── artists.html
	├── events.html
│   └── bookings.html
│
├── static/
│   ├── css/
│   │   └── styles.css
│   │
│   ├── js/
│   │   └── script.js
│   │
│   └── images/
│
├── instance/
│   └── teemusic.db
│
└── venv/
```

---

# 🚀 Running the Project

## 1. Install Flask

```bash
pip install flask
pip install flask-sqlalchemy
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

---

## 3. Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

---

## 4. Run Application

```bash
python app.py
```

---

## 5. Open Browser

Visit:

```text
http://127.0.0.1:5000/
```

---

# 🔧 Development Challenges Encountered

Several challenges were encountered during development, including:

* Understanding Flask project structure
* Configuring template inheritance
* Managing static files correctly
* Debugging Python indentation issues

These challenges were resolved through debugging, restructuring the project, and implementing Flask best practices.

---

# 📚 Learning Outcomes

Through this project, the following skills were developed:

* Flask web application development
* Python backend programming
* Front-end responsive design
* Dynamic template rendering
* CRUD functionality implementation

---

# 👨‍💻 Developer

Developed by Tefo Molemohi for academic purposes.
