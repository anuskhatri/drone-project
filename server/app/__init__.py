from flask import Flask
def create_app():
    app = Flask(__name__)
    # Initialize extensions (if any) here
    # e.g., db.init_app(app)

    # Import and register your blueprint modules here
    from .routes.flight import flight
    app.register_blueprint(flight)

    return app
