import os
from flask import Flask
from flask import Blueprint, request, current_app

mod_docs = Blueprint('docs', __name__, url_prefix='/docs', static_folder = '../../../docs/_build/html')

@mod_docs.route('/', defaults={'path': 'index.html'})
@mod_docs.route('/<path:path>')
def get_dir(path):
    return mod_docs.send_static_file(path)
