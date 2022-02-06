import pyodbc as po
import uuid
from time import time
from zipfile import ZipFile
from databaseconnectionclass import DatabaseConnection
from User import User
from questionclass import Question
from deductionclass import Deduction
from difficuiltyclass import Difficulty
from Marks import Marks
from questionclass import AssignmentQuestion
import ntpath

class Query():
    queryId = str
    questionId = str
    sql = str
    dataRetrieved = str
    timeToExecute = float
    score = float
    feedback = str
    comparisonCriteria = [False, False, False, False, False, False, False, False]

    # Constructor
    def __init__(self, *args):
        # Constructor for a new query object (a query Id is generated in the constructor and therefore 
        # is not passed in as an argument, hence, 5 arguments instad of 6)
        if len(args)==5:
            self.queryId = self.generateId()
            self.questionId = args[0]
            self.sql = args[1]
            self.dataRetrieved = args[2]
            self.timeToExecute = args[3]
            self.score = args[4]
        # Constructor for reading an existing query from the database (i.e. a query that already has an Id, hence, 
        # 4 arguments instead of 5
        elif len(args)==4:
            self.queryId = args[0]
            self.questionId = args[1]
            self.sql = args[2]
            self.score = args[3]
        # Constructor for a new query object that hasnt got the data from the comparison functionality (i.e. data retrieved, time to execute etc. are null)
        elif len(args)==3:
            self.queryId = self.generateId()
            self.questionId = args[0]
            self.sql = args[1]
            self.score = args[2]
        # Constructor for reading query objects from a student file
        elif len(args) == 0:
            self.queryId = self.generateId()
        
    # Function that runs the query object
    def runQuery(self, connection):
        # Create cursor (basically what takes commands to the database and returns the data from it) 
        c = connection.cursor()

        # Stores the time when the query starts to execute
        start = time()
        # Try to query the database given the query objects sql 
        try:
            c.execute(self.sql)
        # Catches any problems with the sql 
        except Exception as e: 
            print (e)
            return "Error"

        # Stores the time when the query has finished executing 
        finish = time()

        # Set the timeToExecute of the query object as the time difference between the start of the query
        # executing and when it finished executing
        self.timeToExecute = finish - start

        # Stores the data retrieved by the cursor in a records variable
        records = c.fetchall()
        
        # Sets the dataRetrieved variable of the query object to the retrieved records 
        self.dataRetrieved = records

        # Commit changes
        connection.commit()
        return "Success"

    # function that generates a GUID for the query object 
    def generateId(self):
        return str(uuid.uuid1())

    # Function that compares a query object (testQuery) with another query object (studentQuery) in terms of columns, rows, time to execute etc.
    def compareQuery(self, studentQuery, connection):
        # stores a count of how many columns the test query/student query returned
        columnCount = 0
        studentColumnCount = 0
        # Stores a count of how many rows the test query/student query returned
        rowCount = 0
        studentRowCount = 0
        # Stores whether the student query retrieved columns/rows in the same order as the test query
        correctColumnOrder = True
        correctRowOrder = True
        # Stores the words from the test/student query sql
        wordCount = 0
        joinCount = 0
        testQueryWords = []
        studentQueryWords = []

        # Runs the test query to retrieve the expected data (columns, rows, time to execute etc.)
        self.runQuery(connection)
        
        # Runs the student query to retrieve the expected data (columns, rows, time to execute etc.)
        errorChecker = studentQuery.runQuery(connection)
        
        # Stops the comparison functionality early if the student query didnt execute properly.
        if errorChecker == "Error":
            studentQuery.comparisonCriteria = [False, False, False, False, False, False, False, False]
            studentQuery.timeToExecute = 0.0
            studentQuery.dataRetrieved = "Broken Query"
            studentQuery.feedback = "Student Query was not formatted correctly to execute and therefore failed everytest."
            return "Error"

        # Holds a record from both the test query and the student query to see if they both contain the same number of columns
        testRecord = studentQuery.dataRetrieved[0]
        studentRecord = studentQuery.dataRetrieved[0]

        # Determines the number of columns retrieved by the test query
        for column in testRecord:
            columnCount +=1
        
        # Determines the number of columns retrieved by the student query 
        for column in studentRecord:
            # Try/except to catch index out of bounds exceptions if they occur
            try:
                # Determines if the student query retrieved the same column order as the test query
                if studentQuery.dataRetrieved[studentColumnCount][studentColumnCount] != self.dataRetrieved[studentColumnCount][studentColumnCount]:
                    correctColumnOrder = False
            except:
                correctColumnOrder = False
            studentColumnCount +=1

        # Determines the number of rows retrieved by the test query
        for record in self.dataRetrieved:
            rowCount +=1
        # rowCount = len(dataRetrieved)

        # Determines the number of rows retrieved by the student query
        for record in studentQuery.dataRetrieved:
            # Try/except to catch index out of bounds exceptions if they occur
            try:
                # Checks if the row order of the student query is the same as the test query 
                if studentQuery.dataRetrieved[studentRowCount] != self.dataRetrieved[studentRowCount]:
                    correctRowOrder = False
            except:
                correctRowOrder = False
            studentRowCount +=1
        

        # Determines if the student query and the student query contain any joins
        # Breaks up the test query/student query sql into individual words and stores them in an array
        testQueryJoins = []
        studentQueryJoins = []
        testQueryWords = self.sql.split(' ')
        studentQueryWords = studentQuery.sql.split(' ')
        
        for word in testQueryWords:
            if word == "join" or word == "JOIN":
                testQueryJoins.append(str(testQueryWords[wordCount - 1]).lower() + " " + str(testQueryWords[wordCount]).lower())
                joinCount += 1
            wordCount += 1
        wordCount = 0
        joinCount = 0
        for word in studentQueryWords:
            if word == "join" or word == "JOIN":
                studentQueryJoins.append(str(studentQueryWords[wordCount -1]).lower() + " " + str(studentQueryWords[wordCount]).lower())
                joinCount +=1
            wordCount +=1

        # Makes the comparison about the retrieved columns (stored in the query's comparisonCriteria array variable)
        if columnCount == studentColumnCount and columnCount != 0 and studentColumnCount != 0:
            studentQuery.comparisonCriteria[0] = True
            # Feedback for the student based of the comparison criteria 
            studentQuery.feedback = ("Correct number of columns retrieved: Test query retrieved: " + str(columnCount) + " columns while Student query retrieved: " + str(studentColumnCount) + " columns.")
        # If the student query retrieved the wrong number of columns or no columns
        elif columnCount != studentColumnCount:
            # Feedback for the student based of the comparison criteria 
            studentQuery.feedback = ("Incorrect number of columns retrieved: Test query retrieved: " + str(columnCount) + " columns while Student query retrieved: " + str(studentColumnCount) + " columns.")
        # If the student query and test query didnt retrieve any columns
        elif columnCount == 0 and studentColumnCount == 0:
            studentQuery.feedback = ("Neither the student query or the test query retrieved any columns.")
        
        # Makes the comparison about the retrieved rows (stored in the query's comparisonCriteria array variable)
        if rowCount == studentRowCount and rowCount != 0 and studentRowCount != 0:
            studentQuery.comparisonCriteria[1] = True
            # Feedback for the student based of the comparison criteria 
            studentQuery.feedback += (" Correct number of rows retrieved: Test query retrieved: " + str(rowCount) + " rows while Student query retrieved: " + str(studentRowCount) + " rows.")
        # If the student query retrieved the wrong number of rows or no rows
        elif rowCount != studentRowCount:
            studentQuery.feedback += (" Incorrect number of rows retrieved: Test query retrieved: " + str(rowCount) + " rows while Student query retrieved: " + str(studentRowCount) + " rows.")
        # If the student query and the test query didnt retrieve any rows
        elif rowCount == 0 and studentRowCount == 0:
            studentQuery.feedback += (" Nor the student query or the test query retrieved any rows.")
        
        # Makes the comparison about the retrieved values (stored in the query's comparisonCriteria array variable) 
        if self.dataRetrieved == studentQuery.dataRetrieved:
            # Feedback for the student based of the comparison criteria
            studentQuery.feedback += (" The student query returned the same values as the test query.")
            studentQuery.comparisonCriteria[2] = True
        elif self.dataRetrieved != studentQuery.dataRetrieved:
            # Feedback for the student based of the comparison criteria
            studentQuery.feedback += (" The student query returned different values to the test query.")

        # Makes the comparison about the column order (stored in the query's comparisonCriteria array variable)
        if correctColumnOrder == True:
            # Feedback for the student based of the comparison criteria
            studentQuery.feedback += (" The student query retrieved the correct order of columns.")
            studentQuery.comparisonCriteria[3] = True
        elif correctColumnOrder == False:
            # Feedback for the student based of the comparison criteria
            studentQuery.feedback += (" The student query retrieved the incorrect order of columns.")
        
        # Makes the comparison about the row order (stored in the query's comparisonCriteria array variable)
        if correctRowOrder == True:
            # Feedback for the student based of the comparison criteria
            studentQuery.feedback += (" The student query retrieved the correct order of rows.")
            studentQuery.comparisonCriteria[4] = True
        elif correctRowOrder == False:
            # Feedback for the student based of the comparison criteria
            studentQuery.feedback += (" The student query retrieved the incorrect order of rows.")

        # Makes the comparison about the time to execute (stored in the query's comparisonCriteria array variable)
        if self.timeToExecute < studentQuery.timeToExecute:
            # Feedback for the student based of the comparison criteria
            studentQuery.feedback += (" Student Query executed inefficiently: Test query took: " + str(self.timeToExecute) + " milliseconds to execute while Student query took: " + str(studentQuery.timeToExecute) 
            + " milliseconds to execute.")
        elif self.timeToExecute >= studentQuery.timeToExecute:
            # Feedback for the student based of the comparison criteria
            studentQuery.feedback += (" Student Query executed efficiently: Test query took: " + str(self.timeToExecute) + " milliseconds to execute while Student query took: " + str(studentQuery.timeToExecute) 
            + " milliseconds to execute.")
            studentQuery.comparisonCriteria[5] = True
        
        # Makes the comparison about if the correct joins were used in the student query
        # Holds the joins that the test/student query both used and the ones they didnt
        sameJoins = []
        differentJoins = []

        # Finds all the joins that the test query and student query share/dont share
        for studentJoin in studentQueryJoins:
            if studentJoin in testQueryJoins:
                sameJoins.append(studentJoin)
            else: 
                differentJoins.append(studentJoin)
        
        # Feedback for the student based of the comparison criteria
        if differentJoins == [] and studentQueryJoins != [] and testQueryJoins != []:
            studentQuery.feedback += (" Student Query used the same joins as the test query.")
            studentQuery.comparisonCriteria[6] = True
        elif studentQueryJoins == [] and testQueryJoins == []:
            studentQuery.feedback += (" Both the student query and the test query didn't use a join.")
            studentQuery.comparisonCriteria[6] = True
        elif differentJoins != [] and studentQueryJoins != [] and testQueryJoins != []:
            studentQuery.feedback += (" Student Query used different joins to the test query.")

        # Determines if the student used TOP incorectly  
        wordCount = 0
        incorrectUseOfTop = False
        for word in studentQueryWords:
            if word == "TOP" or word == "top" and wordCount >= 4:
                studentQuery.feedback += (" Student Query incorrectly used TOP.")
                incorrectUseOfTop = True
                break
            wordCount += 1
            if word == "outer" or "OUTER":
                wordCount = 0
        
        # If wordCount has managed to go through the whole studentQueryWords array without finding an incorrect use of TOP
        # the comparisonCriteria associated with this test is set to True
        if incorrectUseOfTop == False:
            # Feedback for the student based of the comparison criteria
            studentQuery.feedback += (" Student Query did not contain any incorrect uses of TOP.")
            studentQuery.comparisonCriteria[7] = True
        #print ("you made it again")
        #print (studentQuery.comparisonCriteria)
        #print (studentQuery.feedback)
        return "Success" 
    
    # Function that compares 'n' test queries (passed in as an array) against 'n' student queries (passed in as an array)
    @staticmethod
    def compareAll(testQueries, studentQueries, checkerDatabaseConnection, dataDatabaseConnection):
        relatedQueries = []
        testQueryCount = 0
        while testQueryCount <= len(testQueries) - 1:
            #print ("you made it")
            # Retrieves and stores the deduction associated with the test query (for application to the student query object after the comparison)
            relatedDeductions = Deduction.readAllDeductions(testQueries[testQueryCount], checkerDatabaseConnection)
            
            # Finds all the student queries associated with a given test query
            for studentQuery in studentQueries:
                if studentQuery.questionId == testQueries[testQueryCount].questionId:
                    relatedQueries.append(studentQuery)
            
            # Compares each student query with the associated test query 
            for studentQuery in relatedQueries:
                # Calls the compareQuery function on test query and the corresponding student queries
                catchError = testQueries[testQueryCount].compareQuery(studentQuery, dataDatabaseConnection)
                # Applies the appropriate deductions following the results of the comparison
                for deduction in relatedDeductions:
                    deduction.applyDeduction(studentQuery)
                # Converts the student query objects sql and data retrieved into a storable format for the database
                studentQuery.sql = Query.makeStorable(str(studentQuery.sql))
                studentQuery.feedback = Query.makeStorable(str(studentQuery.feedback))
                studentQuery.dataRetrieved = Query.makeStorable(str(studentQuery.dataRetrieved))
                # Updates the student query record in the database and the associated mark in the marks table
                if catchError == "Success":
                    studentQuery.updateQueryData(checkerDatabaseConnection)
                    Marks.updateMarksData(checkerDatabaseConnection, studentQuery)
                elif catchError == "Error":
                    studentQuery.score = 0
                    studentQuery.updateQueryData(checkerDatabaseConnection)
                    Marks.updateMarksData(checkerDatabaseConnection, studentQuery)

            testQueryCount += 1
            # Resets the relatedQueries array for the next test query
            relatedQueries = []
        #print ("you compared all")

    # Function that updates the query object's data in the database with the results of the comparison (dataRetrieved, timeToExecute, score, feedback, comparisonCriteria)
    def updateQueryData(self, connection):
        # Query for the cursor
        query  = "UPDATE Query SET DataRetrieved = '" + str(self.dataRetrieved) + "', TimeToExecute = '" + str(self.timeToExecute) + "', Score = '" + str(self.score) + "', FeedBack = '" + str(self.feedback) + "', ComparisionCriteria = '" + str(self.comparisonCriteria) + "' WHERE QueryId = '" + self.queryId + "';"
        #print (query)
        # Create cursor (basically what takes commands to the database and returns the data from it) 
        c = connection.cursor()

        # Attempts to update the query's data in the database 
        try:
            c.execute(query)
        # Catches any problems with the update query/connection to the database
        except Exception as e:
            print(e)

        # Commit changes
        connection.commit()

    # Function that stores a query object into the database
    def storeQuery(self, connection):
        # Query for the cursor
        query = "INSERT INTO Query (QueryId, QuestionId, SQL, Score) VALUES ('" + self.queryId + "', '" + self.questionId + "', '" + self.sql + "', '" + str(self.score) + "');"  

        # Create cursor (basically what takes commands to the database and returns the data from it) 
        c = connection.cursor()

        # Try to query the database to store the query object
        try:
            c.execute(query)
        # Catches any problems with the query
        except Exception as e:
            print(e)

        # Commit changes
        connection.commit()

    # Function that reads 'n' number of student queries from a file and converts them into query objects
    @staticmethod
    def readIn(filePath, databaseConnection):
        # Open the file name
        openFile = open(filePath, 'r')

        with open(filePath) as openFile:
            # Extracts the fileName from the filePath
            fileName = ntpath.basename(filePath)
            fileNameParts = fileName.split('_')
            # Identify userName
            userName = fileNameParts[-2]
            print (userName)
            
            # Identify fullName 
            fullName = fileNameParts[0]
            print (fullName)

            # Creates a user object given the identified username
            user = User(fullName, userName)
            # Store user method which checks if the user is already in the database or needs to be added (adds them if needed)
            User.storeUser(databaseConnection, user)
            # Gets the users ID (their ID in the database, not their Uni SA Id) from the database given their username
            user.UserId = User.getIdFromUserName(databaseConnection, userName)

            # Identify questionId and the associated assigment question
            questionSplit = fileNameParts[-1].split('.')
            questionNumber = questionSplit[0]
            assignmentQuestion = AssignmentQuestion.getAssignmentQuestionRecord(str(questionNumber), databaseConnection)

            #print (assignmentQuestion)
            # Stores the contents of the student file as a string
            contents = openFile.read()
            lines = contents.splitlines()
            notComments = ""
            # Identify student sql query attempt
            for line in lines:
                li=line.strip()
                if not li.startswith("-"):
                    notComments += line
            
            studentSQL = notComments
            #print(studentSQL)
            
            # Makes a query object and a marks object (and stores both) given the questionId and userName identified in the student file 
            query = Query(assignmentQuestion.questionId, Query.makeStorable(studentSQL), 10.0)
            query.storeQuery(databaseConnection)
            mark = Marks(user.UserId, query.queryId, 10.0)
            return mark

    # Function that reads all the student queries from the database and returns them in a query object array
    @staticmethod
    def readAllStudentQueries(connection):
        # Create cursor (basically what takes commands to the database and returns the data from it) 
        c = connection.cursor()

        # Try to query the database to identify the queries that have a marks record (which highlights they are student queries) 
        try:
            c.execute("SELECT Query.* FROM Marks INNER JOIN Query ON Marks.QueryId = Query.QueryId")
        # Catches any problems with the sql 
        except Exception as e: 
            print (e)

        # Stores the data retrieved by the cursor in a studentQueries array variable
        studentQueriesData = c.fetchall()

        # Commit changes
        # connection.commit()

        studentQueryObjects = []
        # Converts each of the query records read from the database into an actual query object and stores them in an array
        for record in studentQueriesData:
            print (record)
            query = Query(record[0], record[1], Query.makeExecutable(record[2]), record[5])
            studentQueryObjects.append(query)
        
        # Returns the student query object array
        return studentQueryObjects

    # Function that reads all the test queries from the database and returns them in a query object array
    @staticmethod
    def readAllTestQueries(connection):
        # Create cursor (basically what takes commands to the database and returns the data from it) 
        c = connection.cursor()

        # Try to query the database to identify the queries that dont have a marks record (which highlights they are test queries) 
        try:
            c.execute("SELECT Query.* FROM Query LEFT JOIN Marks ON Marks.QueryId = Query.QueryId WHERE Marks.QueryId IS NULL;")
        # Catches any problems with the sql 
        except Exception as e: 
            print (e)

        # Stores the data retrieved by the cursor in a studentQueries array variable
        testQueriesData = c.fetchall()

        # Commit changes
        connection.commit()

        testQueryObjects = []
        # Converts each of the query records read from the database into an actual query object and stores them in an array
        for record in testQueriesData:
            query = Query(record[0], record[1], Query.makeExecutable(record[2]), record[5])
            testQueryObjects.append(query)
        
        # Returns the test query object array
        return testQueryObjects    
    
    # Function that identifies part of a string array based on single quotes (redundant method now following changes to the student file read in functionality)
    @staticmethod
    def identify(line):
        count = 0
        start = None
        end = None

        for char in line:
            # Finds the start of the string
            if char=="'" and start == None:
                start = count + 1
            # Finds the end of the string
            if char=="'" and start != None:
                end = count
            count += 1
        # Returns the string given its start and end index 
        return line[start:end]

    # Static function that alters the sql of a query object so that its storable in the database (single quotes break storing data in the database. To curve this a second single quote needs to be added next to them)
    @staticmethod
    def makeStorable(string):
        index = 0
        lastLocation = 0
        returnString = ""
        for char in string:
            # Looks for single quotes
            if char=="'":
                # Adds a second single quote to the found single quote
                returnString += string[lastLocation:index+1] + "'"
                lastLocation = index+1
            index+=1
        returnString += string[lastLocation:len(string)]
        # Returns the new string with all the additional single quotes
        return returnString

    # Static function that returns the sql query to an executable format after its been read back from the database (takes away all the instances of double single quotes, basically reverses the effects of the previous function)
    @staticmethod
    def makeExecutable(string):
        index = 0
        for char in string:
            if char=="'" and string[index+1] =="'":
                queryStringA = string[0:index]
                queryStringB = string[index+1:len(string)]
                string = queryStringA + queryStringB
            index+=1
        return string

    # Function that extracts 'n' number of student files from a zip folder and puts them in a temporary directory for reading into the system
    @staticmethod
    def extractFromZip(zipFilePath):
        # Opens the zip file in READ mode
        with ZipFile(zipFilePath, 'r') as zip:
            # Prints all the contents of the zip file
            zip.printdir()

            # Extracts all the student files and puts them in a Temporary Student File Directory for reading
            print('Extracting all the files now...')
            zip.extractall('Temporary Student File Directory')
            print('Done!')
    
    # Function that retrieves a Test Query object based off the selected assignment question (API functionality)
    @staticmethod
    def getTestQuery(connection, questionNumber):
        # Create cursor (basically what takes commands to the database and returns the data from it) 
        c = connection.cursor()

        # Try to query the database to retrieve the desired test query object 
        try:
            c.execute("SELECT qr.* FROM Query qr JOIN AssignmentQuestion asq ON qr.QuestionId=asq.QuestionId WHERE asq.QuestionNumber='" + questionNumber + "' AND qr.DataRetrieved IS NULL;")
        # Catches any problems with the sql 
        except Exception as e: 
            print (e)

        # Stores the data retrieved by the cursor in a testQueryData variable
        testQueryData = c.fetchall()

        # Commit changes
        connection.commit()

        # Converts the test query record read from the database into an actual query object 
        testQuery = Query(testQueryData[0][0], testQueryData[0][1], Query.makeExecutable(testQueryData[0][2]), testQueryData[0][5])
        
        # Returns the test query object
        return testQuery
    
    # Make student sql JSON serialisable for transport to the API
    @staticmethod
    def makeSerialisable(string):
        returnString = ""
        for char in string:
            if char == "/":
                returnString += "$"
            if char != "/":
                returnString += char
        return returnString

    # Return student sql back to executable format after inside the API
    @staticmethod
    def unSerialise(string):
        returnString = ""
        for char in string:
            if char == "$":
                returnString += "/"
            if char != "$":
                returnString += char
        return returnString

    # Static function that retrieves a specific test query based off a questionId
    @staticmethod
    def retrieveTestQueryFromQuestionId(questionId, connection):
        # Create cursor (basically what takes commands to the database and returns the data from it) 
        c = connection.cursor()

        # Try to query the database to retrieve the desired test query object 
        try:
            c.execute("SELECT Query.* FROM Query LEFT JOIN Marks ON Marks.QueryId = Query.QueryId WHERE Marks.QueryId IS NULL AND Query.QuestionId = '" + questionId + "';")
        # Catches any problems with the sql 
        except Exception as e: 
            print (e)

        # Stores the data retrieved by the cursor in a testQueryData variable
        testQueryData = c.fetchall()

        # Commit changes
        connection.commit()

        # Converts the test query record read from the database into an actual query object 
        testQuery = Query(testQueryData[0][0], testQueryData[0][1], Query.makeExecutable(testQueryData[0][2]), testQueryData[0][5])
        
        # Returns the test query object
        return testQuery

    # Static function that retrieves all the questions (numbers) that the student answered and their feedback for that question.
    @staticmethod
    def retrievedQuestionNumberAndFeedback(userId, connection):
        # Create cursor (basically what takes commands to the database and returns the data from it) 
        c = connection.cursor()

        # Try to query the database to identify the student's feedback for each question 
        try:
            c.execute("SELECT QuestionNumber, FeedBack FROM Query q JOIN AssignmentQuestion a ON q.QuestionId = a.QuestionId JOIN Marks m On m.QueryId = q.QueryId JOIN UserAccount u On u.UserId = m.UserId WHERE m.UserId = '" + userId + "';")
        # Catches any problems with the sql 
        except Exception as e: 
            print (e)

        # Stores the data retrieved by the cursor in a feedbackData array variable
        feedbackData = c.fetchall()

        # Commit changes
        connection.commit()

        return feedbackData

        
        


