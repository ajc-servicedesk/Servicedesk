from flask import Flask
from flask import Blueprint, request, jsonify, render_template
from app import db
from app.modules.api.models import *
from app import db

mod_frontend = Blueprint('frontend', __name__, url_prefix='')

@mod_frontend.route('/', methods=['GET'])
def index():
    return render_template("mod_frontend/index.html")


@mod_frontend.route('/administration', methods=['GET'])
def administration():
    return render_template("mod_frontend/administration.html")


@mod_frontend.route('/incidents', methods=['GET'])
def incidents():
    return render_template("mod_frontend/incidents.html")

@mod_frontend.route('/incidents/<incident_id>', methods=['GET'])
def get_more_incident_information(incident_id):
    """
    Give more information about the incident and where notes are
    shown to the user
    """
    incident = db.session.query(Incident).filter_by(id=incident_id).one()
    return render_template("mod_frontend/incident_full.html", incident=incident)


@mod_frontend.route('/requesters', methods=['GET'])
def requesters():
    return render_template("mod_frontend/requesters.html")


@mod_frontend.route('/agents', methods=['GET'])
def agents():
    return render_template("mod_frontend/agents.html")