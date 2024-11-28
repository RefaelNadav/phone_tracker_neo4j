from flask import Blueprint, request, jsonify, current_app
import json
import logging
from neo4j_service import InserrCallsRepository



# from neo4j_service import TransactionRepository

insert_bp = Blueprint('insert_bp', __name__)

@insert_bp.route("/api/phone_tracker", methods=['POST'])
def insert_phone_tracker():
    data = request.get_json()
    if data['devices'][0]['id'] == data['devices'][1]['id']:
        return jsonify({'error': 'cannot can yourself'}), 400

    try:
        repo = InserrCallsRepository(current_app.neo4j_driver)
        interaction_id = repo.create_call(data)

        return jsonify({
            'status': 'success',
            'transaction_id': interaction_id
        }), 201
    except Exception as e:
        print(f'Error in POST /api/phone_tracker: {str(e)}')
        logging.error(f'Error in POST /api/phone_tracker: {str(e)}')
        return jsonify({'error': 'internal server error'}), 500