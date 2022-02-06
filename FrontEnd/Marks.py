

import pyodbc
from tkinter import messagebox
import uuid
import csv
import numpy
import matplotlib.pyplot as plt
from difficuiltyclass import Difficulty
from questionclass import Question
from User import User
from databaseconnectionclass import DatabaseConnection
from questionclass import AssignmentQuestion


import random
import string

#Constructor
class Marks(object):
    """description of class"""
    def __init__(self,*args):
        #Constructor for creating Marks instance in program
        #Takes UserId, QueryId and Marks As Argurment
        # Generate a UUID for marksId
        if(len(args)==3):
            self.marksId=str(uuid.uuid1())
            self.userId=args[0]
            self.queryId=args[1]
            self.marks=args[2]
        #Constructor for creating Marks instance from data imported from database
        # Takes MarksId, UserId, QueryId & Marks as Arguement
        elif(len(args)==4):
            self.marksId=args[0]
            self.userId=args[1]
            self.queryId=args[2]
            self.marks=args[3]

    '''
     Function to retrieve all the marks from the database that have the given usedId
     Takes databaseConnection object and userId as Arguements
     Returns all the marks for the given User
     '''
    @staticmethod
    def getMarksForUserId(databaseConnection, userId):
        # Query to retreive all the marks that are related to the given UserId
        query="select * from dbo.Marks m where m.UserId='"+userId+"';"
        
        # Establishes a cursor (essentially what takes the data to and from the database) 
        cursor=databaseConnection.cursor()
        
        # Attempt to query the database
        try:
            cursor.execute(query)
        # Catches any errors querying the database
        except Exception as e:
            print(e)

        # Stores the data retrieved by the cursor in a marksData array variable
        marksData = cursor.fetchall()

        marksObjects = []
        # Converts each of the marks records read from the database into an actual marks object and stores them in an array
        for record in marksData:
            mark = Marks(record[0], record[1], record[2], record[3])
            marksObjects.append(mark)

        # Returns the marks object array
        return marksObjects

    '''
    Function to all the marks for any question
    Takes Database connection and question as arguement
    Returns all the marks recieved for the question
    '''
    @staticmethod
    def getMarksForQuestionId(connection, questionId):
        # Establishes a cursor (essentially what takes data to and from the database)
        cursor=connection.cursor()
        
        # Query to retrieve all marks for the given questionId
        query="select * from dbo.Marks m join dbo.Query qr on m.QueryId=qr.QueryId where qr.QuestionId='"+questionId+"'"
        
        # Attempt to run the query
        try:
            cursor.execute(query)
        # Catch exception
        except Exception as e:
            print(e)
        
        # Stores the data retrieved by the cursor in a marksData array variable
        marksData = cursor.fetchall()
        
        # Commit changes
        connection.commit()

        marksObjects = []
        # Converts each of the marks records read from the database into an actual marks object and stores them in an array
        for record in marksData:
            mark = Marks(record[0], record[1], record[2], record[3])
            marksObjects.append(mark)

        # Returns the marks object array
        return marksObjects


    @staticmethod
    def marksWithQNumForUser(connection,userId):

        cursor=connection.cursor()

        query="select m.*, asq.QuestionNumber from Marks m join Query q on m.QueryId=q.QueryId join AssignmentQuestion asq on q.QuestionId=asq.QuestionId where m.userId='"+userId+"'"

        try:
            cursor.execute(query)
        except Exception as e:
            print(e)
        
        retrievedData=cursor.fetchall()

        return retrievedData



    '''
    Function to store a marks record in the database
    Takes a database connection object and marks object as arguement
    '''
    def storeMarks(self, connection):
        
        # Create cursor (basically what takes commands to the database and returns the data from it)
        cursor=connection.cursor()
        # Query to insert marks record into the marks table
        query="insert into dbo.Marks (MarkId, UserId,QueryId, Marks) values ('"+self.marksId+"','"+self.userId+"','"+self.queryId+"','"+str(self.marks)+"')"
        #Attempt to execute the query
        try:
            cursor.execute(query)
        #Catch Exception
        except Exception as e:
            print(e)
        #Commit changes to the database
        connection.commit()
 
    '''
    Function to uptade the marks for a given query in the database
    Takes Database connection object and Query object as arguement
    '''
    @staticmethod
    def updateMarksData(connection, query):
        # Create cursor (basically what takes commands to the database and returns the data from it)
        cursor=connection.cursor()
        
        # query that updates the marks attribute in the Marks table for
        # a record with the matching query id (follows the comparison functionality)
        query="update Marks set Marks= '" + str(query.score) + "' where QueryId='" + query.queryId + "';"
        #Attemt to execute the query
        try:
            cursor.execute(query)
        #catch any exception
        except Exception as e:
            print(e)
        #commit the change made to the table
        cursor.commit()

    '''
    Function that returns all the marks data that is stored in the Marks Table in the database
    Takes Database Connection as Parameter
    Retruns an array of all the marks object stored in the database
    '''
    @staticmethod
    def readAllMarks(connection):
        # Create cursor (basically what takes commands to the database and returns the data from it) 
        c = connection.cursor()

        # Try to query the database to identify all the marks 
        try:
            c.execute("SELECT * FROM Marks")
        # Catches any problems with querying the database
        except Exception as e: 
            print (e)
        # Stores the data retrieved by the cursor in a marks data array variable
        marksData = c.fetchall()
        # Commit changes
        connection.commit()

        marksObjects = []
        # Converts each of the marks records read from the database into an actual marks object and stores them in an array
        for record in marksData:
            mark = Marks(record[0], record[1], record[2], record[3])
            marksObjects.append(mark)

        # Returns the marks object array
        return marksObjects


    @staticmethod
    def getMarksForQuestionNumberForUser(connection, userId, questionNumber):
         # Create cursor (basically what takes commands to the database and returns the data from it) 
        c = connection.cursor()

        query="SELECT AssignmentQuestion.QuestionNumber FROM AssignmentQuestion JOIN Query ON Query.QuestionId = AssignmentQuestion.QuestionId JOIN Marks ON Marks.QueryId = Query.QueryId WHERE QuestionNumber = '"+ questionNumber+ "' AND Marks.UserId ='"+userId+"'"
        # Try to query the database to identify all the marks 
        try:
            c.execute(query)
        # Catches any problems with querying the database
        except Exception as e: 
            print (e)

        for row in c:
            return row[0]
    
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

    '''
    Function that gathers the students, their marks and the assignment questions and exports them appropriately to a 
    csv file.
    '''
    @staticmethod
    def exportToCSV(filepath, connection):
        # Gathers all the students in an array
        students  = User.getAllUsers(connection)
        # Gathers all the assignment questions in an array
        questions = AssignmentQuestion.getAllAssignmentQuestions(connection)

        

        with open(filepath, mode='w') as csv_file:
            fieldnames = ['Username']
            
            # Adds each question to the fieldnames (essentially makes a column for each assignment question)
            
            for question in questions:
                fieldnames.append(str(question.questionNumber))
                fieldnames.append("Feedback: " + question.questionNumber)
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            # Goes through each student gathers their mark for each question and writes it to the csv using a personalised dictionary of their marks
            index = 0 
            for student in students:
                # Holds a dictionary of key value pairs with each user's marks for all the questions
                userMarksDictionary = {"Username": student.UserName}
                # Gets all the students marks from the databse
                userMarks = Marks.marksWithQNumForUser(connection, student.UserId)

                userFeedBacks=Marks.retrievedQuestionNumberAndFeedback(student.UserId,connection)
               
                for mark in userMarks:
                    # print(str(index)+ " "+mark[4])
                    print(mark[4])
                    for question in questions:
                        if (str(question.questionNumber)==mark[4]):
                            for feedback in userFeedBacks:
                                if(str(question.questionNumber)==feedback[0]):
                                    userMarksDictionary[str(question.questionNumber)] = mark[3]
                                    userMarksDictionary[str("Feedback: " + question.questionNumber)] = feedback[1]
                                    print(userMarksDictionary)
                                    index+=1
                writer.writerow(userMarksDictionary) 
        messagebox.showinfo(title='Success', message='Marks Successfully exported to '+filepath+'.')


                    # if (str(questions[index].questionNumber)==mark[4]):
                    #     userMarksDictionary[str(questions[index].questionNumber)] = userMarks[index].marks
                    #     print(userMarksDictionary)
                    #     index+=1
                
    

    @staticmethod
    def generateRandom():
        students = [None]*100
        scores = [None]*100

        index = 0
        for student in students:
            # printing lowercase
            letters = string.ascii_lowercase
            studentname = ''.join(random.choice(letters) for i in range(5))
            studentnumber = random.randint(100, 999)
            students[index] = studentname + str(studentnumber)
            scores[index] = random.randint(0, 10)
            index+=1


        index = 0
        for student in students:
            print(students[index] + ": " + str(scores[index]))
            index += 1
        
        scoreCount={}
        for score in scores:
            count=0
            if ((score in scoreCount)==False):
                for eachScore in scores:
                    if(eachScore==score):
                        count=count+1
                    scoreCount[score]=count
        return scoreCount


    '''
    Function that gathers all the assignment questions from the database and graphs the average score acheived for each.
    '''
    @staticmethod
    def graphAverageScore(connection):
        # Gathers all the assignment questions from the database in an array 
        questions = AssignmentQuestion.getAllAssignmentQuestions(connection)
        # Holds the assignment question numbers that go along the x axis of the graph
        x = []
        # Holds an array of the average scores for each assignment questions (the y axis)
        y = []
        # Holds all the marks associated with assignment question 'n'
        associatedMarks = []
        # Creates the X axis and the Y axis for the graph 
        for question in questions:
            associatedMarks = Marks.getMarksForQuestionId(connection, question.questionId)
            totalMarks = 0
            for mark in associatedMarks:
                totalMarks += mark.marks
            y.append(totalMarks/len(associatedMarks))
            x.append(question.questionNumber)
        
        # Plots the average score of each question next to the assignment question itself
        plt.title("Average Marks For all Questions")
        plt.xlabel('Assignment Question Number')
        plt.ylabel('Average Score')
        plt.ylim([-1,11])
        
        plt.plot(x,y,marker='o', markerfacecolor='blue', markersize=12)
        # Shows the plot to the user
        plt.show()

    'Function that graphs all the marks recieved by students for a particular question'
    @staticmethod
    def graphAllStudentsForQuestion(connection,questionNumber):
        # Retrieves the assignment question chosen by the teacher 
        question=AssignmentQuestion.getAssignmentQuestionRecord(questionNumber,connection)
        # Retrieves all thr marks associated with that assignment question
        marks=Marks.getMarksForQuestionId(connection,question.questionId)
        
            
        #scoreCount= Marks.generateRandom()
        x = []
        y=[]
        

        # Creates the graph's x and y values
        for mark in marks:
            x.append(User.getUserNameFromId(connection, mark.userId))
            y.append(mark.marks)
        
        # Plots the graph's x and y values
        plt.xlabel('Student Username')
        plt.ylabel('Student Mark')
        plt.ylim([-1, 11])
        plt.xticks([])
        plt.title("Marks for : "+questionNumber)
        plt.scatter(x,y, label="Stars" , marker="*" , color="green")
        #plt.bar(scoreCount.keys(),scoreCount.values())
        # Shows the plot to the user
        plt.show()
    
    @staticmethod
    def graphAllMarksForStudent(connection,userName):
        #Retrive all assignment questions
        questions=AssignmentQuestion.getAllAssignmentQuestions(connection)
        
        #
        userId= User.getIdFromUserName(connection, userName)

        #Retrieve all marks associated with the Student
        marks=Marks.marksWithQNumForUser(connection,userId)
        
        x=[]
        y=[]

        for question in questions:
            x.append(question.questionNumber)
            for mark in marks:
                if (str(mark[4])==question.questionNumber):
                    y.append(mark[3])

        # Plots the graph's x and y values
        plt.title("Marks for User: "+ userName)
        plt.xlabel("Assignment Question Number")
        plt.ylabel('Student Mark')
        plt.ylim([-1,11])
        

        plt.plot(x,y, marker='o',markerfacecolor='blue' ,markersize=12)
        
        plt.show()


if __name__=='__main__':
    connection = DatabaseConnection('Driver={SQL Server};', 'Server=DESKTOP-NFLVEPF;', 'Database=SQLCheckerV2;','Trusted_Connection=yes;')
    dbConnection=DatabaseConnection.getConnection(connection,"Apple")
    '''
    testMarks=Marks('55a1614a-aaff-11eb-92f1-00155dd652d9','3272ddcc-ab08-11eb-98ff-00155dd652d9',10)
    testMarks2=Marks('55a1614a-aaff-11eb-92f1-00155dd652d9','e36f851d-a0df-11eb-b6a2-00155dca3af8',8)
    testMarks3=Marks('8554e788-ab08-11eb-87b3-00155dd652d9','3272ddcc-ab08-11eb-98ff-00155dd652d9',5)
    testMarks4=Marks('8554e788-ab08-11eb-87b3-00155dd652d9','e36f851d-a0df-11eb-b6a2-00155dca3af8',7)
    testMarks3.storeMarks(dbConnection)
    testMarks4.storeMarks(dbConnection)
    '''
    #Marks.getMarksForUser(connection,"TestUserName1")
    #allMarks=Marks.readAllMarks(connection)
    #for marks in allMarks:
    #    print(str(marks.marks))
    #marks=Marks.getMarksForUser(dbConnection,"TestUserName1")
    #marks=Marks.getMarksForQuestion(dbConnection,"Products come in various colours.  List the colours of the various products and the number of products for each of those colours if there are at least 10 items that came in that colour.  Where the colour is not specified, display N/A")
   # print(marks)
   
    Marks.graphAllStudentsForQuestion(dbConnection, "Q1005")

    #Marks.graphAverageScore(dbConnection)

    #Marks.exportToCSV("./FrontEnd/exportedMarks.csv",dbConnection)
    #print(Marks.getMarksForUserId(dbConnection,"4b72f137-b95a-11eb-8d98-00155d0a2966"))

    #print(Marks.marksWithQNumForUser(dbConnection,"4b805eb7-b95a-11eb-a7da-00155d0a2966"))
    #Marks.graphAllMarksForStudent(dbConnection,"STEAN006")

