from flask import Flask
from flask import Blueprint, request, jsonify
from app import db
from app.modules.api.models import Tickets

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_api = Blueprint('api', __name__, url_prefix='/api')


@mod_api.route('/tickets/<int:ticket_id>', methods=['GET'])
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
	tickets = []
	ticket_results = db.session.query(Tickets).all()
	for ticket in ticket_results:
		new_ticket = {}
		new_ticket['id'] = ticket.id
		tickets.append(new_ticket)
	return jsonify({"Data":tickets})


@mod_api.route('/tickets', methods=['POST'])
def new_ticket() -> jsonify:
	"""
	Adds a new ticket and returns the ticket_id
	assigned.

	Returns:
		Returns ticket_id of the new ticket entry.
	"""
	new_ticket = Tickets()
	db.session.add(new_ticket)
	db.session.commit()
	return jsonify({"Ticket_ID":new_ticket.id})


@mod_api.route('/agents/<int:agent_id>', methods=['GET'])
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