# 💸 Expense Tracker – Full Stack Web App

A full-stack Expense Tracker application built using **Flask**, **PostgreSQL**, and **Vanilla JavaScript**, deployed on **Render** (backend) and **Netlify** (frontend).

---

## 🚀 Live Demo

🔗 **Frontend (Netlify)**  
https://extraordinary-brigadeiros-28bb78.netlify.app

🔗 **Backend API (Render)**  
https://expense-tracker-backend-cpc6.onrender.com

---

## 🧩 Features

- User Registration & Login (JWT Authentication)
- Secure Expense CRUD Operations
- Category-wise Expense Tracking
- Total Expense Summary
- Responsive UI
- REST API Architecture
- Production Deployment

---

## 🛠️ Tech Stack

### Frontend
- HTML5
- CSS3
- JavaScript (ES6)
- Netlify (Hosting)

### Backend
- Python
- Flask
- Flask-SQLAlchemy
- JWT Authentication
- PostgreSQL
- Render (Hosting)

---

## 📁 Project Structure

Expense-tracker/
│
├── backend/
│ ├── app.py
│ ├── config.py
│ ├── routes/
│ │ ├── auth_routes.py
│ │ └── expense_routes.py
│ ├── database/
│ │ ├── db.py
│ │ └── models.py
│ └── utils/
│ └── auth_middleware.py
│
├── frontend/
│ ├── index.html
│ ├── login.html
│ ├── register.html
│ ├── dashboard.html
│ ├── styles.css
│ ├── login.js
│ ├── register.js
│ ├── dashboard.js
│ └── _redirects
