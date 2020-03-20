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

from flask import Blueprint, render_template
from flask import current_app as app
from flask_menu import register_menu

from .assets import compile_main_assets

# Blueprint Configuration
main_bp = Blueprint(
    'main_bp', __name__,
    template_folder='templates',
    static_folder='static'
)
compile_main_assets(app)


@main_bp.route('/', methods=['GET'])
@register_menu(main_bp, '.', 'Dashboard')
def home():
    """Homepage route."""
    return render_template(
        'index.html',
        title='DysonSphere Admin | Home',
        template='home-template main',
        body="Home"
    )


@main_bp.route('/tables', methods=['GET'])
@register_menu(main_bp, '.tables', 'Tables', icon='fa-table')
def tables():
    """Tables route."""
    return render_template(
        'tables.html',
        title='Tables',
        template='tables-template main',
        body="Tables"
    )


@main_bp.route('/about', methods=['GET'])
@register_menu(main_bp, '.about', 'About', icon='fa-info')
def about():
    """About page route."""
    return render_template(
        'tables.html',
        title='DysonSphere Admin | About',
        template='about-template main',
        body="About"
    )
