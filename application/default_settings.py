#  RESTRICTED COMPUTER SOFTWARE
#
#  The U.S. Government’s rights to use, modify, reproduce, release, perform, display,
#  or disclose this software are restricted in accordance with paragraph (b)(3) of DFARS
#  252.227-7014. Any reproduction of computer software or portions thereof marked
#  with this legend must also reproduce the markings. Any person, other than the U.S.
#  Government, who has been provided access to such software must promptly notify
#  Novetta, Inc.
#
#  Copyright (c) 2020 Novetta, Inc.

from os import environ

# General Config
SECRET_KEY = environ.get('SECRET_KEY')
FLASK_ENV = environ.get('FLASK_ENV', 'development')

# Flask-Assets
LESS_BIN = environ.get('LESS_BIN')
ASSETS_DEBUG = environ.get('ASSETS_DEBUG')
LESS_RUN_IN_DEBUG = environ.get('LESS_RUN_IN_DEBUG')

# Static Assets
STATIC_FOLDER = environ.get('STATIC_FOLDER')
TEMPLATES_FOLDER = environ.get('TEMPLATES_FOLDER')
COMPRESSOR_DEBUG = environ.get('COMPRESSOR_DEBUG')

# SqlAlchemy
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
