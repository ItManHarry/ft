from flask import Flask
def create_app():
    app = Flask('com')
    @app.route('/')
    def index():
        return '<h1>Flask basic project template!</h1>'
    return app