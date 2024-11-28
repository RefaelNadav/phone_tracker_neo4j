from flask import Blueprint, request, jsonify, current_app
import json
import logging
from neo4j_service import AnalysisRepository


analysis_bp = Blueprint('analysis_bp', __name__)

@analysis_bp.route("/api/analysis/bluetooth", methods=['GET'])
def get_bluetooth_connected():

    try:
        repo = AnalysisRepository(current_app.neo4j_driver)
        length_path = repo.find_bluetooth_connected()

        return jsonify({"length path": length_path}), 200
    except Exception as e:
        print(f'Error in GET /api/analysis/bluetooth: {str(e)}')
        logging.error(f'Error in GET /api/analysis/bluetooth: {str(e)}')
        return jsonify({'error': 'internal server error'}), 500

@analysis_bp.route("/api/analysis/strength_dbm", methods=['GET'])
def get_strength_dbm():
    try:
        repo = AnalysisRepository(current_app.neo4j_driver)
        calls = repo.find_signal_strength()

        return jsonify(calls), 200
    except Exception as e:
        print(f'Error in GET /api/analysis/strength_dbm: {str(e)}')
        logging.error(f'Error in GET /api/analysis/strength_dbm: {str(e)}')
        return jsonify({'error': 'internal server error'}), 500


@analysis_bp.route("/api/analysis/count_connected/<device_id>", methods=['GET'])
def get_count_connected_devices(device_id):
    try:
        repo = AnalysisRepository(current_app.neo4j_driver)
        count_connected = repo.count_connected_devices(device_id)

        return jsonify({"connected devices": count_connected}), 200
    except Exception as e:
        print(f'Error in GET /api/analysis/count_connected: {str(e)}')
        logging.error(f'Error in GET /api/analysis/count_connected: {str(e)}')
        return jsonify({'error': 'internal server error'}), 500


@analysis_bp.route("/api/analysis/is_connected/<device_id1>/<device_id2>", methods=['GET'])
def get_is_connected(device_id1, device_id2):
    try:
        repo = AnalysisRepository(current_app.neo4j_driver)
        count_connected = repo.chekc_is_connected(device_id1, device_id2)

        return jsonify(count_connected), 200
    except Exception as e:
        print(f'Error in GET /api/analysis/count_connected: {str(e)}')
        logging.error(f'Error in GET /api/analysis/count_connected: {str(e)}')
        return jsonify({'error': 'internal server error'}), 500

@analysis_bp.route("/api/analysis/last_interaction/<device_id>", methods=['GET'])
def get_last_interaction(device_id):
    try:
        repo = AnalysisRepository(current_app.neo4j_driver)
        interaction = repo.find_last_interaction(device_id)

        return jsonify(interaction), 200
    except Exception as e:
        print(f'Error in GET /api/analysis/count_connected: {str(e)}')
        logging.error(f'Error in GET /api/analysis/count_connected: {str(e)}')
        return jsonify({'error': 'internal server error'}), 500