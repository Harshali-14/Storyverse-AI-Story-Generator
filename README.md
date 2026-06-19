# StoryVerse AI

<div align="center">

<img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python">
<img src="https://img.shields.io/badge/Django-Web_Framework-green?style=for-the-badge&logo=django">
<img src="https://img.shields.io/badge/AI-Google_Gemini-purple?style=for-the-badge&logo=google">
<img src="https://img.shields.io/badge/Database-SQLite-orange?style=for-the-badge&logo=sqlite">
<img src="https://img.shields.io/badge/Frontend-HTML%20%7C%20CSS%20%7C%20JS-red?style=for-the-badge">

</div>


<div align="center">

## AI Powered Story Generator

Create personalized stories using Artificial Intelligence

</div>


---


https://github.com/user-attachments/assets/1dabb0c8-1de7-41ae-a58b-b399a5dfe240


# Overview


**StoryVerse AI** is an AI-powered story generation web application that transforms user imagination into creative and personalized stories.

Users can provide:

- Character
- Theme
- Keyword
- Story Length
- Age Group


The application uses **Google Gemini AI** to generate unique stories based on user preferences.


Users get a personal story library where they can:

- View stories
- Edit stories
- Delete stories
- Manage generated content


---

# Features


## AI Story Generation

Generate creative stories instantly using Google Gemini AI.


## User Authentication

Secure user registration and login system.


## Personal Story Library

Each user has their own collection of generated stories.


## Story Management

Users can:

- Create stories
- Update stories
- Delete stories
- Read previous stories


## Story Customization

Generate stories according to:

- Age group
- Story length
- Theme
- Character


## Modern UI

Includes:

- Glassmorphism design
- Responsive layout
- Smooth animations
- User-friendly interface


---

# Technology Stack


## Frontend

- HTML5
- CSS3
- JavaScript


## Backend

- Python
- Django


## Database

- SQLite


## AI Integration

- Google Gemini API


## Tools

- VS Code
- Git
- GitHub


---

# Application Workflow


```
User Input

      ↓

Django Backend

      ↓

Gemini AI API

      ↓

Generated Story

      ↓

Save Database

      ↓

User Story Library
```


---

# Project Structure


```
StoryVerse-AI/

│
├── stories/
│   │
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│
├── templates/
│   │
│   ├── base.html
│   ├── home.html
│   ├── generate.html
│   ├── library.html
│   └── result.html
│
├── static/
│
├── manage.py
│
├── requirements.txt
│
├── README.md
│
└── .gitignore

```


---

# Database Design


StoryVerse AI uses SQLite database.


## User Table


| Field | Type | Description |
|---|---|---|
| id | Integer | Unique user ID |
| username | Varchar | Username |
| email | Email | User email |
| password | Varchar | Encrypted password |
| date_joined | DateTime | Account creation date |


---

## Story Table


| Field | Type | Description |
|---|---|---|
| id | Integer | Story ID |
| user | Foreign Key | Story owner |
| title | Varchar | Story title |
| character | Varchar | Main character |
| keyword | Varchar | Story keyword |
| theme | Varchar | Story theme |
| age_group | Varchar | Age category |
| length | Varchar | Story length |
| content | Text | Generated story |
| created_at | DateTime | Creation date |
| updated_at | DateTime | Updated date |


---

# Database Relationship


```
User

 |

 | One To Many

 |

Story

```


One user can create multiple stories.


---

# Installation


## Clone Repository


```bash
git clone https://github.com/Harshali-14/Storyverse-AI-Story-Generator.git
```


## Go To Project Folder


```bash
cd Storyverse-AI-Story-Generator
```


## Create Virtual Environment


```bash
python -m venv venv
```


## Activate Environment


Windows:

```bash
venv\Scripts\activate
```


Linux/Mac:


```bash
source venv/bin/activate
```


---

# Install Dependencies


```bash
pip install -r requirements.txt
```


---

# Environment Setup


Create `.env` file


```env
GEMINI_API_KEY=your_api_key_here
```


Add your Google Gemini API key.


---

# Database Migration


Create migrations:


```bash
python manage.py makemigrations
```


Apply migrations:


```bash
python manage.py migrate
```


---

# Create Django Superuser


Create admin account:


```bash
python manage.py createsuperuser
```


Enter:


```
Username:
Email:
Password:
```


Example:


```
Username: admin
Email: admin@gmail.com
Password: ********
```


---

# Run Project


Start server:


```bash
python manage.py runserver
```


Open browser:


```
http://127.0.0.1:8000/
```


---

# Admin Dashboard


Open:


```
http://127.0.0.1:8000/admin/
```


Login with superuser credentials.


Admin can manage:


- Users
- Stories
- Database Records


---

# Future Enhancements


- Export stories as PDF
- AI generated story images
- AI voice narration
- Cloud deployment
- Favorite stories
- Story sharing
- Mobile application
- Dark mode


---

# Learning Outcomes


Through this project:


- Built Django CRUD application
- Integrated Generative AI API
- Implemented authentication
- Designed database models
- Created responsive UI
- Managed API security


---

# Author


## Harshali Kulkarni


Python Developer | Django Developer | AI Developer


---

# Support


If you like this project, give it a star on GitHub.
