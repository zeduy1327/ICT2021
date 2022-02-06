import pyodbc as po
import uuid
from databaseconnectionclass import DatabaseConnection
from difficuiltyclass import Difficulty
from tkinter import messagebox

class Question():
    questionId = str
    question = str
    difficultyId = str

    # Constructor
    def __init__(self, *args):
        # Constructor for reading an existing question object back from the database (i.e. already has questionId)
        if len(args) == 3:
            self.questionId = args[0]
            self.question = args[1]
            self.difficultyId = args[2]
        # Constructor for creating a new question object (i.e. needs a questionId to be generated in the constructor)
        elif len(args) == 2:
            self.questionId = Question.generateId()
            self.question = args[0]
            self.difficultyId = args[1]

    # Function that stores the question object in the database
    def storeQuestion(self, connection):
        # Verifies whether or not the question is already in the database first
        if Question.getQuestionRecord(self.questionId, connection) == []:
            query = "INSERT INTO Question (QuestionId, Question, DifficultyId) VALUES ('" + self.questionId + "', '" + self.question + "', '" + self.difficultyId + "');"

            # Create cursor (basically what takes commands to the database and returns the data from it) 
            c = connection.cursor()

            # Try to query the database 
            try:
                c.execute(query)
            # Catches any problems with the query
            except:
                print ("There was an error querying the database. Check your database connection via the database connection page")

            # Commit changes
            connection.commit()
        
        else:
            print ("Question Already Exists")
    
    # Function that generates a GUID for the question object
    @staticmethod 
    def generateId():
        return str(uuid.uuid1())

    # Static function that returns a question object if it can be found
    @staticmethod
    def getQuestionRecord(questionId, connection):
        query="Select * from dbo.Question q where q.QuestionId = '" + questionId + "'"
        
        # Create cursor (basically what takes commands to the database and returns the data from it) 
        c = connection.cursor()

        # Try to query the database 
        try:
            c.execute(query)
        # Catches any problems with the query
        except Exception as e:
            print (e)
        
        # Stores the record retrieved by the cursor (if any)
        records = c.fetchall()
        
        
        # Converts the record (if any) into a question object and returns it
        if records != []:
            question = Question(records[0], records[1], records[2])
            return question
        
        # Commit changes
        connection.commit()
        
        # Returns an empty array if no question was found
        return []

    # Static function that alters the description of a question object so that its storable in the database (adds double single quotes if needed)
    @staticmethod
    def makeStorable(string):
        index = 0
        lastLocation = 0
        returnString = ""
        for char in string:
            if char=="'":
                returnString += string[lastLocation:index+1] + "'"
                lastLocation = index+1
            index+=1
        returnString += string[lastLocation:len(string)]
        return returnString

    # Function that reads all the questions from the database and returns them in a question object array
    @staticmethod
    def readAllQuestions(connection):
        # Create cursor (basically what takes commands to the database and returns the data from it) 
        c = connection.cursor()

        # Try to query the database to identify and retrieve the questions 
        try:
            c.execute("SELECT Question.* FROM Question")
        # Catches any problems with the sql 
        except Exception as e: 
            print (e)

        # Stores the data retrieved by the cursor in a questionData array variable
        questionData = c.fetchall()

        # Commit changes
        connection.commit()

        questionObjects = []
        # Converts each of the question records read from the database into an actual question object and stores them in an array
        for record in questionData:
            question = Question(record[0], record[1], record[2])
            questionObjects.append(question)

        # Returns the question object array
        return questionObjects

    # Reads all the questions associated with a specific difficulty from the database
    @staticmethod
    def readAllDifficultyQuestions(connection, difficultyId):
        # Create cursor (basically what takes commands to the database and returns the data from it) 
        c = connection.cursor()

        # Try to query the database to identify and retrieve the questions 
        try:
            c.execute("SELECT Question.* FROM Question WHERE DifficultyId = '" + difficultyId + "';")
        # Catches any problems with the sql 
        except Exception as e: 
            print (e)

        # Stores the data retrieved by the cursor in a questionData array variable
        questionData = c.fetchall()

        # Commit changes
        connection.commit()

        questionObjects = []
        # Converts each of the question records read from the database into an actual question object and stores them in an array
        for record in questionData:
            question = Question(record[0], record[1], record[2])
            questionObjects.append(question)

        # Returns the question object array
        return questionObjects        

# Selected test querys translate into their questions becoming Assignment Questions
class AssignmentQuestion(Question):
    questionId: str
    question: str
    difficultyId: str
    assignmentQuestionId: str
    semesterId: str
    questionNumber: str
    
    # Constructor
    def __init__(self, *args):
        # Constructor for reading an existing assignmnet question object back from the database (i.e. already has an assignmentQuestionId)
        if len(args) == 6:
            self.questionId = args[0]
            self.question = args[1]
            self.difficultyId = args[2]
            self.assignmentQuestionId = args[3]
            self.semesterId = args[4]
            self.questionNumber = args[5]
        # Constructor for creating a new assignment question object (i.e. one that needs an assignmentQuestionID to be generated)
        elif len(args) == 5:
            self.questionId = args[0]
            self.question = args[1]
            self.difficultyId = args[2]
            self.assignmentQuestionId = Question.generateId()
            self.semesterId = args[3]
            self.questionNumber = args[4]
    
    # Function that stores the assignment question object in the database
    def storeAssignmentQuestion(self, connection):
        if AssignmentQuestion.getAssignmentQuestionRecordQuestionId(self.questionId, connection) == []:
                query = "INSERT INTO dbo.AssignmentQuestion (QuestionId, Question, DifficultyId, assignmentQuestionId, semesterId, questionNumber) VALUES ('" + self.questionId + "', '" + self.question + "', '" + self.difficultyId + "', '" + self.assignmentQuestionId + "', '" + self.semesterId + "', '" + self.questionNumber + "');"

                # Create cursor (basically what takes commands to the database and returns the data from it) 
                c = connection.cursor()
                
                # Holds a error bool if one occurs
                storeError = False
                # Try to query the database 
                try:
                    c.execute(query)
                # Catches any problems with the query
                except:
                    storeError = True
                
                if storeError == False:
                    messagebox.showinfo(title='Success', message='Selected question was successfully saved as an Assignment Question.')
                elif storeError == True:
                    messagebox.showinfo(title='Error', message='There was a problem saving the selected question as an Assignment Question. Check your SQL Checker database connection and try again.')
                # Commit changes
                connection.commit()
            
        else:
            messagebox.showinfo(title='Error', message="A question with that question id has already been selected as an assignment question.")

    # Static function that returns an assignment question record if it can be found
    @staticmethod
    def getAssignmentQuestionRecordQuestionId(questionId, connection):
        query="Select * from dbo.AssignmentQuestion q where q.QuestionId = '" + questionId + "'"
        
        # Create cursor (basically what takes commands to the database and returns the data from it) 
        c = connection.cursor()

        # Try to query the database 
        try:
            c.execute(query)
        # Catches any problems with the query
        except Exception as e:
            print (e)
        
        # Stores the record retrieved by the cursor (if any)
        records = c.fetchall()
        
        # Converts the record into an assignment question object and returns it (if any was found)
        if records != []:
            assignmentQuestion = AssignmentQuestion(records[0][0], records[0][1], records[0][2], records[0][3], records[0][4], records[0][5])
            return assignmentQuestion

        return []
    
    # Static function that returns an assignment question record if it can be found
    @staticmethod
    def getAssignmentQuestionRecord(questionNumber, connection):
        query="Select * from dbo.AssignmentQuestion q where q.QuestionNumber = '" + questionNumber + "'"
        
        # Create cursor (basically what takes commands to the database and returns the data from it) 
        c = connection.cursor()

        # Try to query the database 
        try:
            c.execute(query)
        # Catches any problems with the query
        except Exception as e:
            print (e)
        
        # Stores the record retrieved by the cursor (if any)
        records = c.fetchall()
        
        # Converts the record into an assignment question object and returns it (if any was found)
        if records != []:
            assignmentQuestion = AssignmentQuestion(records[0][0], records[0][1], records[0][2], records[0][3], records[0][4], records[0][5])
            return assignmentQuestion

        return []

    # Static function that returns all the assignment questions in the form of an array
    @staticmethod
    def getAllAssignmentQuestions(connection):
        # Create cursor (basically what takes commands to the database and returns the data from it) 
        c = connection.cursor()

        # Try to query the database 
        try:
            c.execute("SELECT * FROM AssignmentQuestion;")
        # Catches any problems with the query
        except Exception as e:
            print (e)

        # Stores the assignment question records retrieved by the cursor
        data = c.fetchall()

        assignmentQuestions = []
        index = 0
        # Converts each record into an actual assignment question object
        for questionRecord in data:
            assignmentQuestion = AssignmentQuestion(data[index][0], data[index][1], data[index][2], data[index][3], data[index][4], data[index][5])
            assignmentQuestions.append(assignmentQuestion)
            index += 1
        
        return assignmentQuestions
        
    # Static function that generates an assignment question number for the object
    @staticmethod
    def generateAssignmentQuestionNumber(difficultyId, connection):
        assignmentQuestions = AssignmentQuestion.getAllAssignmentQuestions(connection)
        difficulty = Difficulty.getDifficultyFromId(difficultyId, connection)
        # Stores how many assignment questions there associated with the given difficulty
        associatedQuestions = []
        # print(assignmentQuestions)
        for question in assignmentQuestions:
            if question.difficultyId == difficultyId:
                associatedQuestions.append(question)
        
        questionCount = 0 
        for question in associatedQuestions:
            questionCount += 1

        return ("Q" + str(questionCount+1) + "00" + str(difficulty.diffLevel))

    # Static function that deletes an assignment question from the assignment question table in the database when it is deselected
    @staticmethod 
    def destoreAssignmentQuestion(questionId, connection):
        # Create cursor (basically what takes commands to the database and returns the data from it) 
        c = connection.cursor()

        deleteError = False
        # Try to query the database 
        try:
            c.execute("DELETE FROM dbo.AssignmentQuestion WHERE QuestionId = '" + questionId + "';")
        # Catches any problems with the query
        except:
            deleteError = True    
        
        if deleteError == False:
            messagebox.showinfo(title='Success', message='Deselected question was successfully removed as an Assignment Question.')
        elif deleteError == True:
            messagebox.showinfo(title='Error', message='There was a problem deselecting the question as an Assignment Question. Check your SQL Checker database connection and try again.')
        # Commit changes
        connection.commit()
    
if __name__=='__main__':
    connection = DatabaseConnection('Driver={SQL Server};', 'Server=DESKTOP-NFLVEPF;', 'Database=SQLCheckerV2;','Trusted_Connection=yes;')

    #testQuestion=Question("--Q1004-Find the First and Last Name of employees who have the same First name but different Last Name to that of customers (no duplicates)","a31269db-a0cc-11eb-a42d-00155dca3af8")
    #allQuestions=(Question.readAllQuestions(DatabaseConnection.getConnection(connection)))
    #for question in allQuestions:
        #print(question.questionId)
    testAssignmentQuestion=AssignmentQuestion("69c55de9-a0db-11eb-9dd0-00155dca3af8","Products come in various colours.  List the colours of the various products and the number of products for each of those colours if there are at least 10 items that came in that colour.  Where the colour is not specified, display N/A","a31269db-a0cc-11eb-a42d-00155dca3af8","c476b76f-ab00-11eb-bafa-00155dd652d9","Q1002")
    testAssignmentQuestion.storeAssignmentQuestion(DatabaseConnection.getConnection(connection))
    #testQuestion.storeQuestion(DatabaseConnection.getConnection(connection))