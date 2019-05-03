from flask import Flask, render_template
from celery import Celery


application = Flask(__name__)
application.config.from_object('config')

from app.modules.api.views import mod_api
from app.modules.docs.views import mod_docs
# Register blueprint(s)
application.register_blueprint(mod_api)
application.register_blueprint(mod_docs)

@application.errorhandler(404)
def not_found(error):
    """
    Ran if no view is found for the url.
    Nothing is done except '404' returned
    """
    return "404"

if __name__ == "__main__":
    application.run(host='0.0.0.0')
