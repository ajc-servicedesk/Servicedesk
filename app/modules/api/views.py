from flask import Flask
from flask import Blueprint, request, jsonify

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_api = Blueprint('api', __name__, url_prefix='/api')


@mod_api.route('/tickets', methods=['GET'])
def get_tickets(ticket_id: str = "") -> jsonify:
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


@mod_api.route('/agents', methods=['GET'])
def get_agents(agent_id: str = "") -> jsonify:
	"""
	Retrieves a list of all agents and returns the basic information
	for each agent. Further API calls would be required to get further
	information.

	Args
		:agent_id (str): Unique ID for the ticket.

	Returns:
		Returns json message.
	"""
	return jsonify({"test":"test"})