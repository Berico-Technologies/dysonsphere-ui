
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


def compile_main_assets(app):
    """Configure landing asset bundles."""
    assets = Environment(app)
    Environment.auto_build = True
    Environment.debug = False
    # Stylesheets Bundle
    css_bundle = Bundle(
        'bower_components/startbootstrap-sb-admin/vendor/fontawesome-free/css/all.min.css',
        'bower_components/startbootstrap-sb-admin/css/sb-admin-2.css',
        'bower_components/startbootstrap-sb-admin/vendor/datatables/dataTables.bootstrap4.min.css',
        filters='cssmin',
        output='dist/css/main.css',
        extra={'rel': 'stylesheet/less'}
    )
    # JavaScript Bundle
    js_bundle = Bundle(
        'bower_components/jquery/dist/jquery.js',
        'bower_components/startbootstrap-sb-admin/js/sb-admin-2.js',
        'bower_components/startbootstrap-sb-admin/vendor/bootstrap/js/bootstrap.bundle.js',
        'bower_components/startbootstrap-sb-admin/vendor/jquery-easing/jquery.easing.min.js',
        'bower_components/startbootstrap-sb-admin/vendor/datatables/jquery.dataTables.min.js',
        'bower_components/startbootstrap-sb-admin/vendor/datatables/dataTables.bootstrap4.min.js',
        'bower_components/startbootstrap-sb-admin/js/demo/datatables-demo.js',
        filters='jsmin',
        output='dist/js/main.min.js'
    )
    dashboard_bundle = Bundle(
        'bower_components/startbootstrap-sb-admin/vendor/chart.js/Chart.min.js',
        'bower_components/startbootstrap-sb-admin/js/demo/chart-area-demo.js',
        'bower_components/startbootstrap-sb-admin/js/demo/chart-pie-demo.js',
        filters='jsmin',
        output='dist/js/dashboard.min.js'
    )
    # Register assets
    assets.register('css_all', css_bundle)
    assets.register('js_all', js_bundle)
    assets.register('dashboard_all', dashboard_bundle)
    # Build assets in development mode
    if app.config['FLASK_ENV'] == 'development':
        css_bundle.build(force=True)
        js_bundle.build()
        dashboard_bundle.build()
