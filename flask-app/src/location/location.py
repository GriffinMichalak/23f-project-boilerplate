from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db

location = Blueprint('location', __name__)

# Get all location from StudyStage
@location.route('/all', methods=['GET'])
def get_locations():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM Location')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'

    # return "Number of location fetched: " + str(len(theData)) + ""

    return the_response

# Get customer detail for customer with particular userID
@location.route('/get-location/<locationID>', methods=['GET'])
def get_location(locationID):
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM Location WHERE LocationID = {0}'.format(locationID))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

@location.route('/create-location', methods=['POST'])
def add_location():
    
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    BuildingName = the_data['BuildingName']
    RoomNumber = the_data['RoomNumber']
    NumberOfSeats = the_data['NumberOfSeats']
    Link = the_data['Link']

    # Constructing the query
    query = 'INSERT INTO Location (BuildingName, RoomNumber, NumberOfSeats, Link) VALUES ("'
    query += BuildingName + '", "'
    query += str(RoomNumber) + '", "'
    query += str(NumberOfSeats) + '", '
    query += Link + ')'
    current_app.logger.info(query)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Successfully created a new Location'

@location.route('/update-location/<locationID>', methods=['PUT'])
def update_location(locationID):
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    BuildingName = the_data['BuildingName']
    RoomNumber = the_data['RoomNumber']
    NumberOfSeats = the_data['NumberOfSeats']
    Link = the_data['Link']

    # constructing the query
    query = 'UPDATE Location SET BuildingName = "'
    query += BuildingName + '", RoomNumber = "'
    query += str(RoomNumber) + '", NumberOfSeats = '
    query += str(NumberOfSeats) + ', Link = '
    query += Link + ' WHERE LocationID = '
    query += str(locationID)
 
    # executing and committing the update statement
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    return 'Location information updated successfully!'

@location.route('/delete-loccation/<locationID>', methods=['DELETE'])
def delete_location(locationID):
    # constructing the query
    query = 'DELETE FROM Location WHERE LocationID = ' + str(locationID)

    # executing and committing the delete statement
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    return 'Location deleted successfully!'