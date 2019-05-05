from flask import Flask
from flask import Blueprint, request, jsonify, render_template
from app import db
from app.modules.api.models import *

mod_frontend = Blueprint('frontend', __name__, url_prefix='')

@mod_frontend.route('/', methods=['GET'])
def index():
    return render_template("mod_frontend/index.html")


@mod_frontend.route('/administration', methods=['GET'])
def administration():
    return render_template("mod_frontend/administration.html")