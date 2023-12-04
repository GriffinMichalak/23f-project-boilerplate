from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db

attends_office_hour = Blueprint('attends_office_hour', __name__)

# Get all attends_office_hour from StudyStage
@attends_office_hour.route('/all', methods=['GET'])
def get_attends_attends_office_hour():
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

# create an office hours 
@attends_office_hour.route('/create-attendsOH', methods=['POST'])
def add_attends_office_hour():
    
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    StudentID = the_data['StudentID']
    OfficeHoursID = the_data['OfficeHoursID']
    AssignmentID = the_data['AssignmentID']

    # Constructing the query
    query = 'insert into Attends_OH (StudentID, OfficeHoursID, AssignmentID) VALUES ("'
    query += str(StudentID) + '", "'
    query += str(OfficeHoursID) + '", "'
    query += str(AssignmentID) + ')'
    current_app.logger.info(query)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Successfully created a new Attends Office Hours!'

# Update information about an office hours
@attends_office_hour.route('/update-attendsOH/<attends_office_hourID>', methods=['PUT'])
def update_attends_office_hour(attends_office_hourID):

    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    StudentID = the_data['StudentID']
    OfficeHoursID = the_data['OfficeHoursID']
    AssignmentID = the_data['AssignmentID']

    # constructing the query
    query = 'UPDATE Attends_OH SET StudentID = "'
    query += str(StudentID) + '", OfficeHoursID = "'
    query += str(OfficeHoursID) + '", AssignmentID = "'
    query += str(AssignmentID) + ' WHERE StudentID = '
    query += str(attends_office_hourID)

    # executing and committing the update statement
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    return 'Office Hours information updated successfully!'

# Delete an office hours
@attends_office_hour.route('/delete-attendsOH/<attends_office_hourID>', methods=['DELETE'])
def delete_attends_office_hour(attends_office_hourID):
    # constructing the query
    query = 'DELETE FROM Attends_OH WHERE StudentID = ' + str(attends_office_hourID)

    # executing and committing the delete statement
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    return 'OfficeHours deleted successfully!'