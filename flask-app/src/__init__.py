# Some set up for the application 

from flask import Flask
from flaskext.mysql import MySQL

# create a MySQL object that we will use in other parts of the API
db = MySQL()

def create_app():
    app = Flask(__name__)
    
    # secret key that will be used for securely signing the session 
    # cookie and can be used for any other security related needs by 
    # extensions or your application
    app.config['SECRET_KEY'] = 'someCrazyS3cR3T!Key.!'

    # these are for the DB object to be able to connect to MySQL. 
    app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_PASSWORD'] = open('/secrets/db_root_password.txt').readline().strip()
    app.config['MYSQL_DATABASE_HOST'] = 'db'
    app.config['MYSQL_DATABASE_PORT'] = 3306
    app.config['MYSQL_DATABASE_DB'] = 'StudyStage'  # Change this to your DB name

    # Initialize the database object with the settings above. 
    db.init_app(app)
    
    # Add the default route
    # Can be accessed from a web browser
    # http://ip_address:port/
    # Example: localhost:8001
    @app.route("/")
    def welcome():
        return "<h1>Welcome to StudyStage app</h1>"

    # Import the various Beluprint Objects
    from src.students.students import students
    from src.professors.professors import professors
    from src.teachingAssistants.teachingAssistants import teachingAssistants
    from src.studygroup.studygroup import studygroup
    from src.location.location import location
    from src.assignment.assignment import assignment
    from src.officeHours.office_hours import office_hours
    from src.classes.classes import classes
    from src.attendsOfficeHour.attendsOfficeHour import attends_office_hour

    # Register the routes from each Blueprint with the app object
    # and give a url prefix to each
    app.register_blueprint(students, url_prefix='/students')
    app.register_blueprint(professors, url_prefix='/professor')
    app.register_blueprint(teachingAssistants, url_prefix='/ta')
    app.register_blueprint(studygroup, url_prefix='/studygroup')
    app.register_blueprint(location, url_prefix='/location')
    app.register_blueprint(assignment, url_prefix='/assignment')
    app.register_blueprint(office_hours, url_prefix='/officehours')
    app.register_blueprint(classes, url_prefix='/classes')
    app.register_blueprint(attends_office_hour, url_prefix='/attends-officehours')

    # Don't forget to return the app object
    return app