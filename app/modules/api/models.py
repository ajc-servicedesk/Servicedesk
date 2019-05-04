from app import db

class Incident(db.Model):
	"""

	"""
	id = db.Column(db.Integer, primary_key=True)
	date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
	date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
							  onupdate=db.func.current_timestamp())
	subject = db.Column(db.String())
	description = db.Column(db.String())
	priority = db.relationship('IncidentPriority', backref='incident', lazy=True)
	status = db.relationship('IncidentStatus', backref='incident', lazy=True)
	agent_group = db.relationship('AgentGroup', backref='incident', lazy=True)
	agent_assigned = db.relationship('Agent', backref='incident', lazy=True)
	department = db.relationship('RequesterDepartment', backref='incident', lazy=True)
	category = db.relationship('IncidentCategory', backref='incident', lazy=True)
	sub_category = db.relationship('IncidentSubCategory', backref='incident', lazy=True)
	requester = db.relationship('Requester', backref='incident', lazy=True)
	notes = db.relationship('Note', backref='incident', lazy=True)

class IncidentStatus(db.Model):
	"""
	"""
	id = db.Column(db.Integer, primary_key=True)
	date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
	date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
							  onupdate=db.func.current_timestamp())
	name = db.Column(db.String())
	incidents = db.Column(db.Integer, db.ForeignKey('incident.id'), nullable=False)


class IncidentPriority(db.Model):
	"""
	"""
	id = db.Column(db.Integer, primary_key=True)
	date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
	date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
							  onupdate=db.func.current_timestamp())
	name = db.Column(db.String())
	incidents = db.Column(db.Integer, db.ForeignKey('incident.id'), nullable=False)


class IncidentNote(db.Model):
	"""
	Contains all notes (private/public) on tickets
	"""
	id = db.Column(db.Integer, primary_key=True)
	date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
	date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
							  onupdate=db.func.current_timestamp())
	type = db.Column(db.String()) # private/public note
	main_body = db.Column(db.String())
	agent = db.Column(db.Integer, db.ForeignKey('agent.id'), nullable=False)
	email = db.Column(db.Integer) # 1 for email, 0 for no email
	incident_id = db.Column(db.Integer, db.ForeignKey('incident.id'), nullable=False)

class IncidentCategory(db.Model):
	"""
	"""
	id = db.Column(db.Integer, primary_key=True)
	date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
	date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
							  onupdate=db.func.current_timestamp())
	name = db.Column(db.String())
	incident_id = db.Column(db.Integer, db.ForeignKey('incident.id'), nullable=False)
	sub_categories = db.relationship('IncidentSubCategory', backref='incidentcategory', lazy=True)


class IncidentImpact(db.Model):
	"""
	"""
	id = db.Column(db.Integer, primary_key=True)
	date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
	date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
							  onupdate=db.func.current_timestamp())
	name = db.Column(db.String())
	incident_id = db.Column(db.Integer, db.ForeignKey('incident.id'), nullable=False)


class IncidentSubCategory(db.Model):
	"""
	"""
	id = db.Column(db.Integer, primary_key=True)
	date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
	date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
							  onupdate=db.func.current_timestamp())
	name = db.Column(db.String())
	incident_id = db.Column(db.Integer, db.ForeignKey('incident.id'), nullable=False)
	category = db.Column(db.Integer, db.ForeignKey('incidentcategory.id'), nullable=False)


class IncidentUrgency(db.Model):
	"""
	"""
	id = db.Column(db.Integer, primary_key=True)
	date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
	date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
							  onupdate=db.func.current_timestamp())
	name = db.Column(db.String())


class Requester(db.Model):
	"""
	"""
	id = db.Column(db.Integer, primary_key=True)
	date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
	date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
							  onupdate=db.func.current_timestamp())
	department = db.relationship('IncidentDepartment', backref='requester', lazy=True)
	incidents = db.Column(db.Integer, db.ForeignKey('incident.id'), nullable=False)


class Agent(db.Model):
	"""
	"""
	id = db.Column(db.Integer, primary_key=True)
	date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
	date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
							  onupdate=db.func.current_timestamp())
	# group = # link back to AgentGroups
	name = db.Column(db.String())
	email_address = db.Column(db.String())
	notes = db.relationship('IncidentNote', backref='agent', lazy=True)
	incidents = db.Column(db.Integer, db.ForeignKey('incident.id'), nullable=False)


class RequesterDepartment(db.Model):
	"""
	"""
	id = db.Column(db.Integer, primary_key=True)
	date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
	date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
							  onupdate=db.func.current_timestamp())
	name = db.Column(db.String())
	requesters = db.Column(db.Integer, db.ForeignKey('requester.id'), nullable=False)
	incidents = db.Column(db.Integer, db.ForeignKey('incident.id'), nullable=False)


class AgentGroups(db.Model):
	"""
	"""
	id = db.Column(db.Integer, primary_key=True)
	date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
	date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
							  onupdate=db.func.current_timestamp())
	agents = db.Column(db.Integer, db.ForeignKey('agent.id'), nullable=False)
	name = db.Column(db.String())
	incidents = db.Column(db.Integer, db.ForeignKey('incident.id'), nullable=False)