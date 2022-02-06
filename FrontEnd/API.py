import os
import json
from flask import Flask
from flask_restful import Api, Resource
from apispec import APISpec
from marshmallow import Schema, fields
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_apispec.extension import FlaskApiSpec
from flask_apispec.views import MethodResource
from flask_apispec import marshal_with, doc, use_kwargs
from questionclass import AssignmentQuestion
from questionclass import Question
from databaseconnectionclass import DatabaseConnection
from queryclass import Query

app = Flask(__name__)
# Wraps the app in the API
api = Api(app)
app.config.update({
    'APISPEC_SPEC': APISpec(
        title='BE Python SQL Checker',
        version='v1',
        plugins=[MarshmallowPlugin()],
        openapi_version='2.0.0'
    ),
    'APISPEC_SWAGGER_URL': '/index.json',  # URI to access API Doc JSON
    'APISPEC_SWAGGER_UI_URL': '/'  # URI to access UI of API Doc
})
docs = FlaskApiSpec(app)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

# Uni City West: 10.233.119.91, Uni Mawson Lakes: 10.233.64.209, Home: 192.168.1.2
# Connection object
advConnection = DatabaseConnection('Driver={ODBC Driver 17 for SQL Server};', 'Server=DESKTOP-R7DFSAV;', 'Database=AdventureWorks2019;', 'Trusted_Connection=yes;')
connection = DatabaseConnection('Driver={ODBC Driver 17 for SQL Server};', 'Server=DESKTOP-R7DFSAV;', 'Database=SQLCheckerV2;', 'Trusted_Connection=yes;')
establishedAdvConnection = DatabaseConnection.getConnection(advConnection,'None')
establishedConnection = DatabaseConnection.getConnection(connection,'None')


# Assignment Question Resource 
class AssignmentQuestions(MethodResource,Resource):
    class AssignmentQuestionsResponseSchema(Schema):
            message = fields.Dict(default={})    

    # Function that displays all the assignment questions to the student
    @doc(description='Get Assignment Question.', tags=['Question'])
    @marshal_with(AssignmentQuestionsResponseSchema)
    def get(self):
        '''
        Get Method to obtain assignment question
        '''
        # Retrieves all the assignment questions from the database
        assignmentQuestions = AssignmentQuestion.getAllAssignmentQuestions(establishedConnection)
        # Assignment Question dictionary for the student to select from (JSON valid)
        assignmentQuestionDict = {}

        # Makes a dictionary of assignment question to display to the student
        for assignmentQuestion in assignmentQuestions:
            assignmentQuestionDict[str(assignmentQuestion.questionNumber)] = (str(assignmentQuestion.question))
        # return assignmentQuestionDict
        return {'message':assignmentQuestionDict}
    
class StudentQuery(MethodResource,Resource):
    class StudentQueryResponseSchema(Schema):
            Feedback = fields.Str(default='No Feedback')            

    # Functions that accepts the student's assignment question selection and their query attempt runs the comparison functionality and returns
    # feedback to the student
    @doc(description='Get Question Feedback.', tags=['Feedback'])
    @marshal_with(StudentQueryResponseSchema)
    def post(self, questionNumber, studentSQL):
        '''
        Post Method to obtain feedback on assignment question with sql input
        '''
        # Converts the student's sql back from its JSON serialised format 
        studentSQL = Query.unSerialise(studentSQL)
        # Finds the test query based of the student's assignment question input
        testQuery = Query.getTestQuery(establishedConnection, questionNumber)
        # Makes the assignment question's sql executable
        testQuery.sql = Query.makeExecutable(testQuery.sql)
        # Turns the student's sql into a query object
        studentQuery = Query(testQuery.questionId, Query.makeExecutable(studentSQL), 10.0)
        # Compares the student's query with the test query
        testQuery.compareQuery(studentQuery, establishedAdvConnection)
        # Returns the feedback from the comparison to the student
        return {"Feedback": studentQuery.feedback}

# / is the default url endpoint
api.add_resource(AssignmentQuestions, "/assignmentquestion")
api.add_resource(StudentQuery, "/studentquery/<string:questionNumber>/<string:studentSQL>")

# All swagger related docs are appended here
docs.register(AssignmentQuestions)
docs.register(StudentQuery)

# Runs the API
if __name__ == "__main__":
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    PORT = 80
    app.run(host='0.0.0.0', port = PORT)