from deductionclass import Deduction
from difficuiltyclass import Difficulty
from queryclass import Query
from databaseconnectionclass import DatabaseConnection

# Example database connection objects
connection = DatabaseConnection('Driver={ODBC Driver 17 for SQL Server};', 'Server=192.168.1.6\localhost,1433;', 'Database=SQLCheckerV2;', 'UID=SA;', 'PWD=reallyStrongPwd123;')

# Example test query object 
testQuery = Query("ed0674a2-a2ec-11eb-add9-d0817ac1bc5a", "62d3d4d6-a17b-11eb-8b3c-d0817ac1bc5a", "SELECT DISTINCT per.FirstName, per.LastName FROM Person.Person per inner join HumanResources.Employee e On e.BusinessEntityID = per.BusinessEntityID and per.FirstName IN (SELECT p.FirstName FROM Person.Person p Inner join Sales.Customer cus On Cus.PersonID = p.BusinessEntityID) AND per.LastName NOT IN(SELECT p.LastName FROM Person.Person p inner join Sales.Customer cus on cus.PersonID = p.BusinessEntityID)", 10.0)

Deduction.populateDeductions(testQuery, connection)
deductions = Deduction.readAllDeductions(testQuery, connection)

deduction = deductions[0]

deduction.changeDeductionValue(1.0)
deduction.updateDeductionData(connection)