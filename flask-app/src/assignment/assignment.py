from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db

assignment = Blueprint('assignment', __name__)

# Get all assignment from StudyStage
@assignment.route('/all', methods=['GET'])
def get_assignments():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM Assignment')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'

    # return "Number of assignment fetched: " + str(len(theData)) + ""

    return the_response

# Get assignment with specific assignmentID
@assignment.route('/get-assignment/<assignmentID>', methods=['GET'])
def get_assignment(assignmentID):
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM Assignment WHERE AssignmentID = {0}'.format(assignmentID))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

@assignment.route('/create-assignment', methods=['POST'])
def add_assignment():
    
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    # extracting the variable
    Title = the_data['Title']
    Description = the_data['Desctiption']
    InGroups = the_data['InGroups']
    CourseCode = the_data['CourseCode']
    TA_ID = the_data['TA_ID']

    # Constructing the query
    query = 'INSERT INTO Assignment (Title, Description, InGroups, CourseCode, TA_ID) VALUES ("'
    query += Title + '", "'
    query += Description + '", "'
    query += str(InGroups) + '", '
    query += str(CourseCode) + '", '
    query += str(TA_ID) + ')'
    current_app.logger.info(query)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Success!'

@assignment.route('/update-assignment/<assignmentID>', methods=['PUT'])
def update_assignment(assignmentID):

    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    # extracting the variable
    Title = the_data['Title']
    Description = the_data['Desctiption']
    InGroups = the_data['InGroups']
    CourseCode = the_data['CourseCode']
    TA_ID = the_data['TA_ID']

    # constructing the query
    query = 'UPDATE Assignment SET Title = "'
    query += Title + '", Description = "'
    query += str(Description) + '", InGroups = '
    query += str(InGroups) + ', CourseCode = '
    query += str(CourseCode) + ', TA_ID = '
    query += str(TA_ID) + ' WHERE AssignmentID = '
    query += str(assignmentID)
 
    # executing and committing the update statement
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    return 'Assignment information updated successfully!'

@assignment.route('/delete-assignment/<assignmentID>', methods=['DELETE'])
def delete_student(assignmentID):
    # constructing the query
    query = 'DELETE FROM Assignment WHERE AssignmentID = ' + str(assignmentID)

    # executing and committing the delete statement
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    return 'Assignment deleted successfully!'