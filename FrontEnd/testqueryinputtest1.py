from queryclass import Query
from deductionclass import Deduction
from questionclass import Question
from difficuiltyclass import Difficulty
from Marks import Marks
from databaseconnectionclass import DatabaseConnection
import pyodbc as po
    
# Example database connection objects
# Driver={ODBC Driver 17 for SQL Server};, Server=10.233.48.153\localhost,1433;, Database=;, UID=SA;, PWD=reallyStrongPwd123;
connection = DatabaseConnection('Driver={ODBC Driver 17 for SQL Server};', 'Server=10.233.17.48\localhost,1433;', 'Database=SQLCheckerV2;', 'UID=SA;', 'PWD=reallyStrongPwd123;')
advConnection = DatabaseConnection('Driver={ODBC Driver 17 for SQL Server};', 'Server=10.233.17.48\localhost,1433;', 'Database=AdventureWorks2019;', 'UID=SA;', 'PWD=reallyStrongPwd123;')

query = "SELECT * FROM Difficulty WHERE DiffLevel =　" + str(4) + ";"

# Attempts to connect to the database given the databaseConnection object
try:
    dbconnection = po.connect(connection.driver + connection.serverName + connection.databaseName + connection.serverUsername + connection.serverPassword)
# Catches any problems with the connection
except: 
    print ("There was an error establishing connection to the database. Check your database connection via the database connection page")
        
# Create cursor (basically what takes commands to the database and returns the data from it) 
c = dbconnection.cursor()

# Tries to query the database to retrieve the Id of the selected difficulty
try:
    c.execute(query)
# Catches any problems with the query
except Exception as e:
    print(e)
    print ("There was an error querying the database. Check your database connection via the database connection page")

# Stores the data retrieved by the cursor in a records variable
difficulty = c.fetchall()

# Commit changes
dbconnection.commit()

# Close database connection
dbconnection.close()

# Test query
queryString = "SELECT DISTINCT per.FirstName, per.LastName FROM Person.Person per inner join HumanResources.Employee e On e.BusinessEntityID = per.BusinessEntityID and per.FirstName IN (SELECT p.FirstName FROM Person.Person p Inner join Sales.Customer cus On Cus.PersonID = p.BusinessEntityID) AND per.LastName NOT IN(SELECT p.LastName FROM Person.Person p inner join Sales.Customer cus on cus.PersonID = p.BusinessEntityID)"
queryString2 = "SELECT ISNULL(pro.Color, 'N/A') AS Color, COUNT (Distinct pro.ProductID) AS Count_Of_Products FROM Production.Product pro GROUP BY pro.Color HAVING COUNT(Distinct pro.ProductID) >= 10 Order by Count_Of_Products desc"
# Function that fixes the issue with posting single quotes (in a sql query string) to the database for storage in the query table
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

storableQuery = makeStorable(queryString)

def makeExecutable(string):
    index = 0
    for char in string:
        if char=="'" and string[index+1] =="'":
            queryStringA = string[0:index]
            queryStringB = string[index+1:len(string)]
            string = queryStringA + queryStringB
        index+=1
    return string

executableQuery = makeExecutable(queryString)

# Example of a question object
theOriginalQuestionObject = Question("Find the First and Last Name of employees who have the same First name but different Last Name to that of customers (no duplicates)", difficulty[0][0])
theOriginalQuestionObject.storeQuestion(connection)
# Example of a query object
theOriginalQueryObject = Query(theOriginalQuestionObject.questionId, storableQuery, 10.0)
theOriginalQueryObject.storeQuery(connection)

# Now that the query string of the query object has been stored it needs to be converted back to its executable form
theOriginalQueryObject.sql = executableQuery

# Test to run the query object
theOriginalQueryObject.runQuery(advConnection)

# Test to compare the query object
theOriginalQueryObject.compareQuery(theOriginalQueryObject, advConnection)
#print(str(theOriginalQueryObject.timeToExecute))
#print(str(theOriginalQueryObject.score))
#print(theOriginalQueryObject.feedback)
#print(theOriginalQueryObject.comparisonCriteria)

storableData = makeStorable(str(theOriginalQueryObject.dataRetrieved))
theOriginalQueryObject.dataRetrieved = storableData
#print(str(theOriginalQueryObject.dataRetrieved))

# Test to update the query object in the database with results of the comparison
theOriginalQueryObject.updateQueryData(connection)

# Example of a marks object
#mark = Marks("689c8bca-a0c6-11eb-932f-d0817ac1bc5a", theOriginalQueryObject.queryId, theOriginalQueryObject.score)
#mark.storeMarks(mark)
# Example of a deduction object
#theOriginalDeductionObject = Deduction("38 charater question id", "Column Deduction", 2.0)
    

# c = po.connect(connection.driver + connection.serverName + connection.databaseName + connection.serverUsername + connection.serverPassword)
#cursor = c.cursor()
#print(theOriginalQueryObject.queryId)
#cursor.execute("""INSERT INTO Difficulty (DifficultyID, Level, Description) VALUES ('0f0e9e1e-9b48-11eb-b683-d0817ac1bc5a', '2', 'Please Work')""")
#cursor.execute("""SELECT * FROM Difficulty""")
#for record in cursor:
#    print(record)
#c.commit()
#c.close()

#theOriginalQueryObject.storeQuery(connection)

# Running the test query object to gather the expected data (columns, rows, order of columns/rows, values, time to execute etc.)
# theOriginalQueryObject.runQuery(advConnection)

# theOriginalQueryObject.compareQuery(theOriginalQueryObject, advConnection)
# print (theOriginalQueryObject.feedback)

# Test for deduction object
#theOriginalDeductionObject.applyDeduction(theOriginalQueryObject)
#print(theOriginalQueryObject.score)

# API
# TestQueries=["testquery1", "testquery2"]
# print ("Select Test Query...:" + TestQueries)
# chosenquery = the test query the student selected
# print ("copy and paste your attempt...")
# testquery1.compareQuery(studentquery)
# print (studentquery.feedback)