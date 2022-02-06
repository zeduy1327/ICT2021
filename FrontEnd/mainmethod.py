# Import packages/classes
from questionclass import Question
from queryclass import Query
from deductionclass import Deduction
from difficuiltyclass import Difficulty
from databaseconnectionclass import DatabaseConnection
from tkinter import * 
from tkinter.scrolledtext import ScrolledText

# GUI root  
root = Tk()
root.title("Python BE SQL Checker")
root.config(background="#282728")
# Gathers the dimensions of the screen to adjust the application to varying screen sizes
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
# Sets the GUI's size to match the dimensions of the screen
root.geometry(str(screen_width) + "x" + str(screen_height))

def storeTestQuery():
    # Example database connection object
    connection = DatabaseConnection('Driver={ODBC Driver 17 for SQL Server};', 'Server=10.233.17.48\localhost,1433;', 'Database=SQLCheckerV2;', 'UID=SA;', 'PWD=reallyStrongPwd123;')

    # Gets the difficuiltyId (from the database) associated with the user's difficuilty selection on the dropdown
    difficultyId = Difficulty.getDifficultyId(variable.get()[2], connection)

    # Creates a question object from the user's input 
    question = Question(Question.makeStorable(question_entry.get("1.0",'end-1c')), difficultyId)

    # Stores the question in the database
    question.storeQuestion(connection)

    # Creates a query object from the user's input
    query = Query(question.questionId, Query.makeStorable(query_entry.get("1.0",'end-1c')), 10.0)

    # Stores the query in the database
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

# Frame
frame = Frame(root, width=screen_width, height=screen_height, bg="#C9C9C0")
frame.pack(fill=BOTH, padx=10, pady=10)

# GUI entry for the question string
question_entry = ScrolledText(frame, borderwidth=5, height=10, width=screen_width, font=("Calibri", 15))
question_entry.pack(padx=5, pady=5)
question_entry.insert(INSERT, "Copy and Paste the Test Query's Question Here:")

# GUI entry for the sql query string 
query_entry = ScrolledText(frame, borderwidth=5, height=10, width=screen_width, font=("Calibri", 15))
query_entry.pack(padx=5, pady=5)
query_entry.insert(INSERT, "Copy and Paste the Test Query's SQL Here")

# GUI dropdown that allows the user to select the difficuilty of the query that they are inputting
difficulty_label = Label(frame, text="Select the difficuilty of the test queries you wish to choose from: ", width=screen_width, font=("Calibri", 15))
difficulty_label.pack(padx=5, pady=5) 
difficulty_dropdown = OptionMenu(frame, variable, *DIFFICUILTY)
difficulty_dropdown.pack(fill=X, padx=5, pady=5)

# Button for saving the test query
inputquery_button = Button(frame, text="Save Query", font=("Calibri", 15), width=screen_width, height=10, command = storeTestQuery)
inputquery_button.pack(padx=10, pady=10)

root.mainloop()