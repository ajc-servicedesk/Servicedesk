from flask import Flask
from flask import Blueprint, request, jsonify

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_api = Blueprint('api', __name__, url_prefix='/api')


@mod_api.route('/hello', methods=['GET'])
def hello():
	"""
	Simple request to test the API is online and
    available
	"""
	return "Online"

@mod_api.route('/tickets', methods=['GET'])
def get_tickets(ticket_id: str) -> jsonify:
	"""
	Retrieves a list of all tickets and returns the basic information
	for each ticket. Further API calls would be required to get further
	information.
	
	Args
		:ticket_id (str): Unique ID for the ticket.

	Returns:
		Returns json message.
	"""
	return jsonify({"test":"test"})