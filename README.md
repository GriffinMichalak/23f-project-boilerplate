# Study Stage 👨‍🏫📚👩‍🏫

StudyStage is a comprehensive, data-driven platform designed to facilitate a collaborative learning experience for students. It simplifies the process of finding and connecting with study partners or group members for various academic activities, such as group projects, exams, and even volunteering tutor sessions. Users can create profiles, search for suitable study buddies, send and accept requests, and efficiently manage their study sessions. StudyStage also includes features such as session capacity management, class-specific searches, favorite locations for study sessions, post-filtering, and account management. With StudyStage, students can streamline their academic collaboration, making it easier to excel in their studies.

## Features
* Create student profiles
* Search for suitable study buddies
* Send and accept study requests
* Manage study sessions
* Session capacity management
* Class-specific searches
* Favorite locations for study sessions
* Post-filtering
* Account management

## Installation
This repo contains a boilerplate setup for spinning up 3 Docker containers: 
1. A MySQL 8 container for obvious reasons
1. A Python Flask container to implement a REST API
1. A Local AppSmith Server

**Important** - you need Docker Desktop installed

1. Clone this repository.  
1. Create a file named `db_root_password.txt` in the `secrets/` folder and put inside of it the root password for MySQL. 
1. Create a file named `db_password.txt` in the `secrets/` folder and put inside of it the password you want to use for the a non-root user named webapp. 
1. In a terminal or command prompt, navigate to the folder with the `docker-compose.yml` file.  
1. Build the images with `docker compose build`
1. Start the containers with `docker compose up`.  To run in detached mode, run `docker compose up -d`. 
  
## Database Schema
The StudyStage database schema consists of the following tables:

* Student: Stores student information, including first name, last name, year, and GPA.
* Professor: Stores professor information, including first name, last name, year hired, and tenured status.
* TeachingAssistant: Stores teaching assistant information, including first name, last name, semesters worked, and hourly wage.
* StudyGroup: Stores study group information, including capacity, description, start time, end time, course code, and student ID.
* Class: Stores class information, including course code, subject, title, description, number of students enrolled, start time, end time, days of the week, and faculty ID.
* OfficeHours: Stores office hours information, including start time, end time, course code, and TA ID.
* Location: Stores location information, including building name, room number, number of seats, and link.
* Assignment: Stores assignment information, including title, description, in groups flag, course code, and TA ID.
* Student_Class: Stores the relationship between students and classes.
* Professor_Class: Stores the relationship between professors and classes.
* StudyGroup_Location: Stores the relationship between study groups and locations.
* OfficeHours_Location: Stores the relationship between office hours and locations.
* StudyGroup_Assignment: Stores the relationship between study groups and assignments.

## Installation
To install StudyStage, you will need to create a database and run the SQL code provided in the given SQL files. You will also need to develop the front-end application, which will interact with the database to provide users with the functionality described in the Overview section.

## Usage
To use StudyStage, students will need to create a profile and provide information about their academic interests and availability for study sessions. They can then search for suitable study partners based on their criteria. Once they find potential study buddies, they can send requests to connect. If the requests are accepted, the students can then coordinate their study sessions.

Professors and teaching assistants can use StudyStage to create office hours and assignments. Students can then view and sign up for office hours or join study groups that are focused on specific assignments.

## Benefits
StudyStage can provide several benefits to students, professors, and teaching assistants, including:

* Improved academic performance: By facilitating collaboration and peer learning, StudyStage can help students improve their understanding of course material and achieve better grades.
* Increased efficiency: By streamlining the process of finding study partners and coordinating study sessions, StudyStage can help students make more efficient use of their time.
* Reduced stress: By providing a platform for connecting with others who are facing similar academic challenges, StudyStage can help reduce stress and anxiety among students.
* Enhanced communication skills: By engaging in collaborative learning activities, students can develop their communication and interpersonal skills.
Improved teaching effectiveness: By providing students with opportunities for additional support and guidance, StudyStage can help professors and teaching assistants improve the effectiveness of their teaching.

## Licence
StudyStage is licensed under the MIT License. This means that you are free to use, modify, and distribute the software for any purpose, including commercial use. The only requirement is that you include the original MIT License with any distribution of the software. A copy of the MIT License can be found in the LICENSE file.





