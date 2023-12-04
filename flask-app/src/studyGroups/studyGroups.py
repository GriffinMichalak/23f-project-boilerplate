from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db

studyGroups = Blueprint('studyGroups', __name__)

# Get all studyGroups from StudyStage
@studyGroups.route('/all', methods=['GET'])
def get_studyGroups():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM StudyGroup')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))

    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    
    # return "Number of studyGroups fetched: " + str(len(theData)) + ""

    return the_response

# Get customer detail for customer with particular userID
@studyGroups.route('/studyGroups/<userID>', methods=['GET'])
def get_studyGroup(userID):
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM studyGroup WHERE TAID = {0}'.format(userID))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

@studyGroups.route('/studyGroups/create-studyGroup', methods=['POST'])
def add_studyGroup():
    
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    FirstName = the_data['FirstName']
    LastName = the_data['LastName']
    Semesters_Worked = the_data['Semesters_Worked']
    Hourly_Wage = the_data['Hourly_Wage']

    # Constructing the query
    query = 'INSERT INTO studyGroup (FirstName, LastName, Semesters_Worked, Hourly_Wage) VALUES ("'
    query += FirstName + '", "'
    query += LastName + '", "'
    query += str(Semesters_Worked) + '", '
    query += str(Hourly_Wage) + ')'
    current_app.logger.info(query)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Successfully created a new TA'

@studyGroups.route('/studyGroups/update-studyGroup/<userID>', methods=['PUT'])
def update_studyGroup(userID):
    # collecting data from the request object
    the_data = request.json
    current_app.logger.info(the_data)

    # extracting the variable
    FirstName = the_data['FirstName']
    LastName = the_data['LastName']
    Semesters_Worked = the_data['Semesters_Worked']
    Hourly_Wage = the_data['Hourly_Wage']

    # constructing the query
    query = 'UPDATE studyGroup SET FirstName = "'
    query += FirstName + '", LastName = "'
    query += LastName + '", Semesters_Worked = '
    query += str(Semesters_Worked) + ', Hourly_Wage = '
    query += str(Hourly_Wage) + ' WHERE TAID = '
    query += str(userID)

    # executing and committing the update statement
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    return 'TA information updated successfully!'

@studyGroups.route('/studyGroups/delete-studyGroup/<userID>', methods=['DELETE'])
def delete_studyGroup(userID):
    # constructing the query
    query = 'DELETE FROM studyGroup WHERE TAID = ' + str(userID)

    # executing and committing the delete statement
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    return 'TA deleted successfully!'