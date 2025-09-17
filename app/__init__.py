from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from config import DB_USERNAME, DB_PASSWORD, DB_NAME, DB_HOST, DB_PORT, SECRET_KEY, BOOTSTRAP_SERVE_LOCAL
from flask_wtf.csrf import CSRFProtect
from . import database

bootstrap = Bootstrap()
login_manager = LoginManager()

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=SECRET_KEY,
        DATABASE_URL=f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}",
        #BOOTSTRAP_SERVE_LOCAL=BOOTSTRAP_SERVE_LOCAL
    )
    bootstrap.init_app(app)
    CSRFProtect(app)
    database.init_app(app)

    login_manager.init_app(app)
    login_manager.login_view = 'user.login'
    login_manager.login_message = 'Please log in to access this page.'

    from .user import user_bp as user_blueprint
    app.register_blueprint(user_blueprint)

    # User loader callback for Flask-Login
    @login_manager.user_loader
    def load_user(user_id):
        from .models import Users
        return Users.get_by_id(user_id)

    return app
