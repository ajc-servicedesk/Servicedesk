from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from celery import Celery


app = Flask(__name__)
app.config.from_object('config')

from modules.api.views import mod_api
from modules.docs.views import mod_docs
# Register blueprint(s)
app.register_blueprint(mod_api)
app.register_blueprint(mod_docs)

@app.errorhandler(404)
def not_found(error):
    """
    Ran if no view is found for the url.
    Nothing is done except '404' returned
    """
    return "404"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
