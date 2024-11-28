from flask import Flask, jsonify, request
import logging

from init_db import init_neo4j
from insert_bp import insert_bp


app = Flask(__name__)

app.config['DEBUG'] = True
app.config['LOGGING_LEVEL'] = logging.DEBUG

app.register_blueprint(insert_bp)


with app.app_context():
    app.neo4j_driver = init_neo4j()

if __name__ == "__main__":
    app.run(debug=True)