from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db

studygroup = Blueprint('studygroup', __name__)

# Get all StudyGroups from StudyStage
@studygroup.route('/all', methods=['GET'])
def get_StudyGroups():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM StudyGroup')
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

@studygroup.route('/get-studygroup/<groupID>', methods=['GET'])
def get_studygroup(groupID):
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM StudyGroup WHERE GroupID = {0}'.format(groupID))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        row_dict = dict(zip(row_headers, row))
        row_dict['Start_Time'] = str(row_dict['Start_Time'])
        row_dict['End_Time'] = str(row_dict['End_Time'])
        json_data.append(row_dict)

    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


@studygroup.route('/create-studygroup', methods=['POST'])
def add_studygroup():
    
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    Capacity = the_data['Capacity']
    Description = the_data['Description']
    Start_Time = the_data['Start_Time']
    End_Time = the_data['End_Time']
    CourseCode = the_data['CourseCode']
    StudentID = the_data['StudentID']

    # Constructing the query
    query = 'INSERT INTO StudyGroup (Capacity, Description, Start_Time, End_Time, CourseCode, StudentID) VALUES ("'
    query += str(Capacity) + '", "'
    query += Description + '", "'
    query += Start_Time + '", "'
    query += End_Time + '", "'
    query += CourseCode + '", '
    query += str(StudentID) + ')'
    current_app.logger.info(query)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Successfully created a new Study Group'

# Update information about a study group
@studygroup.route('/update-studygroup/<userID>', methods=['PUT'])
def update_studygroup(userID):
    # collecting data from the request object
    the_data = request.json
    current_app.logger.info(the_data)

    # extracting the variables
    Capacity = the_data['Capacity']
    Description = the_data['Description']
    Start_Time = the_data['Start_Time']
    End_Time = the_data['End_Time']
    CourseCode = the_data['CourseCode']
    StudentID = the_data['StudentID']

    # constructing the query
    query = 'UPDATE StudyGroup SET Capacity = "'
    query += str(Capacity) + '", Description = "'
    query += Description + '", Start_Time ="'
    query += Start_Time + '", End_Time = "'
    query += End_Time + '", CourseCode = "'
    query += CourseCode + '", StudentID = '
    query += str(StudentID) + ' WHERE GroupID = '
    query += str(userID)

    # executing and committing the update statement
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    return 'Study Group information updated successfully!'


@studygroup.route('/delete-studygroup/<userID>', methods=['DELETE'])
def delete_studygroup(userID):
    # constructing the query
    query = 'DELETE FROM StudyGroup WHERE GroupID = ' + str(userID)

    # executing and committing the delete statement
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    return 'Study Group deleted successfully!'