Event & Club Management System

A web-based Event and Club Management System developed using Flask and MongoDB to streamline event organization, participant registration, and administrative management in academic institutions.

This project provides a centralized platform for managing events with role-based access for users and administrators.

Overview

Student organizations and campus clubs often rely on manual processes for event registrations and communication. This leads to inefficiency, data inconsistency, and limited visibility.

This system addresses these challenges by offering:

Structured event management

Digital registration

Centralized participant tracking

Administrative control panel

The application is designed as a functional prototype suitable for academic projects, hackathons, and learning purposes.

Key Features
User Features

View available events

Register for events

Track registration status

Responsive web interface

Admin Features

Secure admin login

Create and manage events

View registered participants

Approve or reject registrations

Monitor system activity

System Features

REST-based API architecture

MongoDB integration

Session-based authentication

Clean and modular design

Technology Stack
Layer	Technology
Frontend	HTML, CSS, Bootstrap
Backend	Python (Flask)
Database	MongoDB
Tools	Git, GitHub
System Architecture
Client (Browser)
     ↓
Flask Web Server
     ↓
MongoDB Database


The frontend communicates with backend APIs implemented using Flask. All persistent data is stored in MongoDB.

Project Structure
event-management-system/
├── app.py
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── dashboard.html
│   ├── index.html
│   ├── events.html
│   ├── admin.html
│   └── login.html
└── README.md

Future Enhancements

User authentication system

Email/SMS notifications

Certificate generation

Cloud deployment

Payment integration

Admin analytics dashboard

Mobile application support

Author

Abuzer
Farhan Sidduqui - https://github.com/fsid908
Anamika Singh - https://github.com/anamika-singh9
Computer Science Student
Aspiring Full-Stack Developer
