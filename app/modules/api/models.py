from app import db

class Incident(db.Model):
	"""
	Mostly Done!
	"""
	id = db.Column(db.Integer, primary_key=True)
	date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
	date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
							  onupdate=db.func.current_timestamp())
	subject = db.Column(db.String(150))
	description = db.Column(db.String(1000))
	priority = db.relationship('IncidentPriority', backref='incident', lazy=True)
	status = db.relationship('IncidentStatus', backref='incident', lazy=True)
	#agent_group = db.relationship('AgentGroup', backref='incident', lazy=True)
	#department = db.relationship('RequesterDepartment', backref='incident', lazy=True)
	category = db.relationship('IncidentCategory', backref='incident', lazy=True)
	#sub_category = db.relationship('IncidentSubCategory', backref='incident', lazy=True)
	#impact = db.relationship('IncidentImpact', backref='incident', lazy=True)
	#notes = db.relationship('IncidentNote', backref='incident', lazy=True)

class IncidentStatus(db.Model):
	"""
	Done!
	"""
	id = db.Column(db.Integer, primary_key=True)
	date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
	date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
							  onupdate=db.func.current_timestamp())
	name = db.Column(db.String(100))
	incidents = db.Column(db.Integer, db.ForeignKey('incident.id'), nullable=True)


class IncidentPriority(db.Model):
	"""
	Done!
	"""
	__tablename__ = 'incident_priority'
	id = db.Column(db.Integer, primary_key=True)
	date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
	date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
							  onupdate=db.func.current_timestamp())
	name = db.Column(db.String(100))
	incidents = db.Column(db.Integer, db.ForeignKey('incident.id'), nullable=True) #db.Column(db.Integer, db.ForeignKey('incident.id'), nullable=True)


class IncidentNote(db.Model):
	"""

	"""
	id = db.Column(db.Integer, primary_key=True)
	date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
	date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
							  onupdate=db.func.current_timestamp())
	note_type = db.Column(db.String(20)) # private/public note
	main_body = db.Column(db.String(1000))
	email = db.Column(db.Integer) # 1 for email, 0 for no email


class IncidentCategory(db.Model):
	"""
	Done!
	"""
	id = db.Column(db.Integer, primary_key=True)
	date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
	date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
							  onupdate=db.func.current_timestamp())
	name = db.Column(db.String(100))
	incident_id = db.Column(db.Integer, db.ForeignKey('incident.id'), nullable=True)
	#sub_categories = db.relationship('IncidentSubCategory', backref='incidentcategory', lazy=True)


class User(db.Model):
	"""
	"""
	id = db.Column(db.Integer, primary_key=True)
	date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
	date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
							  onupdate=db.func.current_timestamp())
	name = db.Column(db.String(100))
	requester_id = db.relationship('Requester', backref='incident', lazy=True)
	agent_id = db.relationship('Agent', backref='incident', lazy=True)
	email_address = db.Column(db.String(100))


class Requester(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
	date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
							  onupdate=db.func.current_timestamp())
	#incidents = db.relationship('Incident', backref='incident', lazy=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)


class Agent(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
	date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
							  onupdate=db.func.current_timestamp())
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)


class IncidentImpact(db.Model):
	"""
	"""
	id = db.Column(db.Integer, primary_key=True)
	date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
	date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
							  onupdate=db.func.current_timestamp())
	name = db.Column(db.String(100))
	#incident_id = db.Column(db.Integer, db.ForeignKey('incident.id'), nullable=True)


class IncidentSubCategory(db.Model):
	"""
	"""
	id = db.Column(db.Integer, primary_key=True)
	date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
	date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
							  onupdate=db.func.current_timestamp())
	name = db.Column(db.String(100))
	#incident_id = db.Column(db.Integer, db.ForeignKey('incident.id'), nullable=True)
	#category = db.Column(db.Integer, db.ForeignKey('incident_category.id'), nullable=False)


class IncidentUrgency(db.Model):
	"""
	"""
	id = db.Column(db.Integer, primary_key=True)
	date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
	date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
							  onupdate=db.func.current_timestamp())
	name = db.Column(db.String(100))



class RequesterDepartment(db.Model):
	"""
	"""
	id = db.Column(db.Integer, primary_key=True)
	date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
	date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
							  onupdate=db.func.current_timestamp())
	name = db.Column(db.String(100))
	requesters = db.Column(db.Integer, db.ForeignKey('requester.id'), nullable=True)


class AgentGroup(db.Model):
	"""
	"""
	id = db.Column(db.Integer, primary_key=True)
	date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
	date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
							  onupdate=db.func.current_timestamp())
	name = db.Column(db.String(100))