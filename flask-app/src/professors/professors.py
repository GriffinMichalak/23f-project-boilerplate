from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db

professors = Blueprint('professors', __name__)

# Get all professors from StudyStage
@professors.route('/professors', methods=['GET'])
def get_professors():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM Professor')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'

    # return "Number of professors fetched: " + str(len(theData)) + ""

    return the_response

# Get customer detail for customer with particular userID
@professors.route('/professors/<userID>', methods=['GET'])
def get_professor(userID):
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM Professor WHERE FacultyID = {0}'.format(userID))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

@professors.route('/professors/create-professor', methods=['POST'])
def add_professor():
    
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    FirstName = the_data['FirstName']
    LastName = the_data['LastName']
    Year_Hired = the_data['Year_Hired']
    Tenured = the_data['Tenured']

    # Constructing the query
    query = 'INSERT INTO Professor (FirstName, LastName, Year_Hired, Tenured) VALUES ("'
    query += FirstName + '", "'
    query += LastName + '", "'
    query += str(Year_Hired) + '", '
    query += str(Tenured) + ')'
    current_app.logger.info(query)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Successfully added new Professor'

@professors.route('/professors/update-professor/<userID>', methods=['PUT'])
def update_professor(userID):
    # collecting data from the request object
    the_data = request.json
    current_app.logger.info(the_data)

    # extracting the variable
    FirstName = the_data['FirstName']
    LastName = the_data['LastName']
    Year_Hired = the_data['Year_Hired']
    Tenured = the_data['Tenured']

    # constructing the query
    query = 'UPDATE Professor SET FirstName = "'
    query += FirstName + '", LastName = "'
    query += LastName + '", Year_Hired = '
    query += str(Year_Hired) + ', Tenured = '
    query += str(Tenured) + ' WHERE FacultyID = '
    query += str(userID)

    # executing and committing the update statement
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    return 'Professor information updated successfully!'

@professors.route('/professors/delete-professor/<userID>', methods=['DELETE'])
def delete_professor(userID):
    # constructing the query
    query = 'DELETE FROM Professor WHERE FacultyID = ' + str(userID)

    # executing and committing the delete statement
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    return 'Professor deleted successfully!'
