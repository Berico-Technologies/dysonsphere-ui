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

from .assets import compile_admin_assets

# Blueprint Configuration
admin_bp = Blueprint(
    'admin_bp', __name__,
    template_folder='templates',
    static_folder='static',
    url_prefix='/admin'
)
compile_admin_assets(app)


@admin_bp.route('/dashboard', methods=['GET'])
def dashboard():
    """Admin dashboard route."""
    return render_template(
        'dashboard.html',
        title='Flask-Blueprint Tutorial | Admin Dashboard',
        template='dashboard-template account',
        body="Account")
