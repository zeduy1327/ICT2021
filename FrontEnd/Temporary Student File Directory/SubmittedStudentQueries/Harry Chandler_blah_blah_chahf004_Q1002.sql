-- StudentId: chahf004
-- FullName: Harold Chandler
-- Question Number: Q1002
-- Question: Find the First and Last name as well as the bonus amount of all sales people who have a bonus greater 
-- than the average bonus of salespersons in Australia.

SELECT DISTINCT per.FirstName, per.LastName FROM Person.Person per inner join HumanResources.Employee e On e.BusinessEntityID = per.BusinessEntityID and per.FirstName IN (SELECT p.FirstName FROM Person.Person p Inner join Sales.Customer cus On Cus.PersonID = p.BusinessEntityID) AND per.LastName NOT IN(SELECT p.LastName FROM Person.Person p inner join Sales.Customer cus on cus.PersonID = p.BusinessEntityID);