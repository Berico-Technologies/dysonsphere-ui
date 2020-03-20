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

from flask_assets import Environment, Bundle


def compile_admin_assets(app):
    """Configure logged-in asset bundles."""
    assets = Environment(app)
    Environment.auto_build = True
    Environment.debug = False
    # Stylesheets Bundle
    less_bundle = Bundle(
        'bower_components/startbootstrap-sb-admin/css/sb-admin-2.css',
        filters='cssmin',
        output='dist/css/account.css',
        extra={'rel': 'stylesheet/less'}
    )
    # Register assets
    assets.register('less_all', less_bundle)
    # Build assets in development mode
    if app.config['FLASK_ENV'] == 'development':
        less_bundle.build(force=True)
