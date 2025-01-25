""" COMPILE STATIC ASSESTS """
from flask import Flask
from flask_assets import Bundle, Environment


def compile_static_assets(app: Flask):
    """ COMPILE ALL ASSET BUNDLES AT TOP LEVEL """
    assets = Environment(app)
    compile_stylesheets(assets, app)
    compile_javascript(assets, app)
    compile_auth_stylesheets(assets, app)

#-------------------------------Stylesheets and javascripts for home------------------------------------#
def compile_stylesheets(assets: Environment, app: Flask):
    """ GENERATE CSS AT TOP LEVEL BY SOURCE"""
    assets.auto_build = True
    assets.debug = False
    # Stylesheets Bundle
    stylesheet_bundle_home = Bundle(
        "../static/src/less/global.less",
        "../static/src/less/home_vars.less",
        "../static/src/less/home.less",
        "../static/src/less/main.less",
        "../static/src/less/navigation.less", # Source
        filters="less,cssmin",
        output="dist/css/home.css", # Output file
        extra={"rel": "stylesheet/less"},
    )

    # Register assets
    assets.register("styles_home", stylesheet_bundle_home)

    # Build assets in development mode
    if app.config['ENVIRONMENT'] != 'production':
        with app.app_context():
            stylesheet_bundle_home.build(force=True)

def compile_javascript(assets: Environment, app: Flask):
    """ BUNDLE AND BUILD JS FILES """

    # JavaScript Bundle
    js_bundle_main = Bundle(
        "src/js/alert.js",
        filters="jsmin", output="dist/js/home.min.js")

    # Register assets
    assets.register("js_home", js_bundle_main)


    # Build assets in development mode
    if app.config['ENVIRONMENT'] != 'production':
        with app.app_context():
            js_bundle_main.build(force=True)

#-------------------------------Stylesheets and javascript for auth------------------------------------#

def compile_auth_stylesheets(assets: Environment, app: Flask):
    """ GENERATE CSS AT TOP LEVEL BY SOURCE"""
    assets.auto_build = True
    assets.debug = False
    # Stylesheets Bundle
    stylesheet_bundle_auth = Bundle(
        "../static/src/less/auth.less",# Source
        filters="less,cssmin",
        output="dist/css/auth.css", # Output file
        extra={"rel": "stylesheet/less"},
    )
    # Register assets
    assets.register("styles_auth", stylesheet_bundle_auth)

    # Build assets in development mode
    if app.config['ENVIRONMENT'] != 'production':
        with app.app_context():
            stylesheet_bundle_auth.build(force=True)

def compile_auth_javascript(assets: Environment, app: Flask):
    """ BUNDLE AND BUILD JS FILES """

    # JavaScript Bundle
    js_bundle_auth = Bundle(
        "src/js/alert.js",
        "../src/js/auth.js",
        filters="jsmin", output="dist/js/auth.min.js")

    # Register assets
    assets.register("js_auth", js_bundle_auth)


    # Build assets in development mode
    if app.config['ENVIRONMENT'] != 'production':
        with app.app_context():
            js_bundle_auth.build(force=True)
