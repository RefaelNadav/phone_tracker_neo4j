from flask import Flask, jsonify, request
import logging

from init_db import init_neo4j
from analysis_bp import analysis_bp


app = Flask(__name__)

app.config['DEBUG'] = True
app.config['LOGGING_LEVEL'] = logging.DEBUG

app.register_blueprint(analysis_bp)


with app.app_context():
    app.neo4j_driver = init_neo4j()

if __name__ == "__main__":
    app.run(debug=True)