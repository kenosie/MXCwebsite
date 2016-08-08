from flask import Flask, render_template, flash, redirect, make_response, request, session
from flask_wtf.csrf import CsrfProtect
import logging
import subprocess
import traceback
import os

log_formatter = logging.Formatter('''
Message type:       %(levelname)s
Location:           %(pathname)s:%(lineno)d
Module:             %(module)s
Function:           %(funcName)s
Time:               %(asctime)s
Message:
%(message)s
''')

csrf = CsrfProtect()

def create_app(environment):
    app = Flask(__name__)
    app.config.from_pyfile("config/{}.py".format(environment))

    csrf.init_app(app)
    
    @app.route("/")
    def home_page():
        return render_template("index.html")

    @app.route("/favicon.ico")
    def favicon():
        return app.send_static_file("icon/favicon.ico")

    return app

if __name__ == '__main__':
    create_app("dev").run(port=5000, debug=True)
