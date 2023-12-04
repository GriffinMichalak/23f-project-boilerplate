from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db

teachingAssistants = Blueprint('teachingAssistants', __name__)

# Get all teachingAssistants from StudyStage
@teachingAssistants.route('/all', methods=['GET'])
def get_teachingAssistants():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM TeachingAssistant')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'

    # return "Number of teachingAssistants fetched: " + str(len(theData)) + ""

    return the_response

# Get customer detail for customer with particular userID
@teachingAssistants.route('/get-ta/<userID>', methods=['GET'])
def get_teachingAssistant(userID):
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM TeachingAssistant WHERE TAID = {0}'.format(userID))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

@teachingAssistants.route('/create-ta', methods=['POST'])
def add_teachingAssistant():
    
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    FirstName = the_data['FirstName']
    LastName = the_data['LastName']
    Semesters_Worked = the_data['Semesters_Worked']
    Hourly_Wage = the_data['Hourly_Wage']

    # Constructing the query
    query = 'INSERT INTO TeachingAssistant (FirstName, LastName, Semesters_Worked, Hourly_Wage) VALUES ("'
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

@teachingAssistants.route('/update-ta/<userID>', methods=['PUT'])
def update_teachingAssistant(userID):
    # collecting data from the request object
    the_data = request.json
    current_app.logger.info(the_data)

    # extracting the variable
    FirstName = the_data['FirstName']
    LastName = the_data['LastName']
    Semesters_Worked = the_data['Semesters_Worked']
    Hourly_Wage = the_data['Hourly_Wage']

    # constructing the query
    query = 'UPDATE TeachingAssistant SET FirstName = "'
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

@teachingAssistants.route('/delete-ta/<userID>', methods=['DELETE'])
def delete_teachingAssistant(userID):
    # constructing the query
    query = 'DELETE FROM TeachingAssistant WHERE TAID = ' + str(userID)

    # executing and committing the delete statement
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    return 'TA deleted successfully!'