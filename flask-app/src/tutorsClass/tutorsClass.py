from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db

tutorsClass = Blueprint('tutorsClass', __name__)

# Get all tutorsClass from StudyStage
@tutorsClass.route('/all', methods=['GET'])
def get_tutorsClass():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM TUTORS_CLASS')
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

# gets a specific Attends_OH tuple 
@tutorsClass.route('/get/<taID>', methods=['GET'])
def get_specific_tutorsClass(taID):
    query = 'SELECT ClassID, TA_ID FROM TUTORS_CLASS WHERE TA_ID = '
    query += taID

    cursor = db.get_db().cursor()
    cursor.execute(query)
    result = cursor.fetchone()

    if result is None:
        return 'No TutorsClass record found with the specified IDs.'

    class_id = result[0]
    ta_id = result[1]

    attends_oh_data = {
        'ClassID': class_id,
        'TA_ID': ta_id
    }

    return attends_oh_data

@tutorsClass.route('/create', methods=['POST'])
def create_attends_oh():
    # Collecting data from the request object
    the_data = request.json

    # Extracting the variables
    TA_ID = the_data['TA_ID']
    Class_ID = the_data['Class_ID']

    # Constructing the query
    query = 'INSERT INTO TUTORS_CLASS (TA_ID, Class_ID) VALUES ('
    query += str(TA_ID) + ', ' + Class_ID  + ')'

    # Executing and committing the insert statement
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    return 'TutorsClass record created successfully!'

@tutorsClass.route('/delete/<sID>/<gID>', methods=['DELETE'])
def delete_classes(taID, cID):
    # constructing the query
    query = 'DELETE FROM TUTORS_CLASS WHERE TA_ID = ' + str(taID) + ' AND ClassID = ' + cID

    # executing and committing the delete statement
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    return 'Tutors Class deleted successfully!'