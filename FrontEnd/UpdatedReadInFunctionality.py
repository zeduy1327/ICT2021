from zipfile import ZipFile
from queryclass import Query
from databaseconnectionclass import DatabaseConnection
from queryclass import Query
from User import User
from Marks import Marks
from difficuiltyclass import Difficulty
from questionclass import Question 
from questionclass import AssignmentQuestion
from Semester import Semester

# Connection objects
connection = DatabaseConnection('Driver={ODBC Driver 17 for SQL Server};', 'Server=192.168.1.2\localhost,1433;', 'Database=SQLCheckerV2;', 'UID=SA;', 'PWD=reallyStrongPwd123;')
advConnection = DatabaseConnection('Driver={ODBC Driver 17 for SQL Server};', 'Server=192.168.1.2\localhost,1433;', 'Database=AdventureWorks2019;', 'UID=SA;', 'PWD=reallyStrongPwd123;')

# Established connections
establishedConnection = DatabaseConnection.getConnection(connection)
establishedAdvConnection = DatabaseConnection.getConnection(advConnection)

# Stores the 5 difficuilty Objects in the database (commented out because we dont more than one of each difficulty)
#difficulty001 = Difficulty(1, "Level 1 Difficulty")
#difficulty001.storeDifficulty(establishedConnection)
#difficulty002 = Difficulty(2, "Level 2 Difficulty")
#difficulty002.storeDifficulty(establishedConnection)
#difficulty003 = Difficulty(3, "Level 3 Difficulty")
#difficulty003.storeDifficulty(establishedConnection)
#difficulty004 = Difficulty(4, "Level 4 Difficulty")
#difficulty004.storeDifficulty(establishedConnection)
#difficulty005 = Difficulty(5, "Level 5 Difficulty")
#difficulty005.storeDifficulty(establishedConnection)

# Retrieves the approrpiate difficulty from the database 
#difficulty1 = Difficulty.getDifficultyId(1, establishedConnection)

# Creates two question objects and stores them in the database (commented out because we dont need more than one instance of the same question)
#Q1001 = Question(Question.makeStorable("Products come in various colours.  List the colours of the various products and the number of products for each of those colours if there are at least 10 items that came in that colour.  Where the colour is not specified, display N/A"), difficulty1)
#Q1001.storeQuestion(establishedConnection)
#Q1002 = Question(Question.makeStorable("Find the First and Last name as well as the bonus amount of all sales people who have a bonus greater than the average bonus of salespersons in Australia."), difficulty1)
#Q1002.storeQuestion(establishedConnection)

# Semester Object (commented out we only need one current semester)
#currentSemester = Semester(2, '2021', '20210228', '20210701', 'SP2-2021')
#currentSemester.storeSemester(establishedConnection)

# Constructs two test queries (one for each of the questions in the database commented out because we only need one of each)
#testQuery1 = Query("7caa0ac4-acb6-11eb-8ddc-d0817ac1bc5a", Query.makeStorable("SELECT ISNULL(pro.Color, 'N/A') AS Color, COUNT (Distinct pro.ProductID) AS Count_Of_Products FROM Production.Product pro GROUP BY pro.Color HAVING COUNT(Distinct pro.ProductID) >= 10 Order by Count_Of_Products desc"), 10.0)
#testQuery2 = Query("7cacbfbc-acb6-11eb-8ddc-d0817ac1bc5a", Query.makeStorable("SELECT DISTINCT per.FirstName, per.LastName FROM Person.Person per inner join HumanResources.Employee e On e.BusinessEntityID = per.BusinessEntityID and per.FirstName IN (SELECT p.FirstName FROM Person.Person p Inner join Sales.Customer cus On Cus.PersonID = p.BusinessEntityID) AND per.LastName NOT IN(SELECT p.LastName FROM Person.Person p inner join Sales.Customer cus on cus.PersonID = p.BusinessEntityID);"), 10.0)
#testQuery1.storeQuery(establishedConnection)
#testQuery2.storeQuery(establishedConnection)

# The teacher has selected the two test queries so we need to move the questions associated with these queries into the 
# assignment questions table in the database (commented because we only need to do it once).
#allQuestions = Question.readAllQuestions(establishedConnection)
#currentSem = Semester.getCurrentSemester(establishedConnection)
#index = 1
#for question in allQuestions:
#    assignmentQuestion = AssignmentQuestion(question.questionId, question.question, question.difficultyId, currentSem.semesterId, "Q100" + str(index))
#    index +=1
#    assignmentQuestion.storeAssignmentQuestion(establishedConnection)

# Extracts student files from a zip and put them in a temp directory for reading (commented out only need to do this once)
#StudentQueryZipFile = "/Users/chandleslovehandles/Documents/University 2021/ICT Capstone Project/Student File Read In Functionality (Updated)/SubmittedStudentQueries.zip"
#Query.extractFromZip(StudentQueryZipFile)
# Reads the student queries from the student files 
#Query.readIn("/Users/chandleslovehandles/Documents/University 2021/ICT Capstone Project/Week 8 GIT - Fixed/Project/Temp Student File Directory/SubmittedStudentQueries/Harry Chandler_blah_blah_chahf004_Q1002.sql", establishedConnection)

# Runs the comparison functionality on all the test queries/student queries and updates the student data and the marks data accordingly
#testQueries = Query.readAllTestQueries(establishedConnection)
#studentQueries = (Query.readAllStudentQueries(establishedConnection))
#Query.compareAll(testQueries, studentQueries, establishedConnection, establishedAdvConnection)

# Export to CSV file test
#Marks.exportToCSV('/Users/chandleslovehandles/Documents/University 2021/ICT Capstone Project/Week 8 GIT - Fixed/Project/FrontEnd/ExportedMarks.csv', establishedConnection) 

# Graph test
#students = User.getAllUsers(establishedConnection)

#student = students[0]
#print (student)

#Marks.graphAverageScore(establishedConnection)
#Marks.graphAllStudentsForQuestion(establishedConnection, "Q1001")
#Marks.graphAllMarksForStudent(establishedConnection, student)

# Read all questions for a difficulty test
questions = Question.readAllDifficultyQuestions(establishedConnection, "3438d0de-acb3-11eb-9e19-d0817ac1bc5a")
for question in questions:
    print (question.question)

