from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox
from questionclass import AssignmentQuestion
from Semester import Semester
from difficuiltyclass import Difficulty

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

# FoundQuestion class
class FoundQuestion:
    @staticmethod

    # Function to define which row is selected
    def selectAssignmentQuestion(rowNumber, rows, databaseconnection, tickBoxSelection):
        print(tickBoxSelection)
        # Code for adding a selected question as an Assignment Question in the database
        if (tickBoxSelection == 1):
            index = 0
            for row in rows:
                if index == rowNumber:
                    # Get the difficulty Id
                    difficuiltyId = Difficulty.getDifficultyId(
                        row[2], databaseconnection)
                    currentSemester = Semester.getCurrentSemester(
                        databaseconnection)
                    assignmentQuestion = AssignmentQuestion(
                        row[0], row[1], difficuiltyId, currentSemester.semesterId, AssignmentQuestion.generateAssignmentQuestionNumber(difficuiltyId, databaseconnection))
                    assignmentQuestion.storeAssignmentQuestion(
                        databaseconnection)

                index += 1
        # Code for removing an assignment question from the table in the database when it is deselected
        elif (tickBoxSelection == 0):
            index = 0
            for row in rows:
                if index == rowNumber:
                    AssignmentQuestion.destoreAssignmentQuestion(
                        row[0], databaseconnection)
                index += 1

    # Initialize function
    def __init__(self, input_canvas, content_of_row, main_controller, row_no, select_labelRows, databaseconnection):
        self.main_controller = main_controller
        self.package_canvas = tk.Canvas(input_canvas, width=1760, height=30)
        question_canvas = tk.Canvas(self.package_canvas)

        # Create canvas for each question
        # Question ID cell
        quesID_lab = tk.Label(
            question_canvas, text=content_of_row[0], bg="white", relief=RIDGE)
        quesID_lab.configure(anchor="c")
        quesID_lab.configure(font="-family {Segoe UI Historic} -size 10")
        quesID_lab.place(relx=0.2533, rely=0, relheight=1, relwidth=0.15)

        # Question cell
        ques_lab = tk.Label(
            question_canvas, text=content_of_row[1], bg="white", relief=RIDGE)
        ques_lab.configure(anchor="w")
        ques_lab.configure(font="-family {Segoe UI Historic} -size 10")
        ques_lab.place(relx=0.4033, rely=0, relheight=1, relwidth=0.33375)

        # Difficulty cell
        difficulty_lab = tk.Label(
            question_canvas, text=content_of_row[2], bg="white", relief=RIDGE)
        difficulty_lab.configure(anchor="c")
        difficulty_lab.configure(font="-family {Segoe UI Historic} -size 10")
        difficulty_lab.place(relx=0.73705, rely=0, relheight=1, relwidth=0.075)

        # Deduction cell
        deduction_button = tk.Button(question_canvas)
        deduction_button.configure(
            activebackground="black", activeforeground="white")
        deduction_button.configure(
            bg="white", foreground="black", pady="0", relief=RIDGE)
        deduction_button.configure(text='''Open deduction''')
        deduction_button.configure(
            command=lambda: self.main_controller.create_deduction_page(select_labelRows[row_no]))

        deduction_button.place(relx=0.81205, rely=0,
                               relheight=1, relwidth=0.1335)

        # Need this for classifying if not put this value in it will be the same
        # May carry some value for some purpore
        check_var1 = IntVar(self.package_canvas)

        # Tickbox for choosing student query
        var1 = tk.IntVar()
        tickbox_button = tk.Checkbutton(question_canvas, variable=check_var1)
        tickbox_button.configure(
            activebackground="black", relief=RIDGE, activeforeground="#000000", bg="white")
        tickbox_button.configure(variable=var1, onvalue=1, offvalue=0)
        tickbox_button.configure(command=lambda: self.selectAssignmentQuestion(
            row_no, select_labelRows, databaseconnection, var1.get()))
        tickbox_button.configure(onvalue=1, offvalue=0)
        tickbox_button.place(relx=0.94555, rely=0,
                             relheight=1, relwidth=0.0585)

        # Place the question canvas to the table
        question_canvas.place(relx=0, rely=0, relheight=1, relwidth=1)

    # Function to replace the question_canvas anytime we have a new row in the table
    def rePlace(self):
        self.package_canvas.pack()
