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
        # row_dict['Start_Time'] = str(row_dict['Start_Time'])
        # row_dict['End_Time'] = str(row_dict['End_Time'])
        json_data.append(row_dict)

    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'

    return the_response

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