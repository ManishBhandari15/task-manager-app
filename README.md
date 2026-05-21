# Task Manager App

A full-stack task management web application built with Python Flask and PostgreSQL.

## Live Demo
https://task-manager-app-1-o2v4.onrender.com

## Features
- Create tasks with title, description and priority level
- View all tasks in a clean organized layout
- Mark tasks as complete or incomplete
- Edit existing tasks
- Delete tasks
- Priority levels — Low, Medium, High
- Responsive design with Bootstrap

## Tech Stack
- **Backend:** Python, Flask, SQLAlchemy
- **Database:** PostgreSQL
- **Frontend:** HTML, CSS, Bootstrap 5, Jinja2
- **Version Control:** Git, GitHub
- **Deployment:** Render

## Installation and Setup

### Prerequisites
- Python 3.13+
- PostgreSQL
- Git

### Steps

1. Clone the repository
   git clone https://github.com/ManishBhandari15/task-manager-app.git
2. Navigate to project folder
3. Create virtual environment
4. Install dependencies
5. Create a `.env` file in the root folder
   DATABASE_URL=postgresql://postgres:yourpassword@localhost:5432/taskmanager
SECRET_KEY=yoursecretkey
6. Run the application
7. Open your browser and go to
   http://127.0.0.1:5000
## Database Schema

### Tasks Table
| Column | Type | Description |
|---|---|---|
| id | Integer | Primary key, auto generated |
| title | String | Task title, required |
| description | Text | Task details, optional |
| complete | Boolean | Task status, default false |
| priority | String | low, medium or high |
| created_at | DateTime | Auto set on creation |

## Screenshots
I will add later.

## Author
**Manish Bhandari**
- GitHub: [@ManishBhandari15](https://github.com/ManishBhandari15)
- LinkedIn:  I will add later.

## License
This project is open source and available under the [MIT License](LICENSE).
