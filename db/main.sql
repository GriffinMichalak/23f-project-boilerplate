CREATE DATABASE StudyStage;
USE StudyStage;

CREATE TABLE Student (
  StudentID INT AUTO_INCREMENT PRIMARY KEY,
  FirstName VARCHAR(255) NOT NULL,
  LastName VARCHAR(255) NOT NULL,
  Year INT NOT NULL,
  GPA FLOAT NOT NULL
);

CREATE TABLE Professor (
  FacultyID INT AUTO_INCREMENT PRIMARY KEY,
  FirstName VARCHAR(255) NOT NULL,
  LastName VARCHAR(255) NOT NULL,
  Year_Hired INT NOT NULL,
  Tenured BOOLEAN NOT NULL
);

CREATE TABLE TeachingAssistant (
  TAID INT AUTO_INCREMENT PRIMARY KEY,
  FirstName VARCHAR(255) NOT NULL,
  LastName VARCHAR(255) NOT NULL,
  Semesters_Worked INT NOT NULL,
  Hourly_Wage FLOAT NOT NULL
);

CREATE TABLE StudyGroup (
  GroupID INT AUTO_INCREMENT PRIMARY KEY,
  Capacity INT NOT NULL,
  Description TEXT,
  Start_Time TIME NOT NULL,
  End_Time TIME NOT NULL,
  CourseCode VARCHAR(255) NOT NULL,
  StudentID INT NOT NULL,
  FOREIGN KEY (StudentID) REFERENCES Student(StudentID)
);

CREATE TABLE Class (
  CourseCode VARCHAR(255) PRIMARY KEY,
  Subject VARCHAR(255) NOT NULL,
  Title VARCHAR(255) NOT NULL,
  Description VARCHAR(255),
  NumStudentsEnrolled INT NOT NULL,
  StartTime TIME NOT NULL,
  EndTime TIME NOT NULL,
  Days_of_Week VARCHAR(7) NOT NULL,
  FacultyID INT NOT NULL,
  FOREIGN KEY (FacultyID) REFERENCES Professor(FacultyID)
);

CREATE TABLE OfficeHours (
  OfficeHoursID INT AUTO_INCREMENT PRIMARY KEY,
  Start_Time TIME NOT NULL,
  End_Time TIME NOT NULL,
  CourseCode VARCHAR(255) NOT NULL,
  TA_ID INT NOT NULL,
  FOREIGN KEY (CourseCode) REFERENCES Class(CourseCode),
  FOREIGN KEY (TA_ID) REFERENCES TeachingAssistant(TAID)
);

CREATE TABLE Location (
  LocationID INT AUTO_INCREMENT PRIMARY KEY,
  BuildingName VARCHAR(255),
  RoomNumber VARCHAR(255),
  NumberOfSeats INT,
  Link VARCHAR(255)
);

CREATE TABLE Assignment (
  AssignmentID INT AUTO_INCREMENT PRIMARY KEY,
  Title VARCHAR(255) NOT NULL,
  Description TEXT,
  InGroups BOOLEAN NOT NULL,
  CourseCode VARCHAR(255) NOT NULL,
  TA_ID INT NOT NULL,
  FOREIGN KEY (CourseCode) REFERENCES Class(CourseCode),
  FOREIGN KEY (TA_ID) REFERENCES TeachingAssistant(TAID)
);

CREATE TABLE Student_Class (
  StudentID INT NOT NULL,
  CourseCode VARCHAR(255) NOT NULL,
  FOREIGN KEY (StudentID) REFERENCES Student(StudentID),
  FOREIGN KEY (CourseCode) REFERENCES Class(CourseCode),
  PRIMARY KEY (StudentID, CourseCode)
);

CREATE TABLE Professor_Class (
  FacultyID INT NOT NULL,
  CourseCode VARCHAR(255) NOT NULL,
  FOREIGN KEY (FacultyID) REFERENCES Professor(FacultyID),
  FOREIGN KEY (CourseCode) REFERENCES Class(CourseCode),
  PRIMARY KEY (FacultyID, CourseCode)
);

CREATE TABLE StudyGroup_Location (
  GroupID INT NOT NULL,
  LocationID INT NOT NULL,
  FOREIGN KEY (GroupID) REFERENCES StudyGroup(GroupID),
  FOREIGN KEY (LocationID) REFERENCES Location(LocationID),
  PRIMARY KEY (GroupID, LocationID)
);

CREATE TABLE OfficeHours_Location (
  OfficeHoursID INT NOT NULL,
  LocationID INT NOT NULL,
  FOREIGN KEY (OfficeHoursID) REFERENCES OfficeHours(OfficeHoursID),
  FOREIGN KEY (LocationID) REFERENCES Location(LocationID),
  PRIMARY KEY (OfficeHoursID, LocationID)
);

CREATE TABLE StudyGroup_Assignment (
  GroupID INT NOT NULL,
  AssignmentID INT NOT NULL,
  FOREIGN KEY (GroupID) REFERENCES StudyGroup(GroupID),
  FOREIGN KEY (AssignmentID) REFERENCES Assignment(AssignmentID),
  PRIMARY KEY (GroupID, AssignmentID)
);

