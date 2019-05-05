from flask import Flask
from flask import Blueprint, request, jsonify
from app import db
from app.modules.api.models import *

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_api = Blueprint('api', __name__, url_prefix='/api')

@mod_api.route('/incident/', methods=['GET'])
@mod_api.route('/incident/<int:incident_id>', methods=['GET'])
def get_incidents(incident_id: str = "") -> jsonify:
	"""
	Retrieve a list of all incidents (default=last100).
	Pagination on the request for all incidents.
	Retrieve json data on an incident and return. ID required.

	Args
		:incident_id (str): Unique ID for the ticket. (Optional)

	Returns:
		Returns json message.

		{
			"Data": {
				"id": "1"
			}
		}

	"""
	incidents = []
	if incident_id != "":
		print("Do the search with the ID")
		incident_results = db.session.query(Incident).filter_by(id = incident_id).all()
	else:
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


@mod_api.route('/agent/', methods=['GET'])
@mod_api.route('/agent/<int:agent_id>', methods=['GET'])
def get_agents(agent_id: str = "") -> jsonify:
	"""
	Retrieve a list of all agents.
	Filter on the url to get agents for a group (e.g. /agent?group=examplegroup)
	Retrieve json data on an agent and return. ID required.

	Args
		:agent_id (str): Unique ID for the ticket. (Optional)

	Returns:
		Returns json message.

		{
			"Data": [
				{
				"id": 1
				}
			]
		}
	"""
	agents = []
	if agent_id != "":
		print("Do the search with the ID")
		agent_results = db.session.query(Agent).filter_by(id = agent_id).all()
	else:
		agent_results = db.session.query(Agent).all()
	for agent in agent_results:
		new_agent = {}
		new_agent['id'] = agent.id
		new_agent['name'] = agent.name
		agents.append(new_agent)
	return jsonify({"Data":agents})


@mod_api.route('/agent/', methods=['POST'])
def new_agent() -> jsonify:
	"""
	Adds a new agent and returns the agent_id
	assigned.

	Returns:
		Returns agent_id of the new agent.
	"""
	new_agent = Agent()
	db.session.add(new_agent)
	db.session.commit()
	return jsonify({"Agent_ID":new_agent.id})


@mod_api.route('/department/', methods=['GET'])
@mod_api.route('/department/<int:department_id>', methods=['GET'])
def get_department(department_id: str = "") -> jsonify:
	"""
	Retrieve a list of all departments.
	Retrieve json data on an department and return. ID required.

	Args
		:department_id (str): Unique ID for the ticket. (Optional)

	Returns:
		Returns json message.
	"""
	departments = []
	if department_id != "":
		print("Do the search with the ID")
		department_results = db.session.query(RequesterDepartment).filter_by(id = department_id).all()
	else:
		department_results = db.session.query(RequesterDepartment).all()
	for department in department_results:
		new_department = {}
		new_department['id'] = department.id
		new_department['name'] = department.name
		departments.append(new_department)
	return jsonify({"Data":departments})


@mod_api.route('/department/', methods=['POST'])
def new_department() -> jsonify:
	"""
	Adds a new department and returns the agent_id
	assigned.

	Returns:
		Returns agent_id of the new department.
	"""
	new_department = RequesterDepartment()
	db.session.add(new_department)
	db.session.commit()
	return jsonify({"Department_ID":new_department.id})


@mod_api.route('/category/', methods=['GET'])
def get_category() -> jsonify:
	"""
	Retrieve a list of all categories.

	Returns:
		Returns name and id of category
	"""
	categories = []
	category_results = db.session.query(IncidentCategories).all()
	for category in category_results:
		new_category = {}
		new_category['id'] = category.id
		new_category['name'] = category.name
		categories.append(new_category)
	return jsonify({"Data":categories})


@mod_api.route('/department/', methods=['POST'])
def new_category() -> jsonify:
	"""
	Adds a new category and returns the Category_ID
	assigned.

	Returns:
		Returns Category_ID, name of the new category.
	"""
	new_category = RequesterDepartment()
	db.session.add(new_category)
	db.session.commit()
	return jsonify({"Category_ID":new_category.id})