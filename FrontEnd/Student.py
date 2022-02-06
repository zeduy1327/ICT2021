import requests
from queryclass import Query

BASE = "http://127.0.0.1:5000/"

# Get response test
# Get request to retrieve the current assignment questions from the API
#getAssignmentQuestions = requests.get(BASE + "assignmentquestion")
# Displays the API's response to the student
#print(getAssignmentQuestions.json())


# Post response test
# Student sql attempt
string = "SELECT ISNULL(pro.Color, 'N/A') AS Color, COUNT (Distinct pro.ProductID) AS Count_Of_Products FROM Production.Product pro GROUP BY pro.Color HAVING COUNT(Distinct pro.ProductID) >= 10 Order by Count_Of_Products desc;"

# Converts the students sql into a format that is sendable
newString = Query.makeSerialisable(string)

# Post request to the API to compare the student query attempt with the chosen test query 
postAssignmentNumber = requests.post(BASE + "studentquery/Q1001/" + newString)

# Displays the feedback of the comparison back to the student 
print(postAssignmentNumber.json())