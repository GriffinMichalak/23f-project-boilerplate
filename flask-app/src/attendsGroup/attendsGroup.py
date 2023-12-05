from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db

attends_group = Blueprint('attends_group', __name__)

# Get all attends_group from StudyStage
@attends_group.route('/all', methods=['GET'])
def get_attends_group():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM Attends_OH')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        row_dict = dict(zip(row_headers, row))
        json_data.append(row_dict)

    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'

    return the_response

