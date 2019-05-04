from flask import Flask
from flask import Blueprint, request, jsonify
from app import db
from app.modules.api.models import Incident

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_api = Blueprint('api', __name__, url_prefix='/api')


@mod_api.route('/incident/<int:incident_id>', methods=['GET'])
def get_incidents(incident_id: str = "") -> jsonify:
	"""
	Retrieves a list of all incidents and returns the basic information
	for each ticket. Further API calls would be required to get further
	information.

	Args
		:incident_id (str): Unique ID for the ticket.

	Returns:
		Returns json message.
	"""
	incidents = []
	incident_results = db.session.query(Incident).all()
	for incident in incident_results:
		new_incident = {}
		new_incident['id'] = incident.id
		incidents.append(new_incident)
	return jsonify({"Data":incidents})


@mod_api.route('/incident/', methods=['POST'])
def new_incident() -> jsonify:
	"""
	Adds a new incident and returns the incident_id
	assigned.

	Returns:
		Returns incident_id of the new ticket entry.
	"""
	new_incident = Incident()
	db.session.add(new_incident)
	db.session.commit()
	return jsonify({"Ticket_ID":new_incident.id})


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