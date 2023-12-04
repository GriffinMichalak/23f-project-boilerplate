from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db

attends_office_hour = Blueprint('attends_office_hour', __name__)

# Get all attends_office_hour from StudyStage
@attends_office_hour.route('/all', methods=['GET'])
def get_attends_office_hours():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM Attends_OH')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        # Convert Start_Time and End_Time to strings
        row_dict = dict(zip(row_headers, row))
        row_dict['Start_Time'] = str(row_dict['Start_Time'])
        row_dict['End_Time'] = str(row_dict['End_Time'])
        json_data.append(row_dict)

    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'

    return the_response