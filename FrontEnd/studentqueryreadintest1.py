from deductionclass import Deduction
from queryclass import Query
from databaseconnectionclass import DatabaseConnection


# Example database connection objects
connection = DatabaseConnection('Driver={ODBC Driver 17 for SQL Server};', 'Server=192.168.1.6\localhost,1433;', 'Database=SQLCheckerV2;', 'UID=SA;', 'PWD=reallyStrongPwd123;')
advConnection = DatabaseConnection('Driver={ODBC Driver 17 for SQL Server};', 'Server=192.168.1.6\localhost,1433;', 'Database=AdventureWorks2019;', 'UID=SA;', 'PWD=reallyStrongPwd123;')

# Constructs two test queries (one for each of the questions in the database)
testQuery1 = Query("61aabf9c-a181-11eb-bc39-d0817ac1bc5a", Query.makeStorable("SELECT ISNULL(pro.Color, 'N/A') AS Color, COUNT (Distinct pro.ProductID) AS Count_Of_Products FROM Production.Product pro GROUP BY pro.Color HAVING COUNT(Distinct pro.ProductID) >= 10 Order by Count_Of_Products desc"), 10.0)
testQuery2 = Query("62d3d4d6-a17b-11eb-8b3c-d0817ac1bc5a", Query.makeStorable("SELECT DISTINCT per.FirstName, per.LastName FROM Person.Person per inner join HumanResources.Employee e On e.BusinessEntityID = per.BusinessEntityID and per.FirstName IN (SELECT p.FirstName FROM Person.Person p Inner join Sales.Customer cus On Cus.PersonID = p.BusinessEntityID) AND per.LastName NOT IN(SELECT p.LastName FROM Person.Person p inner join Sales.Customer cus on cus.PersonID = p.BusinessEntityID)"), 10.0)

# Stores the test queries in the database
testQuery1.storeQuery(connection)
testQuery2.storeQuery(connection)

# Reads in the student queries from a student file (they get stored in the database inside the readIn function)
Query.readIn("/Users/chandleslovehandles/Documents/University 2021/ICT Capstone Project/Student vs. Test Query Comparison/Comparison Functionality/chahf004.sql.txt", connection)

# Reads in all the student queries/test queries from the database into local query objects
studentQueries = Query.readAllStudentQueries(connection)
testQueries = Query.readAllTestQueries(connection)

# Populates each test query with deduction objects
#for testQuery in testQueries:
    #Deduction.populateDeductions(testQuery, connection)

# Compares all the student queries with their associated test query
#Query.compareAll(testQueries, studentQueries, connection, advConnection)