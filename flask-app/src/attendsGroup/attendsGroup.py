from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db

attends_group = Blueprint('attends_group', __name__)

# Get all attends_group from StudyStage
@attends_group.route('/all', methods=['GET'])
def get_attends_group():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM Attends_Group')
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
@attends_group.route('/get/<sID>', methods=['GET'])
def get_specific_attends_group(sID):
    query = 'SELECT StudentID, StudyGroupID FROM Attends_Group WHERE StudentID = '
    query += str(sID)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    result = cursor.fetchone()

    if result is None:
        return 'No attends_group record found with the specified IDs.'

    student_id = result[0]
    group_id = result[1]

    attends_oh_data = {
        'StudentID': student_id,
        'GroupID': group_id
    }

    return attends_oh_data

@attends_group.route('/create', methods=['POST'])
def create_attends_oh():
    # Collecting data from the request object
    the_data = request.json

    # Extracting the variables
    StudentID = the_data['StudentID']
    StudyGroupID = the_data['GroupID']

    # Constructing the query
    query = 'INSERT INTO Attends_Group (StudentID, StudyGroupID) VALUES ('
    query += str(StudentID) + ', ' + str(StudyGroupID)  + ')'

    # Executing and committing the insert statement
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    return 'Attends_Group record created successfully!'

# Update information about a class
@attends_group.route('/update/<sID>/<gID>', methods=['PUT'])
def update_officehours(sID, gID):
    # collecting data from the request object
    the_data = request.json
    current_app.logger.info(the_data)

    # extracting the variables
    AssignmentID = the_data['AssignmentID']
    OfficeHoursID = the_data['OfficeHoursID']
    StudentID = the_data['StudentID']

    # constructing the query
    query = 'UPDATE Attends_OH SET AssignmentID = "'
    query += str(AssignmentID) + '", OfficeHoursID = "'
    query += str(OfficeHoursID) + '", StudentID = '
    query += str(StudentID) + ' WHERE AssignmentID = '
    query += str(aID) + ' AND OfficeHoursID = '
    query += str(ohID) + ' AND StudentID = '
    query += str(sID)

    # executing and committing the update statement
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    return 'Attends_OH information updated successfully!'

@attends_group.route('/delete/<sID>/<gID>', methods=['DELETE'])
def delete_classes(sID, gID):
    # constructing the query
    query = 'DELETE FROM Attends_Group WHERE StudentID = ' + str(sID) + ' AND StudyGroupID = ' + str(gID)

    # executing and committing the delete statement
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    return 'Study Group deleted successfully!'