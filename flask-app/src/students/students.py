from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db

students = Blueprint('students', __name__)

# Get all students from StudyStage
@students.route('/students', methods=['GET'])
def get_students():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM Student')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'

    # return "Number of students fetched: " + str(len(theData)) + ""

    return the_response

# Get customer detail for customer with particular userID
@students.route('/students/<userID>', methods=['GET'])
def get_student(userID):
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM Student WHERE StudentID = {0}'.format(userID))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

@students.route('/students/create-student', methods=['POST'])
def add_student():
    
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    FirstName = the_data['FirstName']
    LastName = the_data['LastName']
    Year = the_data['Year']
    GPA = the_data['GPA']

    # Constructing the query
    query = 'INSERT INTO Student (FirstName, LastName, Year, GPA) VALUES ("'
    query += FirstName + '", "'
    query += LastName + '", "'
    query += str(Year) + '", '
    query += str(GPA) + ')'
    current_app.logger.info(query)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Success!'

@students.route('/students/update-student/<userID>', methods=['PUT'])
def update_student(userID):
    # collecting data from the request object
    the_data = request.json
    current_app.logger.info(the_data)

    # extracting the variable
    FirstName = the_data['FirstName']
    LastName = the_data['LastName']
    Year = the_data['Year']
    GPA = the_data['GPA']

    # constructing the query
    query = 'UPDATE Student SET FirstName = "'
    query += FirstName + '", LastName = "'
    query += LastName + '", Year = '
    query += str(Year) + ', GPA = '
    query += str(GPA) + ' WHERE StudentID = '
    query += str(userID)

    # executing and committing the update statement
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    return 'Student information updated successfully!'

@students.route('/students/delete-student/<userID>', methods=['DELETE'])
def delete_student(userID):
    # constructing the query
    query = 'DELETE FROM Student WHERE StudentID = ' + str(userID)

    # executing and committing the delete statement
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    return 'Student deleted successfully!'