from flask import Flask
from flask import Blueprint, request

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_api = Blueprint('api', __name__, url_prefix='/api')


@mod_api.route('/hello', methods=['GET'])
def hello():
	"""
	Simple request to test the API is online and
    available
	"""
	return "Online"