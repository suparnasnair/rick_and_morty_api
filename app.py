# module imports
from flask import Flask
from flask_graphql import GraphQLView

from models import db_session
from schema import schema


def create_app(config_file):
    """
    The application factory to create multiple instances of Flask app

    :param config_file: the config file used for Flask
    :return: the application instance
    """
    # initialize the Flask app and get the configuration from file
    app = Flask(__name__)
    app.config.from_pyfile(config_file)

    app.add_url_rule(
        '/graphql',
        view_func=GraphQLView.as_view(
            'graphql',
            schema=schema,
            graphiql=True
        )
    )

    @app.route('/')
    def index():
        """
        This route servers as an initial endpoint.
        """
        return "<h1>Hi there!</h1>"

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        """
        This method re-allocates the memory for db
        when the app is closed.
        """
        db_session.remove()
    return app


if __name__ == '__main__':
    """
    The main entry point for this Flask application
    """
    # create Flask app from the specified configuration file
    app = create_app('config.py')
    app.run()