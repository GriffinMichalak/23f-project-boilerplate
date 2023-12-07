from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db

attends_office_hour = Blueprint('attends_office_hour', __name__)

# Get all attends_office_hour from StudyStage
@attends_office_hour.route('/all', methods=['GET'])
def get_attends_oh():
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

# gets a specific Attends_OH tuple 
@attends_office_hour.route('/get/<aID>/<ohID>/<sID>', methods=['GET'])
def get_specific_attends_oh(aID, ohID, sID):
    query = 'SELECT AssignmentID, OfficeHoursID, StudentID FROM Attends_OH WHERE AssignmentID = '
    query += str(aID) + ' AND OfficeHoursID = ' + str(ohID) + ' AND StudentID = ' + str(sID)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    result = cursor.fetchone()

    if result is None:
        return 'No attends_office_hour record found with the specified IDs.'

    assignment_id = result[0]
    office_hours_id = result[1]
    student_id = result[2]

    attends_oh_data = {
        'AssignmentID': assignment_id,
        'OfficeHoursID': office_hours_id,
        'StudentID': student_id
    }

    return [attends_oh_data]

# gets a specific Attends_OH tuple 
@attends_office_hour.route('/get/<sID>', methods=['GET'])
def get_specific_attends_oh_by_student(sID):
    query = 'SELECT AssignmentID, OfficeHoursID, StudentID FROM Attends_OH WHERE StudentID = '
    query += str(sID)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    result = cursor.fetchone()

    if result is None:
        return 'No attends_office_hour record found with the specified IDs.'

    assignment_id = result[0]
    office_hours_id = result[1]
    student_id = result[2]

    attends_oh_data = {
        'AssignmentID': assignment_id,
        'OfficeHoursID': office_hours_id,
        'StudentID': student_id
    }

    return [attends_oh_data]

@attends_office_hour.route('/create', methods=['POST'])
def create_attends_oh():
    # Collecting data from the request object
    the_data = request.json

    # Extracting the variables
    assignment_id = the_data['AssignmentID']
    office_hours_id = the_data['OfficeHoursID']
    student_id = the_data['StudentID']

    # Constructing the query
    query = 'INSERT INTO Attends_OH (AssignmentID, OfficeHoursID, StudentID) VALUES ('
    query += str(assignment_id) + ', ' + str(office_hours_id) + ', ' + str(student_id) + ')'

    # Executing and committing the insert statement
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    return 'Attends_OH record created successfully!'

# Update information about a class
@attends_office_hour.route('/update/<aID>/<ohID>/<sID>', methods=['PUT'])
def update_officehours(aID, ohID, sID):
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

@attends_office_hour.route('/delete/<aID>/<ohID>/<sID>', methods=['DELETE'])
def delete_classes(aID, ohID, sID):
    # constructing the query
    query = 'DELETE FROM Attends_OH WHERE AssignmentID = ' + str(aID) + ' AND OfficeHoursID = ' + str(ohID) + ' AND StudentID = ' + str(sID)

    # executing and committing the delete statement
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    return 'Study Group deleted successfully!'