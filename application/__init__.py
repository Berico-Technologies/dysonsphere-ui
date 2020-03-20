#  RESTRICTED COMPUTER SOFTWARE
#
#  The U.S. Government’s rights to use, modify, reproduce, release, perform, display, or disclose this software are
#  restricted in accordance with paragraph (b)(3) of DFARS 252.227-7014. Any reproduction of computer software or
#  portions thereof marked with this legend must also reproduce the markings. Any person, other than the U.S. Government,
#  who has been provided access to such software must promptly notify Novetta, Inc.
#
#  Copyright (c) 2020 Novetta, Inc.

from flask import Flask
from flask_menu import Menu
from flask_redis import FlaskRedis
from flask_sqlalchemy import SQLAlchemy

# Globally accessible libraries
from application import auth

db = SQLAlchemy()
r = FlaskRedis()
menu = Menu()


def create_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('application.default_settings')
    app.config.from_pyfile('application.cfg', silent=True)

    # Initialize Plugins
    db.init_app(app)
    r.init_app(app)
    menu.init_app(app)

    with app.app_context():
        # Include our Routes
        from .admin import admin_routes
        from .main import main_routes

        # Register Blueprints
        app.register_blueprint(admin_routes.admin_bp)
        app.register_blueprint(main_routes.main_bp)

        return app
