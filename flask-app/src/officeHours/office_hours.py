from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db

office_hours = Blueprint('office_hours', __name__)

# Get all office_hours from StudyStage
@office_hours.route('/all', methods=['GET'])
def get_office_hourss():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM OfficeHours')
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

# get a specific office hours by ID
@office_hours.route('/get-office-hours/<office_hoursID>', methods=['GET'])
def get_office_hours(office_hoursID):
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM OfficeHours WHERE OfficeHoursID = {0}'.format(office_hoursID))
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

# create an office hours 
@office_hours.route('/create-office_hours', methods=['POST'])
def add_office_hours():
    
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    Start_Time = the_data['Start_Time']
    End_Time = the_data['End_Time']
    CourseCode = the_data['CourseCode']
    TA_ID = the_data['TA_ID']

    # Constructing the query
    query = 'INSERT INTO office_hours (Start_Time, End_Time, CourseCode, TA_ID) VALUES ("'
    query += str(Start_Time) + '", "'
    query += str(End_Time) + '", "'
    query += CourseCode + '", "'
    query += str(TA_ID) + ')'
    current_app.logger.info(query)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Successfully created a new Office Hours!'

# Update information about an office hours
@office_hours.route('/update-office_hours/<office_hoursID>', methods=['PUT'])
def update_office_hours(office_hoursID):

    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    Start_Time = the_data['Start_Time']
    End_Time = the_data['End_Time']
    CourseCode = the_data['CourseCode']
    TA_ID = the_data['TA_ID']

    # constructing the query
    query = 'UPDATE OfficeHours SET Start_Time = "'
    query += str(Start_Time) + '", End_Time = "'
    query += End_Time + '", CourseCode = "'
    query += CourseCode + '", TA_ID = "'
    query += str(TA_ID) + ' WHERE OfficeHoursID = '
    query += str(office_hoursID)

    # executing and committing the update statement
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    return 'Office Hours information updated successfully!'

# Delete an office hours
@office_hours.route('/delete-office_hours/<office_hoursID>', methods=['DELETE'])
def delete_office_hours(office_hoursID):
    # constructing the query
    query = 'DELETE FROM OfficeHours WHERE OfficeHoursID = ' + str(office_hoursID)

    # executing and committing the delete statement
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    return 'OfficeHours deleted successfully!'