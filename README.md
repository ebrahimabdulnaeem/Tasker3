# Task Management Web Application

A web-based task management application built with Flask and SQLite, allowing users to manage projects and tasks efficiently.

## Features

- User authentication (register, login, logout)
- Project management (create, read, update, delete)
- Task management within projects (create, read, update, delete)
- Task prioritization and status tracking
- Due date management for tasks

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd Tasker3
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
- Copy `.env.example` to `.env`
- Update the values in `.env` with your configuration

5. Initialize the database:
```bash
flask db init
flask db migrate
flask db upgrade
```

## Running the Application

1. Start the Flask development server:
```bash
flask run
```

2. Access the application at `http://localhost:5000`

## API Endpoints

### Authentication
- POST `/api/auth/register` - Register a new user
- POST `/api/auth/login` - Login user
- GET `/api/auth/logout` - Logout user
- GET `/api/auth/me` - Get current user info

### Projects
- GET `/api/projects` - List all projects
- POST `/api/projects` - Create a new project
- GET `/api/projects/<id>` - Get project details
- PUT `/api/projects/<id>` - Update project
- DELETE `/api/projects/<id>` - Delete project

### Tasks
- POST `/api/tasks` - Create a new task
- GET `/api/tasks/<id>` - Get task details
- PUT `/api/tasks/<id>` - Update task
- DELETE `/api/tasks/<id>` - Delete task
- GET `/api/tasks/project/<id>` - Get all tasks for a project

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 