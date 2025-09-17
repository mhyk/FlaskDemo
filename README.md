# Flask Demo Project - User Management System

A comprehensive Flask web application demonstrating modern web development practices with user authentication, CRUD operations, and responsive design.

## 🎯 Project Overview

This is a Flask 3.1.2 web application built for educational purposes, showcasing:
- User registration and authentication
- PostgreSQL database integration
- Blueprint-based modular architecture
- Bootstrap 5 responsive frontend
- MVC design pattern implementation
- Form handling with WTForms
- Session management with Flask-Login

## 🚀 Features

- **User Authentication**: Secure login/logout with session management
- **User Management**: Create, read, update, and delete users
- **Responsive Design**: Mobile-friendly Bootstrap 5 interface
- **Form Validation**: Server-side validation with WTForms
- **Flash Messages**: User feedback for actions
- **Modal Editing**: Edit users with Bootstrap modals
- **Security**: CSRF protection and password hashing

## 🛠️ Technology Stack

- **Backend**: Flask 3.1.2, Python 3.10
- **Database**: PostgreSQL with psycopg2
- **Frontend**: Bootstrap 5, Jinja2 templates
- **Forms**: Flask-WTF, WTForms
- **Authentication**: Flask-Login
- **Environment**: Pipenv for dependency management

## 📋 Prerequisites

- Python 3.10 or higher
- PostgreSQL 12 or higher
- Pipenv (recommended) or pip

## 🔧 Installation & Setup

### 1. Clone the Repository
```bash
git clone <repository-url>
cd FlaskDemo
```

### 2. Install Dependencies
```bash
# Using Pipenv (recommended)
pipenv install
pipenv shell

# Or using pip
pip install -r requirements.txt
```

### 3. Database Setup

#### Create PostgreSQL Database
```bash
createdb ccc181
```

#### Import Database Schema
```bash
psql -d ccc181 -f postgresql_schema.sql
```

### 4. Environment Configuration

Copy the sample environment file and configure your settings:
```bash
cp .env_sample .env
```

Edit `.env` with your database credentials:
```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=ccc181
DB_USERNAME=your_username
DB_PASSWORD=your_password
SECRET_KEY=your-secret-key-here
BOOTSTRAP_SERVE_LOCAL=True
```

### 5. Run the Application
```bash
# Using Flask CLI (recommended)
flask run

# Or using Python directly
python run.py
```

The application will be available at `http://localhost:5000`

## 🗂️ Project Structure

```
FlaskDemo/
├── app/                    # Main application package
│   ├── __init__.py        # Application factory
│   ├── database.py        # Database connection management
│   ├── models.py          # Database models (M in MVC)
│   ├── user/              # User blueprint
│   │   ├── __init__.py    # Blueprint registration
│   │   ├── controller.py  # Route handlers (C in MVC)
│   │   └── forms.py       # WTForms definitions
│   ├── templates/         # Jinja2 templates (V in MVC)
│   │   ├── layouts/       # Base templates
│   │   ├── index.html     # User management page
│   │   ├── login.html     # Login page
│   │   └── signup.html    # User registration page
│   └── static/            # CSS, JS, images
│       ├── css/
│       └── js/
├── postgresql_schema.sql  # Database schema
├── run.py                 # Application entry point
├── .flaskenv             # Flask environment variables
├── .env_sample           # Environment template
├── Pipfile               # Dependencies
└── README.md             # This file
```

## 🏗️ Architecture

### MVC Pattern
- **Model**: `app/models.py` - Data layer and business logic
- **View**: `app/templates/` - Presentation layer (HTML templates)
- **Controller**: `app/user/controller.py` - Request handling and routing

### Blueprint Organization
- Modular design using Flask blueprints
- User functionality organized in `app/user/` blueprint
- Easy to extend with additional features

## 📊 Database Schema

### Users Table
```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    user_password VARCHAR(32) NOT NULL  -- MD5 hash
);
```

### User Info Table
```sql
CREATE TABLE user_info (
    id SERIAL PRIMARY KEY,
    fullname VARCHAR(100),
    address TEXT,
    birthday DATE,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE
);
```

## 🔐 Default User Accounts

The application comes with sample user accounts for testing:

| Username | Password | Email |
|----------|----------|-------|
| admin | admin123 | admin@example.com |
| user1 | password | user1@example.com |

## 🎮 Usage

### Login
1. Navigate to `http://localhost:5000`
2. Use credentials: `admin` / `admin123`
3. Access the user management dashboard

### User Management
- **View Users**: Main dashboard shows all registered users
- **Add User**: Click "Add New User" button
- **Edit User**: Click "Edit" button in user table (opens modal)
- **Delete User**: Click "Delete" button (requires confirmation)

### Logout
- Click on your username in the navbar
- Select "Logout" from the dropdown menu

## 🔧 Development

### Running in Development Mode
The application is configured for development in `.flaskenv`:
```env
FLASK_APP=app
FLASK_DEBUG=true
FLASK_RUN_PORT=5000
```

### Adding New Features
1. Create new blueprints in `app/` directory
2. Register blueprints in `app/__init__.py`
3. Follow MVC pattern for organization
4. Add templates in `app/templates/`

### Database Changes
1. Modify `postgresql_schema.sql`
2. Update models in `app/models.py`
3. Re-import schema: `psql -d ccc181 -f postgresql_schema.sql`

## 🛡️ Security Features

- **CSRF Protection**: Forms protected against cross-site request forgery
- **SQL Injection Prevention**: Parameterized queries
- **Session Security**: Flask-Login secure session management
- **Password Hashing**: MD5 hashing (demo purposes)
- **Route Protection**: Login required decorators
- **Environment Variables**: Sensitive data externalized

## 🧪 Testing

### Manual Testing
1. Test user registration and login
2. Verify CRUD operations work correctly
3. Test form validation
4. Check responsive design on different devices

### Sample Test Scenarios
- Create new user with valid data
- Try login with invalid credentials
- Edit existing user information
- Delete user and verify cascading deletes

## 📝 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | User management dashboard |
| GET/POST | `/login` | User login |
| GET | `/logout` | User logout |
| GET/POST | `/user/register` | User registration |
| POST | `/user/edit` | Edit user (AJAX) |
| POST | `/user/delete` | Delete user (AJAX) |

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/new-feature`)
3. Commit changes (`git commit -am 'Add new feature'`)
4. Push to branch (`git push origin feature/new-feature`)
5. Create Pull Request

## 📚 Learning Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [PostgreSQL Documentation](https://postgresql.org/docs/)
- [Bootstrap Documentation](https://getbootstrap.com/docs/)
- [Flask-Login Documentation](https://flask-login.readthedocs.io/)

## 🔍 Troubleshooting

### Common Issues

**Database Connection Error**
- Verify PostgreSQL is running
- Check database credentials in `.env`
- Ensure database `ccc181` exists

**Import Error: No module named 'flask'**
- Activate virtual environment: `pipenv shell`
- Install dependencies: `pipenv install`

**Permission Denied for Table**
- Grant privileges: `GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO your_username;`

**CSRF Token Missing**
- Ensure forms include `{{ form.hidden_tag() }}`
- Check CSRF meta tag in templates

## 📄 License

This project is for educational purposes. Feel free to use and modify for learning.

## 👨‍💻 Author

Created for CCC181 Web Development course - Flask demonstration project.

## 📧 Support

For questions or issues, please create an issue in the repository or contact the course instructor.

---

**Note**: This is a demonstration project for educational purposes. For production use, consider implementing additional security measures such as bcrypt password hashing, HTTPS, rate limiting, and comprehensive error handling.