
from flask import flash, request
import sys
from flask import Flask, jsonify, redirect, render_template, url_for
from flask_migrate import Migrate
from flask_restful import Api


def create_app():
    print("Hello", file=sys.stderr)
    app = Flask(__name__)
    #app.config.from_object(Config)
    # register_extensions(app)
    # register_resources(app)
    routes(app)

    return app


# def register_extensions(app):
#     db.init_app(app)
#     migrate = Migrate(app, db)


def register_resources(app):
    api = Api(app)
def routes(app):
    @app.route('/')
    def home():
        return render_template("index.html")


if __name__ == '__main__':
    app = create_app()
    app.run('127.0.0.1', 5000)
