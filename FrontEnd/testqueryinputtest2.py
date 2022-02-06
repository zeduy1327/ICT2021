from tkinter import *
from queryclass import Query
from deductionclass import Deduction
from databaseconnectionclass import DatabaseConnection
from questionclass import Question
from difficuiltyclass import Difficulty
import pyodbc as po

root = Tk()

# Example database connection object
connection = DatabaseConnection('Driver={ODBC Driver 17 for SQL Server};', 'Server=10.233.17.48\localhost,1433;', 'Database=SQLCheckerV2;', 'UID=SA;', 'PWD=reallyStrongPwd123;')

# Stores the 5 difficuilty Objects in the (commented out because we dont more than one of each difficulty)
#difficulty001 = Difficulty(1, "Level 1 Difficulty")
#difficulty001.storeDifficulty(connection)
#difficulty002 = Difficulty(2, "Level 2 Difficulty")
#difficulty002.storeDifficulty(connection)
#difficulty003 = Difficulty(3, "Level 3 Difficulty")
#difficulty003.storeDifficulty(connection)
#difficulty004 = Difficulty(4, "Level 4 Difficulty")
#difficulty004.storeDifficulty(connection)
#difficulty005 = Difficulty(5, "Level 5 Difficulty")
#difficulty005.storeDifficulty(connection)

# Store Query function
def storeData(variable, databaseConnection):
    chosenDifficulty = variable
    charCount = 0
    for char in chosenDifficulty:
        if charCount == 2:
            diffLevel = char
        charCount += 1
    print (diffLevel)

    query = "SELECT * FROM Difficulty WHERE DiffLevel =　" + diffLevel + ";"

    # Attempts to connect to the database given the databaseConnection object
    try:
        connection = po.connect(databaseConnection.driver + databaseConnection.serverName + databaseConnection.databaseName + databaseConnection.serverUsername + databaseConnection.serverPassword)
    # Catches any problems with the connection
    except: 
        print ("There was an error establishing connection to the database. Check your database connection via the database connection page")
        
    # Create cursor (basically what takes commands to the database and returns the data from it) 
    c = connection.cursor()

    # Tries to query the database to retrieve the Id of the selected difficulty
    try:
        c.execute(query)
    # Catches any problems with the query
    except Exception as e:
        print(e)
        print ("There was an error querying the database. Check your database connection via the database connection page")

    # Stores the data retrieved by the cursor in a records variable
    difficulty = c.fetchall()

    print (difficulty)
    # Commit changes
    connection.commit()

    # Close database connection
    connection.close()

    # Define database connection object 
    connection = DatabaseConnection('Driver={ODBC Driver 17 for SQL Server};', 'Server=10.233.17.48\localhost,1433;', 'Database=SQLCheckerV2;', 'UID=SA;', 'PWD=reallyStrongPwd123;')

    # Testing all my functions
    question = Question(question_entry.get(), difficulty[0][0])
    
    question.storeQuestion(connection)

    query = Query(question.questionId, query_entry.get(), 10.0)

    query.storeQuery(connection)

# Represents the value of the difficuilty dropdown
DIFFICUILTY = [
            "001",
            "002",
            "003",
            "004",
            "005"
        ]

variable = StringVar(root)
# Default drowdown value
variable.set(DIFFICUILTY[0]) 

# GUI entry for the question string
question_entry = Entry(width=200, borderwidth=5, font=("Calibri", 15))
question_entry.pack()
question_entry.insert(0, "Enter The Test Query's Question Here")

# GUI entry for the sql query string 
query_entry = Entry(width=200, borderwidth=5, font=("Calibri", 15))
query_entry.pack()
query_entry.insert(0, "Enter The Test Query Here")

# GUI dropdown that allows the user to select the difficuilty of the query that they are inputting
difficulty_label = Label(root, text="Select the difficuilty of the test queries you wish to choose from: ", font=("Calibri", 15))
difficulty_label.pack(pady=5) 
difficulty_dropdown = OptionMenu(root, variable, *DIFFICUILTY)
difficulty_dropdown.pack(pady=5)

# Button for saving the test query
inputquery_button = Button(root, text="Save Query", font=("Calibri", 15), width=45, padx=20, pady=20, command = lambda: storeData(variable.get(), connection))
inputquery_button.pack()

root.mainloop()