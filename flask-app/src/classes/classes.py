from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db

classes = Blueprint('classes', __name__)

# Get all classess from StudyStage
@classes.route('/all', methods=['GET'])
def get_classess():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM Class')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        # Convert StartTime and EndTime to strings
        row_dict = dict(zip(row_headers, row))
        row_dict['StartTime'] = str(row_dict['StartTime'])
        row_dict['EndTime'] = str(row_dict['EndTime'])
        json_data.append(row_dict)

    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'

    return the_response

@classes.route('/get-class/<courseCode>', methods=['GET'])
def get_classes(courseCode):
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM Class WHERE CourseCode = {0}'.format(courseCode))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        row_dict = dict(zip(row_headers, row))
        row_dict['StartTime'] = str(row_dict['StartTime'])
        row_dict['EndTime'] = str(row_dict['EndTime'])
        json_data.append(row_dict)

    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

@classes.route('/student-class/<sID>', methods=['GET'])
def get_class_by_student(sID):
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM Student_Class WHERE StudentID = {0}'.format(sID))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        row_dict = dict(zip(row_headers, row))
        # row_dict['StartTime'] = str(row_dict['StartTime'])
        # row_dict['EndTime'] = str(row_dict['EndTime'])
        json_data.append(row_dict)

    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

@classes.route('/prof-class/<pID>', methods=['GET'])
def get_class_by_prof(pID):
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM Class WHERE FacultyID = {0}'.format(pID))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        row_dict = dict(zip(row_headers, row))
        row_dict['StartTime'] = str(row_dict['StartTime'])
        row_dict['EndTime'] = str(row_dict['EndTime'])
        json_data.append(row_dict)

    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


@classes.route('/create-classes', methods=['POST'])
def add_classes():
    
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    CourseCode = the_data['CourseCode']
    Subject = the_data['Subject']
    Title = the_data['Title']
    Description = the_data['Description']
    NumStudentsEnrolled = the_data['NumStudentsEnrolled']
    StartTime = the_data['StartTime']
    EndTime = the_data['EndTime']
    Days_of_Week = the_data['Days_of_Week']
    FacultyID = the_data['FacultyID']

    # Constructing the query
    query = 'INSERT INTO Class (CourseCode, Subject, Title, Description, NumStudentsEnrolled, StartTime, EndTime, Days_of_Week, FacultyID) VALUES ("'
    query += CourseCode + '", "'
    query += Subject + '", "'
    query += Title + '", "'
    query += Description + '", "'
    query += str(NumStudentsEnrolled) + '", "'
    query += StartTime + '", "'
    query += EndTime + '", "'
    query += Days_of_Week + '", '
    query += str(FacultyID) + ')'

    current_app.logger.info(query)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Successfully created a new Study Group'

# Update information about a class
@classes.route('/update-classes/<courseCode>', methods=['PUT'])
def update_classes(courseCode):
    # collecting data from the request object
    the_data = request.json
    current_app.logger.info(the_data)

    # extracting the variables
    CourseCode = the_data['CourseCode']
    Subject = the_data['Subject']
    Title = the_data['Title']
    Description = the_data['Description']
    NumStudentsEnrolled = the_data['NumStudentsEnrolled']
    StartTime = the_data['StartTime']
    EndTime = the_data['EndTime']
    Days_of_Week = the_data['Days_of_Week']
    FacultyID = the_data['FacultyID']

    # constructing the query
    query = 'UPDATE Class SET CourseCode = "'
    query += str(CourseCode) + '", Subject = "'
    query += Subject + '", Title ="'
    query += Title + '", Description = "'
    query += Description + '", NumStudentsEnrolled = "'
    query += str(NumStudentsEnrolled) + '", StartTime = "'
    query += StartTime + '", EndTime = "'
    query += EndTime + '", Days_of_Week = "'
    query += Days_of_Week + '", FacultyID = '
    query += str(FacultyID) + ' WHERE CourseCode = '
    query += courseCode

    # executing and committing the update statement
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    return 'Class information updated successfully!'


@classes.route('/delete-classes/<courseCode>', methods=['DELETE'])
def delete_classes(courseCode):
    # constructing the query
    query = 'DELETE FROM Class WHERE CourseCode = ' + courseCode

    # executing and committing the delete statement
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    return 'Study Group deleted successfully!'