from flask import Flask
from flask import Blueprint, request, jsonify
from app import db
from app.modules.api.models import *

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_api = Blueprint('api', __name__, url_prefix='/api')

@mod_api.route('/incident/', methods=['GET'])
@mod_api.route('/incident/<incident_id>', methods=['GET'])
def get_incidents(incident_id: str = "") -> jsonify:
	"""
	Retrieve a list of all incidents (default=last100).
	Pagination on the request for all incidents.
	Retrieve json data on an incident and return. ID required.

	Args
		:incident_id (str): Unique ID for the ticket. (Optional)

	Returns:
		Returns json message.

	"""
	incidents = []
	if incident_id != "":
		incident_results = db.session.query(Incident).filter_by(id = incident_id).all()
	else:
		incident_results = db.session.query(Incident).all()
	for incident in incident_results:
		new_incident = {}
		new_incident['id'] = incident.id
		try:
			new_incident['status'] = incident.status[0].name
		except:
			pass
		new_incident['subject'] = incident.subject
		new_incident['description'] = incident.description
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
	post_data = request.json
	print(post_data)
	if 'incident' not in post_data:
		return jsonify({"Error": "No incident data"})
	print("3")
	print(post_data['incident'])
	if 'status' in post_data['incident']:
		try:
			status1 = db.session.query(IncidentStatus).filter_by(id=post_data['incident']['status']).one()
			new_incident.status.append(status1)
			db.session.commit()
		except:
			return jsonify({"Error": "couldn't find the status"})

	if 'priority' in post_data['incident'] and post_data['incident']['priority'] != '':
		new_incident.priority = post_data['incident']['priority']

	if 'agent_group' in post_data['incident'] and post_data['incident']['agent_group'] != '':
		new_incident.agent_group = post_data['incident']['agent_group']

	if 'agent_assigned' in post_data['incident'] and post_data['incident']['agent_assigned'] != '':
		new_incident.agent_assigned = post_data['incident']['agent_assigned']

	if 'department' in post_data['incident'] and post_data['incident']['department'] != '':
		new_incident.department = post_data['incident']['department']

	if 'category' in post_data['incident'] and post_data['incident']['category'] != '':
		new_incident.category = post_data['incident']['category']

	if 'sub_category' in post_data['incident'] and post_data['incident']['sub_category'] != '':
		new_incident.sub_category = post_data['incident']['sub_category']

	if 'requester' in post_data['incident'] and post_data['incident']['requester'] != '':
		new_incident.requester = post_data['incident']['requester']

	if 'subject' in post_data['incident'] and post_data['incident']['subject'] != '':
		new_incident.subject = post_data['incident']['subject']

	if 'description' in post_data['incident'] and post_data['incident']['description'] != '':
		new_incident.description = post_data['incident']['description']
	db.session.add(new_incident)
	db.session.commit()
	return jsonify({"Incident_ID":new_incident.id})


@mod_api.route('/agent/', methods=['GET'])
@mod_api.route('/agent/<agent_id>', methods=['GET'])
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
		new_agent['email_address'] = agent.email_address
		agents.append(new_agent)
	return jsonify({"Data":agents})


@mod_api.route('/agent/', methods=['POST'])
def new_agent() -> jsonify:
	"""
	Adds a new agent and returns the agent_id
	assigned.

	Requires data sent as JSON
	Name
	email_address

	Returns:
		Returns agent_id of the new agent.
	"""
	new_agent = Agent()
	post_data = request.json
	print(post_data)
	new_agent.name = post_data['agent']['name']
	new_agent.email_address = post_data['agent']['email_address']
	db.session.add(new_agent)
	db.session.commit()
	return jsonify({"Agent_ID":new_agent.id})


@mod_api.route('/agent/<agent_id>', methods=['DELETE'])
def delete_agent(agent_id: str = "") -> jsonify:
	"""
	Deletes the agent associated with the id passed in
	the url

	Returns the id of the agent deleted
	"""
	agent = db.session.query(Agent).filter_by(id=agent_id).one()
	id = agent.id
	db.session.delete(agent)
	db.session.commit()
	return jsonify({"Agent_ID":id})


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
	Adds a new department and returns the department_id
	assigned.

	Returns:
		Returns department_id of the new department.
	"""
	new_department = RequesterDepartment()
	db.session.add(new_department)
	db.session.commit()
	return jsonify({"Department_ID":new_department.id})


@mod_api.route('/department/<department_id>', methods=['DELETE'])
def delete_department(department_id: str = "") -> jsonify:
	"""
	Deletes the department associated with the id passed in
	the url

	Returns the id of the department deleted
	"""
	department = db.session.query(RequesterDepartment).filter_by(id=department_id).one()
	id = department.id
	db.session.delete(department)
	db.session.commit()
	return jsonify({"department_id":id})


@mod_api.route('/category/', methods=['GET'])
def get_category() -> jsonify:
	"""
	Retrieve a list of all categories.

	Returns:
		Returns name and id of category
	"""
	categories = []
	category_results = db.session.query(IncidentCategory).all()
	for category in category_results:
		new_category = {}
		new_category['id'] = category.id
		new_category['name'] = category.name
		categories.append(new_category)
	return jsonify({"Data":categories})


@mod_api.route('/category/', methods=['POST'])
def new_category() -> jsonify:
	"""
	Adds a new category and returns the Category_ID
	assigned.

	Returns:
		Returns Category_ID, name of the new category.
	"""
	new_category = IncidentCategory()
	db.session.add(new_category)
	db.session.commit()
	return jsonify({"Category_ID":new_category.id})


@mod_api.route('/category/<category_id>', methods=['DELETE'])
def delete_category(category_id: str = "") -> jsonify:
	"""
	Deletes the category associated with the id passed in
	the url

	Returns the id of the category deleted
	"""
	category = db.session.query(IncidentCategory).filter_by(id=category_id).one()
	id = category.id
	db.session.delete(category)
	db.session.commit()
	return jsonify({"category_id":id})


@mod_api.route('/status/', methods=['GET'])
def get_status() -> jsonify:
	"""
	Retrieve a list of all statuses.

	Returns:
		Returns name and id of status
	"""
	statuses = []
	status_results = db.session.query(IncidentStatus).all()
	for status in status_results:
		new_status = {}
		new_status['id'] = status.id
		new_status['name'] = status.name
		statuses.append(new_status)
	return jsonify({"Data":statuses})


@mod_api.route('/status/', methods=['POST'])
def new_status() -> jsonify:
	"""
	Adds a new status and returns the status_id
	assigned.

	Returns:
		Returns status_id, name of the new status.
	"""
	new_status = IncidentStatus()
	post_data = request.json
	if 'status' in post_data:
		if 'name' in post_data['status']:
			new_status.name = post_data['status']['name']
	else:
		return jsonify({"Error": "no status data"})
	db.session.add(new_status)
	db.session.commit()
	return jsonify({"Status_ID":new_status.id})


@mod_api.route('/status/<status_id>', methods=['DELETE'])
def delete_status(status_id: str = "") -> jsonify:
	"""
	Deletes the status associated with the id passed in
	the url

	Returns the id of the status deleted
	"""
	status = db.session.query(IncidentStatus).filter_by(id=status_id).one()
	id = status.id
	db.session.delete(status)
	db.session.commit()
	return jsonify({"status_id":id})


@mod_api.route('/priority/', methods=['GET'])
def get_priority() -> jsonify:
	"""
	Retrieve a list of all priority.

	Returns:
		Returns name and id of priority
	"""
	priorities = []
	priority_results = db.session.query(IncidentPriority).all()
	for priority in priority_results:
		new_priority = {}
		new_priority['id'] = priority.id
		new_priority['name'] = priority.name
		priorities.append(new_priority)
	return jsonify({"Data":priorities})


@mod_api.route('/priority/', methods=['POST'])
def new_priority() -> jsonify:
	"""
	Adds a new priority and returns the priority_id
	assigned.

	Returns:
		Returns priority_id, name of the new priority.
	"""
	new_priority = IncidentPriority()
	db.session.add(new_priority)
	db.session.commit()
	return jsonify({"priority_id":new_priority.id})


@mod_api.route('/priority/<priority_id>', methods=['DELETE'])
def delete_priority(priority_id: str = "") -> jsonify:
	"""
	Deletes the priority associated with the id passed in
	the url

	Returns the id of the priority deleted
	"""
	priority = db.session.query(IncidentPriority).filter_by(id=priority_id).one()
	id = priority.id
	db.session.delete(priority)
	db.session.commit()
	return jsonify({"priority_id":id})


@mod_api.route('/impact/', methods=['GET'])
def get_impact() -> jsonify:
	"""
	Retrieve a list of all impact.

	Returns:
		Returns name and id of impact
	"""
	impacts = []
	impact_results = db.session.query(IncidentImpact).all()
	for impact in impact_results:
		new_impact = {}
		new_impact['id'] = impact.id
		new_impact['name'] = impact.name
		impacts.append(new_impact)
	return jsonify({"Data":impacts})


@mod_api.route('/impact/', methods=['POST'])
def new_impact() -> jsonify:
	"""
	Adds a new impact and returns the impact_id
	assigned.

	Returns:
		Returns impact_id, name of the new impact.
	"""
	new_impact = IncidentImpact()
	db.session.add(new_impact)
	db.session.commit()
	return jsonify({"impact_id":new_impact.id})


@mod_api.route('/impact/<impact_id>', methods=['DELETE'])
def delete_impact(impact_id: str = "") -> jsonify:
	"""
	Deletes the impact associated with the id passed in
	the url

	Returns the id of the impact deleted
	"""
	impact = db.session.query(IncidentImpact).filter_by(id=impact_id).one()
	id = impact.id
	db.session.delete(impact)
	db.session.commit()
	return jsonify({"impact_id":id})


@mod_api.route('/sub_category/', methods=['GET'])
def get_sub_category() -> jsonify:
	"""
	Retrieve a list of all sub_category.

	Returns:
		Returns name and id of sub_category
	"""
	sub_categories = []
	sub_category_results = db.session.query(IncidentSubCategory).all()
	for sub_category in sub_category_results:
		new_sub_category = {}
		new_sub_category['id'] = prisub_categoryority.id
		new_sub_category['name'] = sub_category.name
		sub_categories.append(new_sub_category)
	return jsonify({"Data":sub_categories})


@mod_api.route('/sub_category/', methods=['POST'])
def new_sub_category() -> jsonify:
	"""
	Adds a new sub_category and returns the sub_category_id
	assigned.

	Returns:
		Returns sub_category_id, name of the new sub_category.
	"""
	new_sub_category = IncidentSubCategory()
	db.session.add(new_sub_category)
	db.session.commit()
	return jsonify({"sub_category_id":new_sub_category.id})


@mod_api.route('/sub_category/<sub_category_id>', methods=['DELETE'])
def delete_sub_category(sub_category_id: str = "") -> jsonify:
	"""
	Deletes the sub_category associated with the id passed in
	the url

	Returns the id of the sub_category deleted
	"""
	sub_category = db.session.query(IncidentSubCategory).filter_by(id=sub_category_id).one()
	id = sub_category.id
	db.session.delete(sub_category)
	db.session.commit()
	return jsonify({"sub_category_id":id})


@mod_api.route('/urgency/', methods=['GET'])
def get_urgency() -> jsonify:
	"""
	Retrieve a list of all urgency.

	Returns:
		Returns name and id of urgency
	"""
	urgencies = []
	urgency_results = db.session.query(IncidentUrgency).all()
	for urgency in urgency_results:
		new_urgency = {}
		new_urgency['id'] = urgency.id
		new_urgency['name'] = urgency.name
		urgencies.append(new_urgency)
	return jsonify({"Data":urgencies})


@mod_api.route('/urgency/', methods=['POST'])
def new_urgency() -> jsonify:
	"""
	Adds a new urgency and returns the urgency_id
	assigned.

	Returns:
		Returns urgency_id, name of the new urgency.
	"""
	new_urgency = IncidentUrgency()
	db.session.add(new_urgency)
	db.session.commit()
	return jsonify({"urgency_id":new_urgency.id})


@mod_api.route('/urgency/<urgency_id>', methods=['DELETE'])
def delete_urgency(urgency_id: str = "") -> jsonify:
	"""
	Deletes the urgency associated with the id passed in
	the url

	Returns the id of the urgency deleted
	"""
	urgency = db.session.query(IncidentSubCategory).filter_by(id=urgency_id).one()
	id = urgency.id
	db.session.delete(urgency)
	db.session.commit()
	return jsonify({"urgency":id})


@mod_api.route('/agent_group/', methods=['GET'])
def get_agent_group() -> jsonify:
	"""
	Retrieve a list of all agent_group.

	Returns:
		Returns name and id of agent_group
	"""
	agent_groups = []
	agent_group_results = db.session.query(AgentGroup).all()
	for agent_group in agent_group_results:
		new_agent_group = {}
		new_agent_group['id'] = agent_group.id
		new_agent_group['name'] = agent_group.name
		agent_groups.append(new_agent_group)
	return jsonify({"Data":agent_groups})


@mod_api.route('/agent_group/', methods=['POST'])
def new_agent_group() -> jsonify:
	"""
	Adds a new agent_group and returns the agent_group_id
	assigned.

	Returns:
		Returns agent_group_id, name of the new agent_group.
	"""
	new_agent_group = AgentGroup()
	db.session.add(new_agent_group)
	db.session.commit()
	return jsonify({"agent_group_id":new_agent_group.id})


@mod_api.route('/agent_group/<agent_group_id>', methods=['DELETE'])
def delete_agent_group(agent_group_id: str = "") -> jsonify:
	"""
	Deletes the urgency associated with the id passed in
	the url

	Returns the id of the urgency deleted
	"""
	agent_group = db.session.query(AgentGroup).filter_by(id=agent_group_id).one()
	id = agent_group.id
	db.session.delete(agent_group)
	db.session.commit()
	return jsonify({"agent_group":id})