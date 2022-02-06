from questionclass import AssignmentQuestion
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox, ttk
from tkinter.filedialog import asksaveasfile
from databaseconnectionclass import DatabaseConnection
from Semester import Semester
from queryclass import Query
from tkinter import filedialog
from User import User
from Marks import Marks
from difficuiltyclass import Difficulty
from questionclass import Question
from deductionclass import Deduction
import os


try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

from FoundQuestion import FoundQuestion

# Function to start GUI


def vp_start_gui():
    global val, w, root

    # Create root for the GUI
    root = tk.Tk()

    # Create top as a new main_menu object
    top = main_menu(root)
    root.mainloop()


w = None

# Function to create the Main menu


def create_main_menu(rt, *args, **kwargs):

    global w, w_win, root

    # Create root for main menu
    root = rt

    # Create the widget on top of main menu
    w = tk.Toplevel(root)

    # Pack the widget
    w.pack()

    # Put the top to the left side of main menu
    top.pack(side=LEFT, fill=BOTH)
    return (w, top)

# Terminate the GUI


def destroy_main_menu():
    global w
    w.destroy()
    w = None


# main class
class main_menu:
    x = 0
    # Connections
    # SQLCheckerConnection=None
    # AssignmentDataConnection=None

    def __init__(self, top=None):

        self.num_of_row = 0
        # Create and configure the top
        self.top = top
        # Gathers the dimensions of the screen to adjust the application to varying screen sizes
        screen_width = top.winfo_screenwidth()
        screen_height = top.winfo_screenheight()
        # Sets the GUI's size to match the dimensions of the screen
        self.top.geometry(str(screen_width) + "x" + str(screen_height))
        self.top.state('zoomed')

        self.top.minsize(120, 1)
        self.top.maxsize(1920, 1080)
        self.top.resizable(1, 1)
        self.top.title("Python BE SQL Checker")
        self.top.configure(background="#ffffff")

        # Create the main frame for the window GUI
        self.main_frame = Frame(self.top)
        self.main_frame.pack(expand=True, fill=BOTH)

        # Create the main canvas for holding everything inside GUI
        self.main_canvas = Canvas(self.main_frame)
        self.main_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        # Create a list for storing the label of questions control
        self.list_label_ques = []

        # Create the header label
        self.header_label = tk.Label(self.main_canvas, bg="white")
        self.header_label.place(
            relx=0.0, rely=0.0, relheight=0.3, relwidth=1.0)

        # Create the canvas at the top of GUI (inside header label)
        self.header = tk.Canvas(self.header_label)
        self.header.place(relx=0.0, rely=0.0, relheight=0.75, relwidth=1.0)
        self.header.configure(background="white")
        self.header.configure(borderwidth="2")
        self.header.configure(insertbackground="black")
        self.header.configure(selectbackground="blue")
        self.header.configure(selectforeground="white")

        # Create the logo for the product
        self.header_picture_photo = PhotoImage(file="Pictures/Logo.png")
        self.header_picture_photoImage = self.header_picture_photo.subsample(
            1, 1)
        self.header_picture = tk.Label(
            self.header, image=self.header_picture_photoImage)
        self.header_picture.place(
            relx=0.007, rely=0.02, relheight=0.96, relwidth=0.112)
        self.header_picture.configure(background="white")
        self.header_picture.configure(foreground="white")

        # Create the header text for the product's name
        self.header_text = tk.Label(self.header)
        self.header_text.place(relx=0.127, rely=0.019,
                               relheight=0.962, relwidth=0.87)
        self.header_text.configure(background="#0052A0")
        self.header_text.configure(anchor="c")
        self.header_text.configure(font="-family {Terminal} -size 60")
        self.header_text.configure(foreground="white")
        self.header_text.configure(text='''Python BE SQL Checker''')

        # Create navigation bar (inside header label) - Main menu button
        self.main_menu_nav_button = tk.Button(self.header_label)
        self.main_menu_nav_button.place(
            relx=0.0425, rely=0.8, relheight=0.145, relwidth=0.145)
        self.main_menu_nav_button.configure(activebackground="#0052A0")
        self.main_menu_nav_button.configure(activeforeground="white")
        self.main_menu_nav_button.configure(activeforeground="#000000")
        self.main_menu_nav_button.configure(background="#A4CAED")
        self.main_menu_nav_button.configure(cursor="fleur")
        self.main_menu_nav_button.configure(foreground="#000000")
        self.main_menu_nav_button.configure(highlightcolor="black")
        self.main_menu_nav_button.configure(pady="0")
        self.main_menu_nav_button.configure(text='''Main Menu''')
        self.main_menu_nav_button.configure(
            font="-family {Segoe UI Historic} -size 12 -weight bold")
        self.main_menu_nav_button.configure(command=self.turn_on_main_menu)

        # Assignment Questions button in navigation bar
        self.test_query_nav_button = tk.Button(self.header_label)
        self.test_query_nav_button.place(
            relx=0.188, rely=0.8, relheight=0.145, relwidth=0.223)
        self.test_query_nav_button.configure(activebackground="#0052A0")
        self.test_query_nav_button.configure(activeforeground="white")
        self.test_query_nav_button.configure(activeforeground="#000000")
        self.test_query_nav_button.configure(background="#A4CAED")
        self.test_query_nav_button.configure(foreground="#000000")
        self.test_query_nav_button.configure(highlightcolor="black")
        self.test_query_nav_button.configure(pady="0")
        self.test_query_nav_button.configure(text='''Assignment Questions''')
        self.test_query_nav_button.configure(
            font="-family {Segoe UI Historic} -size 12 -weight bold")
        self.test_query_nav_button.configure(
            command=self.turn_on_test_query_menu)

        # Student Query button in navigation bar
        self.student_query_nav_button = tk.Button(self.header_label)
        self.student_query_nav_button.place(
            relx=0.411, rely=0.8, relheight=0.145, relwidth=0.173)
        self.student_query_nav_button.configure(activebackground="#0052A0")
        self.student_query_nav_button.configure(activeforeground="white")
        self.student_query_nav_button.configure(activeforeground="#000000")
        self.student_query_nav_button.configure(background="#A4CAED")
        self.student_query_nav_button.configure(foreground="#000000")
        self.student_query_nav_button.configure(highlightcolor="black")
        self.student_query_nav_button.configure(pady="0")
        self.student_query_nav_button.configure(text='''Student Query''')
        self.student_query_nav_button.configure(
            font="-family {Segoe UI Historic} -size 12 -weight bold")
        self.student_query_nav_button.configure(
            command=self.turn_on_student_query_menu)

        # Student vs. Test Query button in navigation bar
        self.student_vs_test_query_nav_button = tk.Button(self.header_label)
        self.student_vs_test_query_nav_button.place(
            relx=0.584, rely=0.8, relheight=0.145, relwidth=0.225)
        self.student_vs_test_query_nav_button.configure(
            activebackground="#0052A0")
        self.student_vs_test_query_nav_button.configure(
            activeforeground="white")
        self.student_vs_test_query_nav_button.configure(
            activeforeground="#000000")
        self.student_vs_test_query_nav_button.configure(background="#A4CAED")
        self.student_vs_test_query_nav_button.configure(cursor="fleur")
        self.student_vs_test_query_nav_button.configure(foreground="#000000")
        self.student_vs_test_query_nav_button.configure(highlightcolor="black")
        self.student_vs_test_query_nav_button.configure(pady="0")
        self.student_vs_test_query_nav_button.configure(
            text='''Student vs. Test Query''')
        self.student_vs_test_query_nav_button.configure(
            font="-family {Segoe UI Historic} -size 12 -weight bold")
        self.student_vs_test_query_nav_button.configure(
            command=self.turn_on_SVT_query_menu)

        # Setting button in navigation bar
        self.database_nav_button = tk.Button(self.header_label)
        self.database_nav_button.place(
            relx=0.809, rely=0.8, relheight=0.145, relwidth=0.149)
        self.database_nav_button.configure(activebackground="#0052A0")
        self.database_nav_button.configure(activeforeground="white")
        self.database_nav_button.configure(activeforeground="#000000")
        self.database_nav_button.configure(background="#A4CAED")
        self.database_nav_button.configure(foreground="#000000")
        self.database_nav_button.configure(highlightcolor="black")
        self.database_nav_button.configure(pady="0")
        self.database_nav_button.configure(text='''Settings''')
        self.database_nav_button.configure(
            font="-family {Segoe UI Historic} -size 12 -weight bold")
        self.database_nav_button.configure(command=self.turn_on_database)

        # Create the label for main menu
        self.main_menu_label = tk.Label(self.main_canvas, bg="white")
        self.main_menu_label.place(relx=0.0, rely=0.3, relheight=1, relwidth=1)

        # Create Assignment Questions button in main menu
        self.test_query_button_photo = PhotoImage(
            file="Pictures/QueryManagement.png")
        self.test_query_button_photoImage = self.test_query_button_photo.subsample(
            1, 1)
        self.test_query_button = tk.Button(
            self.main_menu_label, image=self.test_query_button_photoImage, compound=BOTTOM)
        self.test_query_button.place(
            relx=0.043, rely=0.05, relheight=0.263, relwidth=0.4)
        self.test_query_button.configure(activebackground="#A4CAED")
        self.test_query_button.configure(activeforeground="white")
        self.test_query_button.configure(activeforeground="#000000")
        self.test_query_button.configure(anchor='n')
        self.test_query_button.configure(background="#A4CAED")
        self.test_query_button.configure(
            font="-family {Segoe UI Historic} -size 18 -weight bold -underline 1")
        self.test_query_button.configure(foreground="#000000")
        self.test_query_button.configure(highlightcolor="black")
        self.test_query_button.configure(pady="0")
        self.test_query_button.configure(text='''Questions Management''')
        self.test_query_button.configure(command=self.turn_on_test_query_menu)

        # Create Student Query button in main menu
        self.student_query_button_photo = PhotoImage(
            file=r"Pictures/StudentQuery.png")
        self.student_query_button_photoImage = self.student_query_button_photo.subsample(
            1, 1)
        self.student_query_button = tk.Button(
            self.main_menu_label, image=self.student_query_button_photoImage, compound=BOTTOM)
        self.student_query_button.place(
            relx=0.56, rely=0.05, relheight=0.263, relwidth=0.4)
        self.student_query_button.configure(activebackground="#A4CAED")
        self.student_query_button.configure(activeforeground="white")
        self.student_query_button.configure(activeforeground="#000000")
        self.student_query_button.configure(anchor='n')
        self.student_query_button.configure(background="#A4CAED")
        self.student_query_button.configure(
            font="-family {Segoe UI Historic} -size 18 -weight bold -underline 1")
        self.student_query_button.configure(foreground="#000000")
        self.student_query_button.configure(highlightcolor="black")
        self.student_query_button.configure(pady="0")
        self.student_query_button.configure(text='''Student Query''')
        self.student_query_button.configure(
            command=self.turn_on_student_query_menu)

        # Create Student vs. Test Query button in main menu
        self.student_vs_test_query_button_photo = PhotoImage(
            file=r"Pictures/Marking.png")
        self.student_vs_test_query_button_photoImage = self.student_vs_test_query_button_photo.subsample(
            1, 1)
        self.student_vs_test_query_button = tk.Button(
            self.main_menu_label, image=self.student_vs_test_query_button_photoImage, compound=BOTTOM)
        self.student_vs_test_query_button.place(
            relx=0.043, rely=0.38, relheight=0.263, relwidth=0.4)
        self.student_vs_test_query_button.configure(activebackground="#A4CAED")
        self.student_vs_test_query_button.configure(activeforeground="white")
        self.student_vs_test_query_button.configure(activeforeground="#000000")
        self.student_vs_test_query_button.configure(anchor='n')
        self.student_vs_test_query_button.configure(background="#A4CAED")
        self.student_vs_test_query_button.configure(
            font="-family {Segoe UI Historic} -size 18 -weight bold -underline 1")
        self.student_vs_test_query_button.configure(foreground="#000000")
        self.student_vs_test_query_button.configure(highlightcolor="black")
        self.student_vs_test_query_button.configure(pady="0")
        self.student_vs_test_query_button.configure(
            text='''Student vs. Test Query''')
        self.student_vs_test_query_button.configure(
            command=self.turn_on_SVT_query_menu)

        # Create Settings button in main menu
        self.database_button_photo = PhotoImage(file=r"Pictures/Setting.png")
        self.database_button_photoImage = self.database_button_photo.subsample(
            1, 1)
        self.database_button = tk.Button(
            self.main_menu_label, image=self.database_button_photoImage, compound=BOTTOM)
        self.database_button.place(
            relx=0.56, rely=0.38, relheight=0.263, relwidth=0.4)
        self.database_button.configure(activebackground="#A4CAED")
        self.database_button.configure(activeforeground="white")
        self.database_button.configure(activeforeground="#000000")
        self.database_button.configure(anchor='n')
        self.database_button.configure(background="#A4CAED")
        self.database_button.configure(
            font="-family {Segoe UI Historic} -size 18 -weight bold -underline 1")
        self.database_button.configure(foreground="#000000")
        self.database_button.configure(highlightcolor="black")
        self.database_button.configure(pady="0")
        self.database_button.configure(text='''Settings''')
        self.database_button.configure(command=self.turn_on_database)

        # Create label for Assignment Questions Management
        self.test_query_management_label = tk.Label(
            self.main_canvas, bg="white")
        self.test_query_management_label.place(
            relx=0.0, rely=0.3, relheight=1, relwidth=1)
        self.test_query_management_label.place_forget()

        # Create Input Questions/Test Queries button in Assignment Questions Management
        self.input_photo = PhotoImage(file=r"Pictures/Input.png")
        self.input_photoImage = self.input_photo.subsample(1, 1)
        self.input_test_query_button = tk.Button(
            self.test_query_management_label, image=self.input_photoImage, compound=BOTTOM)
        self.input_test_query_button.place(
            relx=0.04, rely=0.085, relheight=0.5, relwidth=0.42)
        self.input_test_query_button.configure(activebackground="#A4CAED")
        self.input_test_query_button.configure(activeforeground="white")
        self.input_test_query_button.configure(activeforeground="#000000")
        self.input_test_query_button.configure(anchor='n')
        self.input_test_query_button.configure(background="#A4CAED")
        self.input_test_query_button.configure(
            font="-family {Segoe UI Historic} -size 18 -weight bold -underline 1")
        self.input_test_query_button.configure(foreground="#000000")
        self.input_test_query_button.configure(highlightcolor="black")
        self.input_test_query_button.configure(pady="0")
        self.input_test_query_button.configure(
            text='''Input Questions/Test Queries''')
        self.input_test_query_button.configure(
            command=self.turn_on_input_query)

        # Create Select Assignment Questions button in Assignment Questions Management
        self.select_photo = PhotoImage(file=r"Pictures/Select.png")
        self.select_photoImage = self.select_photo.subsample(1, 1)
        self.select_test_query_button = tk.Button(
            self.test_query_management_label, image=self.select_photoImage, compound=BOTTOM)
        self.select_test_query_button.place(
            relx=0.54, rely=0.085, relheight=0.5, relwidth=0.42)
        self.select_test_query_button.configure(activebackground="#A4CAED")
        self.select_test_query_button.configure(activeforeground="white")
        self.select_test_query_button.configure(activeforeground="#000000")
        self.select_test_query_button.configure(anchor='n')
        self.select_test_query_button.configure(background="#A4CAED")
        self.select_test_query_button.configure(
            font="-family {Segoe UI Historic} -size 18 -weight bold -underline 1")
        self.select_test_query_button.configure(foreground="#000000")
        self.select_test_query_button.configure(highlightcolor="black")
        self.select_test_query_button.configure(pady="0")
        self.select_test_query_button.configure(
            text='''Select Assignment Questions''')
        self.select_test_query_button.configure(
            command=self.turn_on_select_query)

        # Create canvas for Input Questions/Test Queries functionality
        self.input_canvas = tk.Canvas(self.main_canvas)
        self.input_canvas.configure(background="white")
        self.input_canvas.place_forget()

        # Canvas for containing all questions queries canvas inside
        self.canvas_query = tk.Canvas(self.input_canvas, bg="white")
        self.canvas_query.place(relx=0.043, rely=0.08,
                                relheight=0.55, relwidth=0.914)

        # Assignment Question label
        self.assignment_label = tk.Label(self.canvas_query)
        self.assignment_label.place(
            relx=0.01, rely=0.03, relheight=0.1, relwidth=0.6)
        self.assignment_label.configure(anchor='w')
        self.assignment_label.configure(background="white")
        self.assignment_label.configure(
            font="-family {Segoe UI Historic} -size 20 -weight bold -underline 1")
        self.assignment_label.configure(foreground="#000000")
        self.assignment_label.configure(text='''Assignment Question''')

        # Question label
        self.question_label = tk.Label(self.canvas_query)
        self.question_label.place(
            relx=0.01, rely=0.15, relheight=0.1, relwidth=0.3)
        self.question_label.configure(anchor='w')
        self.question_label.configure(background="#ffffff")
        self.question_label.configure(
            font="-family {Segoe UI Historic} -size 13")
        self.question_label.configure(foreground="#000000")
        self.question_label.configure(text='''Question''')

        # Textbox for question
        self.question_entry = tk.Text(self.canvas_query)
        self.question_entry.place(
            relx=0.01, rely=0.27, relheight=0.22, relwidth=0.98)
        self.question_entry.configure(background="white")
        self.question_entry.configure(cursor="fleur")
        self.question_entry.configure(font="TkFixedFont")
        self.question_entry.configure(foreground="#000000")
        self.question_entry.configure(insertbackground="black")

        # Query label
        self.query_label = tk.Label(self.canvas_query)
        self.query_label.place(relx=0.01, rely=0.51,
                               relheight=0.1, relwidth=0.1)
        self.query_label.configure(anchor='w')
        self.query_label.configure(background="#ffffff")
        self.query_label.configure(font="-family {Segoe UI Historic} -size 13")
        self.query_label.configure(foreground="#000000")
        self.query_label.configure(text='''Query''')

        # Textbox for query
        self.query_entry = tk.Text(self.canvas_query)
        self.query_entry.place(relx=0.01, rely=0.63,
                               relheight=0.22, relwidth=0.98)
        self.query_entry.configure(background="white")
        self.query_entry.configure(cursor="fleur")
        self.query_entry.configure(font="TkFixedFont")
        self.query_entry.configure(foreground="#000000")
        self.query_entry.configure(insertbackground="black")

        # Difficulty label
        self.input_difficulty_label = tk.Label(self.canvas_query)
        self.input_difficulty_label.place(
            relx=0.01, rely=0.88, relheight=0.1, relwidth=0.15)
        self.input_difficulty_label.configure(anchor='w')
        self.input_difficulty_label.configure(background="#ffffff")
        self.input_difficulty_label.configure(cursor="fleur")
        self.input_difficulty_label.configure(foreground="#000000")
        self.input_difficulty_label.configure(
            font="-family {Segoe UI Historic} -size 13")
        self.input_difficulty_label.configure(text='''Difficulty''')

        # Difficulty dropdown for Input Questions/Test Queries function
        # Difficulty array for the difficulty dropdown
        DIFFICULTY = ["001", "002", "003", "004", "005"]
        input_variable = StringVar(self.canvas_query)
        # Default drowdown value
        input_variable.set(DIFFICULTY[0])

        # GUI dropdown that allows the user to select the difficuilty of the queries they wish to select from (and the label next to it)
        input_difficulty = tk.OptionMenu(
            self.canvas_query, input_variable, *DIFFICULTY)
        input_difficulty.place(relx=0.2, rely=0.88,
                               relheight=0.1, relwidth=0.3)

        # Create Input Questions/Test Queries title
        self.input_header_label = tk.Label(self.input_canvas)
        self.input_header_label.place(
            relx=0.043, rely=0.0, relheight=0.075, relwidth=0.914)
        self.input_header_label.configure(background="#0052A0")
        self.input_header_label.configure(
            font="-family {Segoe UI} -size 20 -weight bold")
        self.input_header_label.configure(foreground="#ffffff")
        self.input_header_label.configure(
            text='''Input Questions/Test Queries''')

        # Back button for Input Questions/Test Queries function
        self.input_assignment_questions_back_button_photo = PhotoImage(
            file="Pictures/Back.png")
        self.input_assignment_questions_back_button_photoImage = self.input_assignment_questions_back_button_photo.subsample(
            1, 1)
        self.input_assignment_questions_back_button = tk.Button(
            self.input_canvas, image=self.input_assignment_questions_back_button_photoImage)
        self.input_assignment_questions_back_button.place(
            relx=0, rely=0, relheight=0.075, relwidth=0.043)
        self.input_assignment_questions_back_button.configure(
            activebackground="#0052A0")
        self.input_assignment_questions_back_button.configure(
            activeforeground="#000000")
        self.input_assignment_questions_back_button.configure(
            background="#0052A0")
        self.input_assignment_questions_back_button.configure(
            foreground="white")
        self.input_assignment_questions_back_button.configure(pady="0")
        self.input_assignment_questions_back_button.configure(
            command=self.turn_on_test_query_menu)

        # Create submit button in Input Questions/Test Queries

        self.submit_button = tk.Button(self.input_canvas)
        self.submit_button.place(
            relx=0.826, rely=0.64, relheight=0.05, relwidth=0.13)
        self.submit_button.configure(activebackground="white")
        self.submit_button.configure(activeforeground="#000000")
        self.submit_button.configure(background="#0052A0")
        self.submit_button.configure(foreground="white")
        self.submit_button.configure(pady="0")
        self.submit_button.configure(text='''Submit''')
        self.submit_button.configure(
            command=lambda: self.input_SQL_query(input_variable.get()[2]))

        # Select Assignment Questions Page

        # Create the main canvas for Select Assignment Questions functionality
        self.select_canvas = tk.Canvas(self.main_canvas, bg="white")
        self.select_canvas.place(relx=0.0, rely=0.3, relheight=1, relwidth=1)
        self.select_canvas.place_forget()

        # Create Select Assignment Questions title
        self.select_header_label = tk.Label(self.select_canvas)
        self.select_header_label.place(
            relx=0.043, rely=0.0, relheight=0.075, relwidth=0.914)
        self.select_header_label.configure(background="#0052A0")
        self.select_header_label.configure(
            font="-family {Segoe UI} -size 20 -weight bold")
        self.select_header_label.configure(foreground="#ffffff")
        self.select_header_label.configure(
            text='''Select Assignment Questions''')

        # Back button for Select Assignment Questions function
        self.select_assignment_questions_back_button_photo = PhotoImage(
            file="Pictures/Back.png")
        self.select_assignment_questions_back_button_photoImage = self.select_assignment_questions_back_button_photo.subsample(
            1, 1)
        self.select_assignment_questions_back_button = tk.Button(
            self.select_canvas, image=self.select_assignment_questions_back_button_photoImage)
        self.select_assignment_questions_back_button.place(
            relx=0, rely=0, relheight=0.075, relwidth=0.043)
        self.select_assignment_questions_back_button.configure(
            activebackground="#0052A0")
        self.select_assignment_questions_back_button.configure(
            activeforeground="#000000")
        self.select_assignment_questions_back_button.configure(
            background="#0052A0")
        self.select_assignment_questions_back_button.configure(
            foreground="white")
        self.select_assignment_questions_back_button.configure(pady="0")
        self.select_assignment_questions_back_button.configure(text='''Back''')
        self.select_assignment_questions_back_button.configure(
            command=self.turn_on_test_query_menu)

        # Create canvas for filter search area in Select Assignment Questions functionality
        self.select_search_canvas = tk.Canvas(self.select_canvas)
        self.select_search_canvas.place(
            relx=0.040, rely=0.1, relheight=0.214, relwidth=0.92)
        self.select_search_canvas.configure(background="white")
        self.select_search_canvas.configure(borderwidth="2")
        self.select_search_canvas.configure(insertbackground="black")
        self.select_search_canvas.configure(relief="solid")

        # Filter search label
        self.filter_search_label = tk.Label(self.select_search_canvas)
        self.filter_search_label.place(
            relx=0.01, rely=0.05, relheight=0.2, relwidth=0.2)
        self.filter_search_label.configure(anchor='w')
        self.filter_search_label.configure(background="#ffffff")
        self.filter_search_label.configure(
            font="-family {Segoe UI} -size 15 -weight bold -underline 1")
        self.filter_search_label.configure(foreground="#000000")
        self.filter_search_label.configure(text='''Filter search:''')

        # Difficulty label
        self.select_search_difficulty_label = tk.Label(
            self.select_search_canvas)
        self.select_search_difficulty_label.place(
            relx=0.01, rely=0.5, relheight=0.2, relwidth=0.1)
        self.select_search_difficulty_label.configure(background="white")
        self.select_search_difficulty_label.configure(anchor='w')
        self.select_search_difficulty_label.configure(
            font="-family {Segoe UI Historic} -size 13")
        self.select_search_difficulty_label.configure(foreground="#000000")
        self.select_search_difficulty_label.configure(
            text='''Search by difficulty:''')

        # Find button
        self.find_button = tk.Button(self.select_search_canvas)
        self.find_button.place(relx=0.88, rely=0.72,
                               relheight=0.2, relwidth=0.1)
        self.find_button.configure(activebackground="white")
        self.find_button.configure(activeforeground="#000000")
        self.find_button.configure(background="#0052A0")
        self.find_button.configure(foreground="white")
        self.find_button.configure(pady="0")
        self.find_button.configure(text='''Find''')
        self.find_button.configure(
            command=lambda: self.add_table_select(search_variable.get()[2]))

        # Canvas for select student query area
        self.select_area_canvas = tk.Canvas(self.select_canvas)
        self.select_area_canvas.place(relx=0, rely=0, relheight=1, relwidth=1)
        self.select_area_canvas.configure(background="white")
        self.select_area_canvas.configure(insertbackground="black")
        self.select_area_canvas.configure(relief="solid")
        self.select_area_canvas.place_forget()

        # Canvas for storing the grid table which containing the Assignment Questions table
        self.select_table_canvas = tk.Canvas(self.select_area_canvas)
        self.select_table_canvas.place(relx=0, rely=0, relheight=1, relwidth=1)
        self.select_table_canvas.configure(background="#0052A0")
        self.select_table_canvas.configure(insertbackground="black")
        self.select_table_canvas.configure(relief="solid")
        self.select_table_canvas.place_forget()

        # Save button for Select Assignment Questions function
        self.select_save_button = tk.Button(self.select_canvas)
        self.select_save_button.place(
            relx=0.85, rely=0.63, relheight=0.05, relwidth=0.107)
        self.select_save_button.configure(activebackground="white")
        self.select_save_button.configure(activeforeground="#000000")
        self.select_save_button.configure(background="#0052A0")
        self.select_save_button.configure(foreground="white")
        self.select_save_button.configure(pady="0")
        self.select_save_button.configure(text='''Save''')
        self.select_save_button.configure(
            command=self.select_SQL_query_message)

        # Difficulty dropdown for Select Assignment Questions function
        # Difficulty array for the difficulty dropdown
        DIFFICULTY = ["001", "002", "003", "004", "005"]
        search_variable = StringVar(self.select_search_canvas)
        # Default drowdown value
        search_variable.set(DIFFICULTY[0])

        # GUI dropdown that allows the user to select the difficuilty of the queries they wish to select from (and the label next to it)
        search_difficulty = tk.OptionMenu(
            self.select_search_canvas, search_variable, *DIFFICULTY)
        search_difficulty.place(
            relx=0.2, rely=0.5, relheight=0.2, relwidth=0.2)

        # Student Query Page

        # Create canvas for Student Query function
        self.student_canvas = tk.Canvas(self.main_canvas, bg="white")
        self.student_canvas.place(relx=0.0, rely=0.3, relheight=1, relwidth=1)
        self.student_canvas.place_forget()

        # Create Read In Student Queries title
        self.select_header_label = tk.Label(self.student_canvas)
        self.select_header_label.place(
            relx=0.043, rely=0.0, relheight=0.075, relwidth=0.914)
        self.select_header_label.configure(background="#0052A0")
        self.select_header_label.configure(
            font="-family {Segoe UI} -size 20 -weight bold")
        self.select_header_label.configure(foreground="#ffffff")
        self.select_header_label.configure(text='''Read In Student Queries''')

        # Browse label for Read In Student Queries function
        self.browse_label = tk.Label(self.student_canvas)
        self.browse_label.place(relx=0.04, rely=0.1,
                                relheight=0.05, relwidth=0.8)
        self.browse_label.configure(anchor='w')
        self.browse_label.configure(background="white")
        self.browse_label.configure(
            font="-family {Segoe UI Historic} -size 13")
        self.browse_label.configure(
            text='''Browse and select the zip folder that contains the student files:''')

        # Create canvas for browse file area in Read In Student Queries function
        self.browse_canvas = tk.Canvas(self.student_canvas)
        self.browse_canvas.place(
            relx=0.040, rely=0.15, relheight=0.2, relwidth=0.8)
        self.browse_canvas.configure(background="white")
        self.browse_canvas.configure(borderwidth="2")
        self.browse_canvas.configure(insertbackground="black")
        self.browse_canvas.configure(relief="solid")

        # Upload button for Read In Student Queries function
        self.upload_button = tk.Button(self.student_canvas)
        self.upload_button.place(relx=0.85, rely=0.15,
                                 relheight=0.05, relwidth=0.107)
        self.upload_button.configure(activebackground="white")
        self.upload_button.configure(background="#0052A0")
        self.upload_button.configure(highlightbackground="white")
        self.upload_button.configure(highlightcolor="white")
        self.upload_button.configure(foreground="white")
        self.upload_button.configure(pady="0")
        self.upload_button.configure(text='''Upload''')
        self.upload_button.configure(command=self.upload_SQL)

        # Function to return the destination of the selected file
        def search(canvas):
            zipfile = filedialog.askopenfile(
                title="Select the Zip file that contains the Student Files")
            chosen_directory_label = Label(canvas, text="The student files have been successfully extracted from: " + "\n" + zipfile.name + " \n" +
                                           "to a temporary directory. Click upload to read them into the system.", font=("Calibri", 11), width=45, wraplength=1100, anchor="nw")
            chosen_directory_label.place(
                relx=0.16, rely=0.1, relheight=0.45, relwidth=0.81)
            chosen_directory_label.configure(anchor="nw")
            chosen_directory_label.configure(background="white")
            Query.extractFromZip(zipfile.name)

        # Browse button for Read In Student Queries function
        self.browse_button = tk.Button(self.browse_canvas)
        self.browse_button.place(
            relx=0.03, rely=0.1, relheight=0.2, relwidth=0.107)
        self.browse_button.configure(activebackground="white")
        self.browse_button.configure(background="#0052A0")
        self.browse_button.configure(highlightbackground="white")
        self.browse_button.configure(highlightcolor="white")
        self.browse_button.configure(foreground="white")
        self.browse_button.configure(pady="0")
        self.browse_button.configure(text='''Browse''')
        self.browse_button.configure(
            command=lambda: search(self.browse_canvas))

        # Create canvas for the selected query area
        self.selected_canvas = tk.Canvas(self.student_canvas)
        self.selected_canvas.place(
            relx=0.040, rely=0.4, relheight=0.28, relwidth=0.8)
        self.selected_canvas.configure(background="white")
        self.selected_canvas.configure(borderwidth="2")
        self.selected_canvas.configure(insertbackground="black")
        self.selected_canvas.configure(relief="solid")
        self.selected_canvas.place_forget()

        # Student vs. Test Query Page

        # Create canvas for Student Vs. Test Query function
        self.main_SVT_canvas = tk.Canvas(self.main_canvas, bg="white")
        self.main_SVT_canvas.place(relx=0.0, rely=0.3, relheight=1, relwidth=1)
        self.main_SVT_canvas.place_forget()

        # Canvas for the first page of Student Vs. Test Query function
        self.SVT_canvas = tk.Canvas(self.main_SVT_canvas, bg="white")
        self.SVT_canvas.place(relx=0.0, rely=0, relheight=1, relwidth=1)

        # Title label for Student vs. Test Query function
        self.SVT_header_label = tk.Label(self.SVT_canvas)
        self.SVT_header_label.place(
            relx=0.043, rely=0.0, relheight=0.075, relwidth=0.914)
        self.SVT_header_label.configure(background="#0052A0")
        self.SVT_header_label.configure(
            font="-family {Segoe UI} -size 20 -weight bold")
        self.SVT_header_label.configure(foreground="#ffffff")
        self.SVT_header_label.configure(text='''Student vs. Test Query''')

        # Canvas for selecting student query file
        self.SVT_selected_student_query_canvas = tk.Canvas(self.SVT_canvas)
        self.SVT_selected_student_query_canvas.place(
            relx=0.040, rely=0.1, relheight=0.494, relwidth=0.92)
        self.SVT_selected_student_query_canvas.configure(background="white")
        self.SVT_selected_student_query_canvas.configure(borderwidth="2")
        self.SVT_selected_student_query_canvas.configure(
            insertbackground="black")
        self.SVT_selected_student_query_canvas.configure(relief="solid")
        self.SVT_selected_student_query_canvas.place_forget()

        # Canvas for selecting student query file (after using search function)
        self.search_SVT_selected_student_query_canvas = tk.Canvas(
            self.SVT_canvas)
        self.search_SVT_selected_student_query_canvas.place(
            relx=0.040, rely=0.1, relheight=0.494, relwidth=0.92)
        self.search_SVT_selected_student_query_canvas.configure(
            background="white")
        self.search_SVT_selected_student_query_canvas.configure(
            borderwidth="2")
        self.search_SVT_selected_student_query_canvas.configure(
            insertbackground="black")
        self.search_SVT_selected_student_query_canvas.configure(relief="solid")
        self.search_SVT_selected_student_query_canvas.place_forget()

        # Canvas for Generate functionality
        self.generate_SVT_canvas = tk.Canvas(self.main_SVT_canvas, bg="white")
        self.generate_SVT_canvas.place(
            relx=0.0, rely=0, relheight=1, relwidth=1)
        self.generate_SVT_canvas.place_forget()

        # Title label for Generate functionality
        self.generate_SVT_header_label = tk.Label(self.generate_SVT_canvas)
        self.generate_SVT_header_label.place(
            relx=0.043, rely=0.0, relheight=0.075, relwidth=0.914)
        self.generate_SVT_header_label.configure(background="#0052A0")
        self.generate_SVT_header_label.configure(
            font="-family {Segoe UI} -size 20 -weight bold")
        self.generate_SVT_header_label.configure(foreground="#ffffff")
        self.generate_SVT_header_label.configure(
            text='''Student vs. Test Query (Generate)''')

        # Canvas for Export functionality
        self.export_SVT_canvas = tk.Canvas(self.main_SVT_canvas, bg="white")
        self.export_SVT_canvas.place(relx=0.0, rely=0, relheight=1, relwidth=1)
        self.export_SVT_canvas.place_forget()

        # Title label for Export functionality
        self.export_SVT_header_label = tk.Label(self.export_SVT_canvas)
        self.export_SVT_header_label.place(
            relx=0.043, rely=0.0, relheight=0.075, relwidth=0.914)
        self.export_SVT_header_label.configure(background="#0052A0")
        self.export_SVT_header_label.configure(
            font="-family {Segoe UI} -size 20 -weight bold")
        self.export_SVT_header_label.configure(foreground="#ffffff")
        self.export_SVT_header_label.configure(
            text='''Student vs. Test Query (Export)''')

        # Canvas for Graph functionality
        self.graph_SVT_canvas = tk.Canvas(self.main_SVT_canvas, bg="white")
        self.graph_SVT_canvas.place(relx=0.0, rely=0, relheight=1, relwidth=1)
        self.graph_SVT_canvas.place_forget()

        # Title label for Graph functionality
        self.graph_SVT_header_label = tk.Label(self.graph_SVT_canvas)
        self.graph_SVT_header_label.place(
            relx=0.043, rely=0.0, relheight=0.075, relwidth=0.914)
        self.graph_SVT_header_label.configure(background="#0052A0")
        self.graph_SVT_header_label.configure(
            font="-family {Segoe UI} -size 20 -weight bold")
        self.graph_SVT_header_label.configure(foreground="#ffffff")
        self.graph_SVT_header_label.configure(
            text='''Student vs. Test Query (Graph)''')

        # Canvas for select graph's type functionality
        self.graph_SVT_types_canvas = tk.Canvas(
            self.graph_SVT_canvas, bg="white")
        self.graph_SVT_types_canvas.place(
            relx=0.043, rely=0.08, relheight=0.62, relwidth=0.914)
        self.graph_SVT_types_canvas.place_forget()

        # Button to export a graph show the average point for all questions
        self.avg_point_graph_photo = PhotoImage(file = r"Pictures/Average Graph.png")
        self.avg_point_graph_photoImage = self.avg_point_graph_photo.subsample(1,1)
        self.avg_point_graph_button = tk.Button(self.graph_SVT_types_canvas, image = self.avg_point_graph_photoImage, compound = BOTTOM)
        self.avg_point_graph_button.place(
            relx=0.02, rely=0.085, relheight=0.7, relwidth=0.28)
        self.avg_point_graph_button.configure(activebackground="#A4CAED")
        self.avg_point_graph_button.configure(activeforeground="white")
        self.avg_point_graph_button.configure(activeforeground="#000000")
        self.avg_point_graph_button.configure(anchor='n')
        self.avg_point_graph_button.configure(
            font="-family {Segoe UI Historic} -size 15 -weight bold")
        self.avg_point_graph_button.configure(background="#A4CAED")
        self.avg_point_graph_button.configure(foreground="#000000")
        self.avg_point_graph_button.configure(highlightcolor="black")
        self.avg_point_graph_button.configure(pady="0")
        self.avg_point_graph_button.configure(
            text='''Graph Average Point For All Questions''')
        self.avg_point_graph_button.configure(command =lambda : Marks.graphAverageScore(DatabaseConnection.establishConnectionGUI(main_menu.makeConnectionString(
                self.server_connection_entry.get("1.0", 'end'), self.sql_db_entry.get("1.0", 'end-1c')), "No Pop Up")))


        # Button to export a graph show the point for each question
        self.question_graph_photo = PhotoImage(file = r"Pictures/Question Graph.png")
        self.question_graph_photoImage = self.question_graph_photo.subsample(1,1)
        self.question_graph_button = tk.Button(self.graph_SVT_types_canvas, image = self.question_graph_photoImage, compound = BOTTOM)
        self.question_graph_button.place(
            relx=0.36, rely=0.085, relheight=0.7, relwidth=0.28)
        self.question_graph_button.configure(activebackground="#A4CAED")
        self.question_graph_button.configure(activeforeground="white")
        self.question_graph_button.configure(activeforeground="#000000")
        self.question_graph_button.configure(anchor='n')
        self.question_graph_button.configure(
            font="-family {Segoe UI Historic} -size 15 -weight bold")
        self.question_graph_button.configure(background="#A4CAED")
        self.question_graph_button.configure(foreground="#000000")
        self.question_graph_button.configure(highlightcolor="black")
        self.question_graph_button.configure(pady="0")
        self.question_graph_button.configure(
            text='''Graph For Each Question''')
        self.question_graph_button.configure(
            command= lambda: self.turn_on_question_graph(DatabaseConnection.establishConnectionGUI(main_menu.makeConnectionString(
                self.server_connection_entry.get("1.0", 'end'), self.sql_db_entry.get("1.0", 'end-1c')), "No Pop Up")))

        # Canvas for setting the graph of each question
        self.question_graph_canvas = tk.Canvas(self.graph_SVT_canvas)
        self.question_graph_canvas.configure(background="white")
        self.question_graph_canvas.configure(insertbackground="black")
        self.question_graph_canvas.configure(relief="solid")
        self.question_graph_canvas.place_forget()

        # Title label for graph functionality
        self.question_graph_header_label = tk.Label(self.question_graph_canvas)
        self.question_graph_header_label.place(
            relx=0.043, rely=0.0, relheight=0.075, relwidth=0.914)
        self.question_graph_header_label.configure(background="#0052A0")
        self.question_graph_header_label.configure(
            font="-family {Segoe UI} -size 20 -weight bold")
        self.question_graph_header_label.configure(foreground="#ffffff")
        self.question_graph_header_label.configure(
            text='''Student vs. Test Query (Question Graph)''')

        # Back button for question graph functionality
        self.question_graph_back_button_photo = PhotoImage(
            file="Pictures/Back.png")
        self.question_graph_back_button_photoImage = self.question_graph_back_button_photo.subsample(
            1, 1)
        self.question_graph_back_button = tk.Button(
            self.question_graph_canvas, image=self.question_graph_back_button_photoImage)
        self.question_graph_back_button.place(
            relx=0, rely=0, relheight=0.075, relwidth=0.043)
        self.question_graph_back_button.configure(activebackground="#0052A0")
        self.question_graph_back_button.configure(activeforeground="#000000")
        self.question_graph_back_button.configure(background="#0052A0")
        self.question_graph_back_button.configure(foreground="white")
        self.question_graph_back_button.configure(pady="0")
        self.question_graph_back_button.configure(text='''Back''')
        self.question_graph_back_button.configure(command=self.turn_on_graph)

        # Header Question ID label for question graph functionality
        self.header_question_graph_question_ID_label = tk.Label(
            self.question_graph_canvas)
        self.header_question_graph_question_ID_label.place(
            relx=0.043, rely=0.15, relheight=0.1, relwidth=0.3)
        self.header_question_graph_question_ID_label.configure(anchor='w')
        self.header_question_graph_question_ID_label.configure(background="#ffffff")
        self.header_question_graph_question_ID_label.configure(
            font="-family {Segoe UI Historic} -size 13 -weight bold")
        self.header_question_graph_question_ID_label.configure(foreground="#000000")
        self.header_question_graph_question_ID_label.configure(text='''Choose the question ID from the following list''')

        # Question ID label for question graph functionality
        self.question_graph_question_ID_label = tk.Label(
            self.question_graph_canvas)
        self.question_graph_question_ID_label.place(
            relx=0.043, rely=0.25, relheight=0.1, relwidth=0.15)
        self.question_graph_question_ID_label.configure(anchor='w')
        self.question_graph_question_ID_label.configure(background="#ffffff")
        self.question_graph_question_ID_label.configure(
            font="-family {Segoe UI Historic} -size 13")
        self.question_graph_question_ID_label.configure(foreground="#000000")
        self.question_graph_question_ID_label.configure(text='''Assignment Question Number''')

        # Save button for question graph functionality
        self.question_graph_save_button = tk.Button(self.question_graph_canvas)
        self.question_graph_save_button.place(
            relx=0.807, rely=0.45, relheight=0.05, relwidth=0.15)
        self.question_graph_save_button.configure(activebackground="white")
        self.question_graph_save_button.configure(activeforeground="#000000")
        self.question_graph_save_button.configure(background="#0052A0")
        self.question_graph_save_button.configure(foreground="white")
        self.question_graph_save_button.configure(pady="0")
        self.question_graph_save_button.configure(text='''Generate Graph''')
        self.question_graph_save_button.configure(command = lambda: Marks.graphAllStudentsForQuestion(DatabaseConnection.establishConnectionGUI(main_menu.makeConnectionString(
                self.server_connection_entry.get("1.0", 'end'), self.sql_db_entry.get("1.0", 'end-1c')), "No Pop Up"), questionid_variable.get()))
       

        # Button to export a graph show the point for each student
        self.student_graph_photo = PhotoImage(file = r"Pictures/Student Graph.png")
        self.student_graph_photoImage = self.student_graph_photo.subsample(1,1)
        self.student_graph_button = tk.Button(self.graph_SVT_types_canvas, image = self.student_graph_photoImage, compound = BOTTOM)
        self.student_graph_button.place(
            relx=0.7, rely=0.085, relheight=0.7, relwidth=0.28)
        self.student_graph_button.configure(activebackground="#A4CAED")
        self.student_graph_button.configure(activeforeground="white")
        self.student_graph_button.configure(activeforeground="#000000")
        self.student_graph_button.configure(anchor='n')
        self.student_graph_button.configure(background="#A4CAED")
        self.student_graph_button.configure(
            font="-family {Segoe UI Historic} -size 15 -weight bold")
        self.student_graph_button.configure(foreground="#000000")
        self.student_graph_button.configure(highlightcolor="black")
        self.student_graph_button.configure(pady="0")
        self.student_graph_button.configure(text='''Graph For Each Student''')
        self.student_graph_button.configure(command= lambda: self.turn_on_student_graph(DatabaseConnection.establishConnectionGUI(main_menu.makeConnectionString(self.server_connection_entry.get("1.0", 'end'), self.sql_db_entry.get("1.0", 'end-1c')), "Yep")))

        # Canvas for setting the graph of each question
        self.student_graph_canvas = tk.Canvas(self.graph_SVT_canvas)
        self.student_graph_canvas.configure(background="white")
        self.student_graph_canvas.configure(insertbackground="black")
        self.student_graph_canvas.configure(relief="solid")
        self.student_graph_canvas.place_forget()

        # Title label for student graph functionality
        self.student_graph_header_label = tk.Label(self.student_graph_canvas)
        self.student_graph_header_label.place(
            relx=0.043, rely=0.0, relheight=0.075, relwidth=0.914)
        self.student_graph_header_label.configure(background="#0052A0")
        self.student_graph_header_label.configure(
            font="-family {Segoe UI} -size 20 -weight bold")
        self.student_graph_header_label.configure(foreground="#ffffff")
        self.student_graph_header_label.configure(
            text='''Student vs. Test Query (Student Graph)''')

        # Back button for student graph functionality
        self.student_graph_back_button_photo = PhotoImage(
            file="Pictures/Back.png")
        self.student_graph_back_button_photoImage = self.student_graph_back_button_photo.subsample(
            1, 1)
        self.student_graph_back_button = tk.Button(
            self.student_graph_canvas, image=self.student_graph_back_button_photoImage)
        self.student_graph_back_button.place(
            relx=0, rely=0, relheight=0.075, relwidth=0.043)
        self.student_graph_back_button.configure(activebackground="#0052A0")
        self.student_graph_back_button.configure(activeforeground="#000000")
        self.student_graph_back_button.configure(background="#0052A0")
        self.student_graph_back_button.configure(foreground="white")
        self.student_graph_back_button.configure(pady="0")
        self.student_graph_back_button.configure(text='''Back''')
        self.student_graph_back_button.configure(command=self.turn_on_graph)

        # Header Student ID label for student graph functionality
        self.header_student_graph_student_ID_label = tk.Label(
            self.student_graph_canvas)
        self.header_student_graph_student_ID_label.place(
            relx=0.043, rely=0.15, relheight=0.1, relwidth=0.3)
        self.header_student_graph_student_ID_label.configure(anchor='w')
        self.header_student_graph_student_ID_label.configure(background="#ffffff")
        self.header_student_graph_student_ID_label.configure(
            font="-family {Segoe UI Historic} -size 13 -weight bold")
        self.header_student_graph_student_ID_label.configure(foreground="#000000")
        self.header_student_graph_student_ID_label.configure(text='''Choose the student name from the following list''')

        # Student ID label for student graph functionality
        self.student_graph_student_ID_label = tk.Label(
            self.student_graph_canvas)
        self.student_graph_student_ID_label.place(
            relx=0.043, rely=0.25, relheight=0.1, relwidth=0.1)
        self.student_graph_student_ID_label.configure(anchor='w')
        self.student_graph_student_ID_label.configure(background="#ffffff")
        self.student_graph_student_ID_label.configure(
            font="-family {Segoe UI Historic} -size 13")
        self.student_graph_student_ID_label.configure(foreground="#000000")
        self.student_graph_student_ID_label.configure(text='''Student User Name''')

        # save button for question graph function
        self.student_graph_save_button = tk.Button(self.student_graph_canvas)
        self.student_graph_save_button.place(
            relx=0.807, rely=0.45, relheight=0.05, relwidth=0.15)
        self.student_graph_save_button.configure(activebackground="white")
        self.student_graph_save_button.configure(activeforeground="#000000")
        self.student_graph_save_button.configure(background="#0052A0")
        self.student_graph_save_button.configure(foreground="white")
        self.student_graph_save_button.configure(pady="0")
        self.student_graph_save_button.configure(text='''Generate Graph''')
        self.student_graph_save_button.configure(command = lambda: Marks.graphAllMarksForStudent(DatabaseConnection.establishConnectionGUI(main_menu.makeConnectionString(
                self.server_connection_entry.get("1.0", 'end'), self.sql_db_entry.get("1.0", 'end-1c')), "No Pop Up"), studentid_variable.get()))

        # # Canvas for searching student query file area in Student Vs. Test Query function
        # self.search_student_query_canvas = tk.Canvas(self.SVT_canvas)
        # self.search_student_query_canvas.place(
        #     relx=0.040, rely=0.1, relheight=0.214, relwidth=0.92)
        # self.search_student_query_canvas.configure(background="white")
        # self.search_student_query_canvas.configure(borderwidth="2")
        # self.search_student_query_canvas.configure(insertbackground="black")
        # self.search_student_query_canvas.configure(relief="solid")

        # # Select student query label in Student Vs. Test Query functions
        # self.select_student_query_label = tk.Label(
        #     self.search_student_query_canvas)
        # self.select_student_query_label.place(
        #     relx=0.01, rely=0.05, relheight=0.2, relwidth=0.3)
        # self.select_student_query_label.configure(anchor='w')
        # self.select_student_query_label.configure(background="#ffffff")
        # self.select_student_query_label.configure(
        #     font="-family {Segoe UI} -size 15 -weight bold -underline 1")
        # self.select_student_query_label.configure(foreground="#000000")
        # self.select_student_query_label.configure(
        #     text='''Select Student Query:''')

        # # Search by student ID label in Student Vs. Test Query function 
        # self.SVT_search_name_label = tk.Label(self.search_student_query_canvas)
        # self.SVT_search_name_label.place(
        #     relx=0.01, rely=0.4, relheight=0.2, relwidth=0.17)
        # self.SVT_search_name_label.configure(anchor='w')
        # self.SVT_search_name_label.configure(background="#ffffff")
        # self.SVT_search_name_label.configure(
        #     font="-family {Segoe UI Historic} -size 13")
        # self.SVT_search_name_label.configure(foreground="#000000")
        # self.SVT_search_name_label.configure(text='''Search By Student ID:''')

        # # Search by student ID textbox in Student Vs. Test Query function
        # self.SVT_search_name_entry = tk.Text(self.search_student_query_canvas)
        # self.SVT_search_name_entry.place(
        #     relx=0.18, rely=0.4, relheight=0.2, relwidth=0.25)
        # self.SVT_search_name_entry.configure(background="white")
        # self.SVT_search_name_entry.configure(font="TkFixedFont")
        # self.SVT_search_name_entry.configure(foreground="#000000")
        # self.SVT_search_name_entry.configure(insertbackground="black")

        # # Get input value from textbox
        # name_input = self.SVT_search_name_entry.get(1.0, "end-1c")

        # # Search button
        # self.SVT_search_button = tk.Button(self.search_student_query_canvas)
        # self.SVT_search_button.place(
        #     relx=0.88, rely=0.73, relheight=0.2, relwidth=0.1)
        # self.SVT_search_button.configure(activebackground="white")
        # self.SVT_search_button.configure(activeforeground="#000000")
        # self.SVT_search_button.configure(background="#0052A0")
        # self.SVT_search_button.configure(foreground="white")
        # self.SVT_search_button.configure(pady="0")
        # self.SVT_search_button.configure(text='''Search''')
        # self.SVT_search_button.configure(command=self.search_table)

        # Export button
        self.export_button = tk.Button(self.main_SVT_canvas)
        self.export_button.place(relx=0.62, rely=0.63,
                                 relheight=0.05, relwidth=0.15)
        self.export_button.configure(activebackground="white")
        self.export_button.configure(activeforeground="#000000")
        self.export_button.configure(background="#0052A0")
        self.export_button.configure(foreground="white")
        self.export_button.configure(pady="0")
        self.export_button.configure(text='''Export results''')
        self.export_button.configure(command=self.export_result_message)

        # Generate button
        self.generate_button = tk.Button(self.main_SVT_canvas)
        self.generate_button.place(
            relx=0.433, rely=0.63, relheight=0.05, relwidth=0.15)
        self.generate_button.configure(activebackground="white")
        self.generate_button.configure(activeforeground="#000000")
        self.generate_button.configure(background="#0052A0")
        self.generate_button.configure(foreground="white")
        self.generate_button.configure(pady="0")
        self.generate_button.configure(text='''Generate results''')
        self.generate_button.configure(command=lambda: self.generate_table(DatabaseConnection.establishConnectionGUI(main_menu.makeConnectionString(self.server_connection_entry.get("1.0", 'end'), self.sql_db_entry.get(
            "1.0", 'end-1c')), "No Pop Ups"), DatabaseConnection.establishConnectionGUI(main_menu.makeConnectionString(self.server_connection_entry.get("1.0", 'end'), self.assignment_db_entry.get("1.0", 'end-1c')), "Yep")))

        # Graph button
        self.graph_button = tk.Button(self.main_SVT_canvas)
        self.graph_button.place(relx=0.807, rely=0.63,
                                relheight=0.05, relwidth=0.15)
        self.graph_button.configure(activebackground="white")
        self.graph_button.configure(activeforeground="#000000")
        self.graph_button.configure(background="#0052A0")
        self.graph_button.configure(foreground="white")
        self.graph_button.configure(pady="0")
        self.graph_button.configure(text='''Graph results''')
        self.graph_button.configure(command=self.turn_on_graph)
        # self.graph_button.configure(command= lambda: Marks.graphAllStudentsForQuestion(DatabaseConnection.establishConnectionGUI(main_menu.makeConnectionString(self.server_connection_entry.get("1.0",'end'), self.sql_db_entry.get("1.0",'end-1c')),"Q1004"))

        # Settings Page

        # Create the main canvas for Settings function
        self.database_canvas = tk.Canvas(self.main_canvas, bg="white")
        self.database_canvas.place(relx=0.0, rely=0.3, relheight=1, relwidth=1)
        self.database_canvas.place_forget()

        # Create Settings title
        self.database_header_label = tk.Label(self.database_canvas)
        self.database_header_label.place(
            relx=0.043, rely=0.0, relheight=0.075, relwidth=0.914)
        self.database_header_label.configure(background="#0052A0")
        self.database_header_label.configure(
            font="-family {Segoe UI} -size 20 -weight bold")
        self.database_header_label.configure(foreground="#ffffff")
        self.database_header_label.configure(text='''Settings''')

        # Create canvas for Database Connection area in Setting functionality
        self.setting_connection_canvas = tk.Canvas(self.database_canvas)
        self.setting_connection_canvas.place(
            relx=0.040, rely=0.08, relheight=0.28, relwidth=0.92)
        self.setting_connection_canvas.configure(background="white")
        self.setting_connection_canvas.configure(borderwidth="1")
        self.setting_connection_canvas.configure(insertbackground="black")
        self.setting_connection_canvas.configure(relief="solid")

        # Create Database Connection title
        self.db_header_label = tk.Label(self.setting_connection_canvas)
        self.db_header_label.place(
            relx=0.0015, rely=0.011, relheight=0.15, relwidth=0.997)
        self.db_header_label.configure(background="#0052A0")
        self.db_header_label.configure(
            font="-family {Segoe UI} -size 13 -weight bold")
        self.db_header_label.configure(foreground="#ffffff")
        self.db_header_label.configure(text='''Database Connection''')

        # Server Connection label
        self.server_connection_label = tk.Label(self.setting_connection_canvas)
        self.server_connection_label.place(
            relx=0.05, rely=0.165, relheight=0.11, relwidth=0.8)
        self.server_connection_label.configure(anchor='w')
        self.server_connection_label.configure(background="#ffffff")
        self.server_connection_label.configure(
            font="-family {Segoe UI Historic} -size 11")
        self.server_connection_label.configure(foreground="#000000")
        self.server_connection_label.configure(text='''Server Connection''')

        # Create textbox to input Server Connection
        self.server_connection_entry = tk.Text(self.setting_connection_canvas)
        self.server_connection_entry.place(
            relx=0.05, rely=0.285, relheight=0.11, relwidth=0.62)
        self.server_connection_entry.configure(background="white")
        self.server_connection_entry.configure(font="TkFixedFont")
        self.server_connection_entry.configure(foreground="#000000")
        self.server_connection_entry.configure(insertbackground="black")

        # Create test button for Server Connection
        self.server_connection_test_button = tk.Button(
            self.setting_connection_canvas)
        self.server_connection_test_button.place(
            relx=0.73, rely=0.285, relheight=0.11, relwidth=0.1)
        self.server_connection_test_button.configure(activebackground="white")
        self.server_connection_test_button.configure(
            activeforeground="#000000")
        self.server_connection_test_button.configure(background="#0052A0")
        self.server_connection_test_button.configure(foreground="white")
        self.server_connection_test_button.configure(pady="0")
        self.server_connection_test_button.configure(text='''Test''')
        self.server_connection_test_button.configure(command=lambda: DatabaseConnection.testConnectionGUI(
            self.server_connection_entry.get("1.0", 'end')))

        # Create connect button for Server Connection
        self.server_connection_connect_button = tk.Button(
            self.setting_connection_canvas)
        self.server_connection_connect_button.place(
            relx=0.85, rely=0.285, relheight=0.11, relwidth=0.1)
        self.server_connection_connect_button.configure(
            activebackground="white")
        self.server_connection_connect_button.configure(
            activeforeground="#000000")
        self.server_connection_connect_button.configure(background="#0052A0")
        self.server_connection_connect_button.configure(foreground="white")
        self.server_connection_connect_button.configure(pady="0")
        self.server_connection_connect_button.configure(text='''Connect''')
        self.server_connection_connect_button.configure(command=lambda: DatabaseConnection.establishConnectionGUI(
            self.server_connection_entry.get("1.0", 'end'), "Settings"))

        # SQL Checker Database Connection label
        self.sql_db_label = tk.Label(self.setting_connection_canvas)
        self.sql_db_label.place(relx=0.05, rely=0.425,
                                relheight=0.11, relwidth=0.8)
        self.sql_db_label.configure(anchor='w')
        self.sql_db_label.configure(background="#ffffff")
        self.sql_db_label.configure(
            font="-family {Segoe UI Historic} -size 11")
        self.sql_db_label.configure(foreground="#000000")
        self.sql_db_label.configure(text='''SQL Checker Database Connection''')

        # Create textbox to input SQL Checker Database Connection
        self.sql_db_entry = tk.Text(self.setting_connection_canvas)
        self.sql_db_entry.place(relx=0.05, rely=0.545,
                                relheight=0.11, relwidth=0.62)
        self.sql_db_entry.configure(background="white")
        self.sql_db_entry.configure(font="TkFixedFont")
        self.sql_db_entry.configure(foreground="#000000")
        self.sql_db_entry.configure(insertbackground="black")

        # Create test button for SQL Checker Database Connection
        self.sql_db_test_button = tk.Button(self.setting_connection_canvas)
        self.sql_db_test_button.place(
            relx=0.73, rely=0.545, relheight=0.11, relwidth=0.1)
        self.sql_db_test_button.configure(activebackground="white")
        self.sql_db_test_button.configure(activeforeground="#000000")
        self.sql_db_test_button.configure(background="#0052A0")
        self.sql_db_test_button.configure(foreground="white")
        self.sql_db_test_button.configure(pady="0")
        self.sql_db_test_button.configure(text='''Test''')
        self.sql_db_test_button.configure(command=lambda: DatabaseConnection.testConnectionGUI(
            main_menu.makeConnectionString(self.server_connection_entry.get("1.0", 'end'), self.sql_db_entry.get("1.0", 'end-1c'))))

        # Create connect button for SQL Checker Database Connection
        self.sql_db_connect_button = tk.Button(self.setting_connection_canvas)
        self.sql_db_connect_button.place(
            relx=0.85, rely=0.545, relheight=0.11, relwidth=0.1)
        self.sql_db_connect_button.configure(activebackground="white")
        self.sql_db_connect_button.configure(activeforeground="#000000")
        self.sql_db_connect_button.configure(background="#0052A0")
        self.sql_db_connect_button.configure(foreground="white")
        self.sql_db_connect_button.configure(pady="0")
        self.sql_db_connect_button.configure(text='''Connect''')
        self.sql_db_connect_button.configure(command=lambda: DatabaseConnection.establishConnectionGUI(main_menu.makeConnectionString(
            self.server_connection_entry.get("1.0", 'end'), self.sql_db_entry.get("1.0", 'end-1c')), "Settings"))

        # Assignment Data Database Connection label
        self.assignment_db_label = tk.Label(self.setting_connection_canvas)
        self.assignment_db_label.place(
            relx=0.05, rely=0.685, relheight=0.11, relwidth=0.8)
        self.assignment_db_label.configure(anchor='w')
        self.assignment_db_label.configure(background="#ffffff")
        self.assignment_db_label.configure(
            font="-family {Segoe UI Historic} -size 11")
        self.assignment_db_label.configure(foreground="#000000")
        self.assignment_db_label.configure(
            text='''Assignment Data Database Connection''')

        # Create textbox to input Assignment Data Database Connection
        self.assignment_db_entry = tk.Text(self.setting_connection_canvas)
        self.assignment_db_entry.place(
            relx=0.05, rely=0.805, relheight=0.11, relwidth=0.62)
        self.assignment_db_entry.configure(background="white")
        self.assignment_db_entry.configure(font="TkFixedFont")
        self.assignment_db_entry.configure(foreground="#000000")
        self.assignment_db_entry.configure(insertbackground="black")

        # Assignment Data Database Connection test button
        self.assignment_db_test_button = tk.Button(
            self.setting_connection_canvas)
        self.assignment_db_test_button.place(
            relx=0.73, rely=0.805, relheight=0.11, relwidth=0.1)
        self.assignment_db_test_button.configure(activebackground="white")
        self.assignment_db_test_button.configure(activeforeground="#000000")
        self.assignment_db_test_button.configure(background="#0052A0")
        self.assignment_db_test_button.configure(foreground="white")
        self.assignment_db_test_button.configure(pady="0")
        self.assignment_db_test_button.configure(text='''Test''')
        self.assignment_db_test_button.configure(command=lambda: DatabaseConnection.testConnectionGUI(
            main_menu.makeConnectionString(self.server_connection_entry.get("1.0", 'end'), self.assignment_db_entry.get("1.0", 'end-1c'))))

        # Assignment Data Database Connection connect button
        self.assignment_db_connect_button = tk.Button(
            self.setting_connection_canvas)
        self.assignment_db_connect_button.place(
            relx=0.85, rely=0.805, relheight=0.11, relwidth=0.1)
        self.assignment_db_connect_button.configure(activebackground="white")
        self.assignment_db_connect_button.configure(activeforeground="#000000")
        self.assignment_db_connect_button.configure(background="#0052A0")
        self.assignment_db_connect_button.configure(foreground="white")
        self.assignment_db_connect_button.configure(pady="0")
        self.assignment_db_connect_button.configure(text='''Connect''')
        self.assignment_db_connect_button.configure(command=lambda: DatabaseConnection.establishConnectionGUI(main_menu.makeConnectionString(
            self.server_connection_entry.get("1.0", 'end'), self.assignment_db_entry.get("1.0", 'end-1c')), "Settings"))

        # Semester canvas

        self.setting_semester_canvas = tk.Canvas(self.database_canvas)
        self.setting_semester_canvas.place(
            relx=0.040, rely=0.36, relheight=0.28, relwidth=0.92)
        self.setting_semester_canvas.configure(background="white")
        self.setting_semester_canvas.configure(borderwidth="1")
        self.setting_semester_canvas.configure(insertbackground="black")
        self.setting_semester_canvas.configure(relief="solid")

        # Create Semester title
        self.db_header_label = tk.Label(self.setting_semester_canvas)
        self.db_header_label.place(
            relx=0.0015, rely=0.011, relheight=0.15, relwidth=0.997)
        self.db_header_label.configure(background="#0052A0")
        self.db_header_label.configure(
            font="-family {Segoe UI} -size 13 -weight bold")
        self.db_header_label.configure(foreground="#ffffff")
        self.db_header_label.configure(text='''Semester''')

        # Study Period label
        self.study_period_label = tk.Label(self.setting_semester_canvas)
        self.study_period_label.place(
            relx=0.05, rely=0.2, relheight=0.12, relwidth=0.15)
        self.study_period_label.configure(anchor='w')
        self.study_period_label.configure(background="#ffffff")
        self.study_period_label.configure(
            font="-family {Segoe UI Historic} -size 11")
        self.study_period_label.configure(foreground="#000000")
        self.study_period_label.configure(text='''STUDY PERIOD''')

        # Study Period textbox
        self.study_period_entry = tk.Text(self.setting_semester_canvas)
        self.study_period_entry.place(
            relx=0.25, rely=0.2, relheight=0.12, relwidth=0.7)
        self.study_period_entry.configure(background="white")
        self.study_period_entry.configure(font="TkFixedFont")
        self.study_period_entry.configure(foreground="#000000")
        self.study_period_entry.configure(insertbackground="black")

        # Year label
        self.year_label = tk.Label(self.setting_semester_canvas)
        self.year_label.place(relx=0.05, rely=0.35,
                              relheight=0.12, relwidth=0.15)
        self.year_label.configure(anchor='w')
        self.year_label.configure(background="#ffffff")
        self.year_label.configure(font="-family {Segoe UI Historic} -size 11")
        self.year_label.configure(foreground="#000000")
        self.year_label.configure(text='''YEAR''')

        # Year textbox
        self.year_entry = tk.Text(self.setting_semester_canvas)
        self.year_entry.place(relx=0.25, rely=0.35,
                              relheight=0.12, relwidth=0.7)
        self.year_entry.configure(background="white")
        self.year_entry.configure(font="TkFixedFont")
        self.year_entry.configure(foreground="#000000")
        self.year_entry.configure(insertbackground="black")

        # Start Date label
        self.start_date_label = tk.Label(self.setting_semester_canvas)
        self.start_date_label.place(
            relx=0.05, rely=0.5, relheight=0.12, relwidth=0.15)
        self.start_date_label.configure(anchor='w')
        self.start_date_label.configure(background="#ffffff")
        self.start_date_label.configure(
            font="-family {Segoe UI Historic} -size 11")
        self.start_date_label.configure(foreground="#000000")
        self.start_date_label.configure(text='''START DATE''')

        # Start Date textbox
        self.start_date_entry = tk.Text(self.setting_semester_canvas)
        self.start_date_entry.place(
            relx=0.25, rely=0.5, relheight=0.12, relwidth=0.7)
        self.start_date_entry.configure(background="white")
        self.start_date_entry.configure(font="TkFixedFont")
        self.start_date_entry.configure(foreground="#000000")
        self.start_date_entry.configure(insertbackground="black")

        # End Date label
        self.end_date_label = tk.Label(self.setting_semester_canvas)
        self.end_date_label.place(
            relx=0.05, rely=0.65, relheight=0.12, relwidth=0.15)
        self.end_date_label.configure(anchor='w')
        self.end_date_label.configure(background="#ffffff")
        self.end_date_label.configure(
            font="-family {Segoe UI Historic} -size 11")
        self.end_date_label.configure(foreground="#000000")
        self.end_date_label.configure(text='''END DATE''')

        # End Date textbox
        self.end_date_entry = tk.Text(self.setting_semester_canvas)
        self.end_date_entry.place(
            relx=0.25, rely=0.65, relheight=0.12, relwidth=0.7)
        self.end_date_entry.configure(background="white")
        self.end_date_entry.configure(font="TkFixedFont")
        self.end_date_entry.configure(foreground="#000000")
        self.end_date_entry.configure(insertbackground="black")

        # Semester Code label
        self.semester_label = tk.Label(self.setting_semester_canvas)
        self.semester_label.place(
            relx=0.05, rely=0.8, relheight=0.12, relwidth=0.2)
        self.semester_label.configure(anchor='w')
        self.semester_label.configure(background="#ffffff")
        self.semester_label.configure(
            font="-family {Segoe UI Historic} -size 11")
        self.semester_label.configure(foreground="#000000")
        self.semester_label.configure(text='''SEMESTER CODE''')

        # Semester Code textbox
        self.semester_entry = tk.Text(self.setting_semester_canvas)
        self.semester_entry.place(
            relx=0.25, rely=0.8, relheight=0.12, relwidth=0.7)
        self.semester_entry.configure(background="white")
        self.semester_entry.configure(font="TkFixedFont")
        self.semester_entry.configure(foreground="#000000")
        self.semester_entry.configure(insertbackground="black")

        # Create save button for Setting page
        self.db_save_button = tk.Button(self.database_canvas)
        self.db_save_button.place(
            relx=0.807, rely=0.65, relheight=0.04, relwidth=0.15)
        self.db_save_button.configure(activebackground="white")
        self.db_save_button.configure(activeforeground="#000000")
        self.db_save_button.configure(background="#0052A0")
        self.db_save_button.configure(foreground="white")
        self.db_save_button.configure(pady="0")
        self.db_save_button.configure(text='''Save''')
        self.db_save_button.configure(command=lambda: Semester.SaveSemesterGUI(self.study_period_entry.get("1.0", 'end-1c'), self.year_entry.get("1.0", 'end-1c'),
                                                                               self.start_date_entry.get(
            "1.0", 'end-1c'), self.end_date_entry.get("1.0", 'end-1c'),
            self.semester_entry.get("1.0", 'end-1c'), DatabaseConnection.establishConnectionGUI(main_menu.makeConnectionString(self.server_connection_entry.get("1.0", 'end'), self.sql_db_entry.get("1.0", 'end-1c')), "Page")))

    # Retrieve student usernames for dropdown
    def retrieveStudents(self, connection):
        students = User.getAllUsers(connection)
        usernames = []
        for student in students:
            usernames.append(student.UserName)
        return usernames
    
    # Retrieve assignment question numbers for dropdown
    def retrieveAssignmentQuestions(self, connection):
        assignmentQuestions = AssignmentQuestion.getAllAssignmentQuestions(connection)
        questionNumbers =[]
        for question in assignmentQuestions:
            questionNumbers.append(question.questionNumber)
        return questionNumbers

    # Create deduction window when select a deduction button
    def create_deduction_page(self, selectedQuestion):

        # Get deduction data from database
        testQuery = testQuery = Query.retrieveTestQueryFromQuestionId(selectedQuestion[0], DatabaseConnection.establishConnectionGUI(
            main_menu.makeConnectionString(self.server_connection_entry.get("1.0", 'end'), self.sql_db_entry.get("1.0", 'end-1c')), "No Pop Ups"))

        # Create the new deduction object to store deduction data
        try:
            deductionObjects = Deduction.readAllDeductions(testQuery, DatabaseConnection.establishConnectionGUI(main_menu.makeConnectionString(
                self.server_connection_entry.get("1.0", 'end'), self.sql_db_entry.get("1.0", 'end-1c')), "No Pop Ups"))
            deductions = [deductionObjects[0].deductionValue, deductionObjects[1].deductionValue, deductionObjects[2].deductionValue, deductionObjects[3].deductionValue,
                          deductionObjects[4].deductionValue, deductionObjects[5].deductionValue, deductionObjects[6].deductionValue, deductionObjects[7].deductionValue]
        # If can not store deduction data, set the default value for each textbox
        except:
            deductions = [1.0, 1.0, 2.0, 1.0, 1.0, 1.0, 1.0, 2.0]

        # Print out the deduction data
        print(deductions)

        # Create a new window for deduction page GUI
        self.new_window = tk.Toplevel(self.top)
        self.new_window.geometry("698x665+700+199")
        self.new_window.minsize(120, 1)
        self.new_window.maxsize(1924, 1061)
        self.new_window.resizable(1, 1)
        self.new_window.title("Deduction Test Query")
        self.new_window.configure(background="#ffffff")

        # Create the header label for the deduction window
        self.header_label_new_window = tk.Label(self.new_window, bg="white")
        self.header_label_new_window.place(
            relx=0.0, rely=0.0, relheight=0.3, relwidth=1.0)

        # Create the canvas at the top of GUI (inside header label)
        self.header_canvas_new_window = tk.Canvas(self.header_label_new_window)
        self.header_canvas_new_window.place(
            relx=0.0, rely=0.0, relheight=0.75, relwidth=1.0)
        self.header_canvas_new_window.configure(background="#0052A0")
        self.header_canvas_new_window.configure(borderwidth="2")
        self.header_canvas_new_window.configure(insertbackground="black")
        self.header_canvas_new_window.configure(relief="ridge")
        self.header_canvas_new_window.configure(selectbackground="blue")
        self.header_canvas_new_window.configure(selectforeground="white")

        # Create the main canvas for deduction functionality
        self.deduction_canvas = tk.Canvas(self.new_window, bg="white")
        self.deduction_canvas.place(
            relx=0.0, rely=0.3, relheight=1, relwidth=1)

        # Create Deduction Test Query title
        self.deduction_header_label = tk.Label(self.deduction_canvas)
        self.deduction_header_label.place(
            relx=0.043, rely=0.0, relheight=0.075, relwidth=0.914)
        self.deduction_header_label.configure(background="#0052A0")
        self.deduction_header_label.configure(
            font="-family {Segoe UI} -size 20 -weight bold")
        self.deduction_header_label.configure(foreground="#ffffff")
        self.deduction_header_label.configure(text='''Deduction Test Query''')

        # Create the canvas for all requirement on deduction
        self.requirement_deduction_canvas = tk.Canvas(
            self.deduction_canvas, bg="white")
        self.requirement_deduction_canvas.place(
            relx=0.043, rely=0.1, relheight=0.6, relwidth=0.914)

        # Incorrect column label
        self.incorrect_column_label = tk.Label(
            self.requirement_deduction_canvas)
        self.incorrect_column_label.place(
            relx=0.03, rely=0.05, relheight=0.05, relwidth=0.5)
        self.incorrect_column_label.configure(background="white")
        self.incorrect_column_label.configure(background="#ffffff")
        self.incorrect_column_label.configure(
            font="-family {Segoe UI Historic} -size 11")
        self.incorrect_column_label.configure(foreground="#000000")
        self.incorrect_column_label.configure(
            text='''Query returned incorrect number of columns:''')

        # Incorrect column textbox
        self.incorrect_column_entry = tk.Text(
            self.requirement_deduction_canvas)
        self.incorrect_column_entry.insert(END, str(deductions[0]))
        self.incorrect_column_entry.place(
            relx=0.7, rely=0.05, relheight=0.06, relwidth=0.12)
        self.incorrect_column_entry.configure(background="white")
        self.incorrect_column_entry.configure(font="TkFixedFont")
        self.incorrect_column_entry.configure(foreground="#000000")
        self.incorrect_column_entry.configure(insertbackground="black")

        # Incorrect column point label
        self.incorrect_column_label_point = tk.Label(
            self.requirement_deduction_canvas)
        self.incorrect_column_label_point.place(
            relx=0.85, rely=0.05, relheight=0.05, relwidth=0.1)
        self.incorrect_column_label_point.configure(background="white")
        self.incorrect_column_label_point.configure(background="#ffffff")
        self.incorrect_column_label_point.configure(
            font="-family {Segoe UI Historic} -size 11")
        self.incorrect_column_label_point.configure(foreground="#000000")
        self.incorrect_column_label_point.configure(text='''point(s)''')

        # Incorrect row label
        self.incorrect_row_label = tk.Label(self.requirement_deduction_canvas)
        self.incorrect_row_label.place(
            relx=0.03, rely=0.15, relheight=0.05, relwidth=0.5)
        self.incorrect_row_label.configure(background="white")
        self.incorrect_row_label.configure(background="#ffffff")
        self.incorrect_row_label.configure(
            font="-family {Segoe UI Historic} -size 11")
        self.incorrect_row_label.configure(foreground="#000000")
        self.incorrect_row_label.configure(
            text='''Query returned incorrect number of rows:''')

        # Incorrect row textbox
        self.incorrect_row_entry = tk.Text(self.requirement_deduction_canvas)
        self.incorrect_row_entry.insert(END, str(deductions[1]))
        self.incorrect_row_entry.place(
            relx=0.7, rely=0.15, relheight=0.06, relwidth=0.12)
        self.incorrect_row_entry.configure(background="white")
        self.incorrect_row_entry.configure(font="TkFixedFont")
        self.incorrect_row_entry.configure(foreground="#000000")
        self.incorrect_row_entry.configure(insertbackground="black")

        # Incorrect row point label
        self.incorrect_row_label_point = tk.Label(
            self.requirement_deduction_canvas)
        self.incorrect_row_label_point.place(
            relx=0.85, rely=0.15, relheight=0.05, relwidth=0.1)
        self.incorrect_row_label_point.configure(background="white")
        self.incorrect_row_label_point.configure(background="#ffffff")
        self.incorrect_row_label_point.configure(
            font="-family {Segoe UI Historic} -size 11")
        self.incorrect_row_label_point.configure(foreground="#000000")
        self.incorrect_row_label_point.configure(text='''point(s)''')

        # Incorrect value label
        self.incorrect_value_label = tk.Label(
            self.requirement_deduction_canvas)
        self.incorrect_value_label.place(
            relx=0.03, rely=0.25, relheight=0.05, relwidth=0.5)
        self.incorrect_value_label.configure(background="white")
        self.incorrect_value_label.configure(background="#ffffff")
        self.incorrect_value_label.configure(
            font="-family {Segoe UI Historic} -size 11")
        self.incorrect_value_label.configure(foreground="#000000")
        self.incorrect_value_label.configure(
            text='''Query returned incorrect values:''')

        # Incorrect value textbox
        self.incorrect_value_entry = tk.Text(self.requirement_deduction_canvas)
        self.incorrect_value_entry.insert(END, str(deductions[2]))
        self.incorrect_value_entry.place(
            relx=0.7, rely=0.25, relheight=0.06, relwidth=0.12)
        self.incorrect_value_entry.configure(background="white")
        self.incorrect_value_entry.configure(font="TkFixedFont")
        self.incorrect_value_entry.configure(foreground="#000000")
        self.incorrect_value_entry.configure(insertbackground="black")

        # Incorrect value point label
        self.incorrect_value_label_point = tk.Label(
            self.requirement_deduction_canvas)
        self.incorrect_value_label_point.place(
            relx=0.85, rely=0.25, relheight=0.05, relwidth=0.1)
        self.incorrect_value_label_point.configure(background="white")
        self.incorrect_value_label_point.configure(background="#ffffff")
        self.incorrect_value_label_point.configure(
            font="-family {Segoe UI Historic} -size 11")
        self.incorrect_value_label_point.configure(foreground="#000000")
        self.incorrect_value_label_point.configure(text='''point(s)''')

        # Incorrect order column label
        self.incorrect_order_column_label = tk.Label(
            self.requirement_deduction_canvas)
        self.incorrect_order_column_label.place(
            relx=0.03, rely=0.35, relheight=0.05, relwidth=0.5)
        self.incorrect_order_column_label.configure(background="white")
        self.incorrect_order_column_label.configure(background="#ffffff")
        self.incorrect_order_column_label.configure(
            font="-family {Segoe UI Historic} -size 11")
        self.incorrect_order_column_label.configure(foreground="#000000")
        self.incorrect_order_column_label.configure(
            text='''Query returned incorrect order of columns:''')

        # Incorrect order column textbox
        self.incorrect_order_column_entry = tk.Text(
            self.requirement_deduction_canvas)
        self.incorrect_order_column_entry.insert(END, str(deductions[3]))
        self.incorrect_order_column_entry.place(
            relx=0.7, rely=0.35, relheight=0.06, relwidth=0.12)
        self.incorrect_order_column_entry.configure(background="white")
        self.incorrect_order_column_entry.configure(font="TkFixedFont")
        self.incorrect_order_column_entry.configure(foreground="#000000")
        self.incorrect_order_column_entry.configure(insertbackground="black")

        # Incorrect order column point label
        self.incorrect_order_column_label_point = tk.Label(
            self.requirement_deduction_canvas)
        self.incorrect_order_column_label_point.place(
            relx=0.85, rely=0.35, relheight=0.05, relwidth=0.1)
        self.incorrect_order_column_label_point.configure(background="white")
        self.incorrect_order_column_label_point.configure(background="#ffffff")
        self.incorrect_order_column_label_point.configure(
            font="-family {Segoe UI Historic} -size 11")
        self.incorrect_order_column_label_point.configure(foreground="#000000")
        self.incorrect_order_column_label_point.configure(text='''point(s)''')

        # Incorrect order of row label
        self.incorrect_order_row_label = tk.Label(
            self.requirement_deduction_canvas)
        self.incorrect_order_row_label.place(
            relx=0.03, rely=0.45, relheight=0.05, relwidth=0.5)
        self.incorrect_order_row_label.configure(background="white")
        self.incorrect_order_row_label.configure(background="#ffffff")
        self.incorrect_order_row_label.configure(
            font="-family {Segoe UI Historic} -size 11")
        self.incorrect_order_row_label.configure(foreground="#000000")
        self.incorrect_order_row_label.configure(
            text='''Query returned incorrect order of rows:''')

        # Incorrect order of row textbox
        self.incorrect_order_row_entry = tk.Text(
            self.requirement_deduction_canvas)
        self.incorrect_order_row_entry.insert(END, str(deductions[4]))
        self.incorrect_order_row_entry.place(
            relx=0.7, rely=0.45, relheight=0.06, relwidth=0.12)
        self.incorrect_order_row_entry.configure(background="white")
        self.incorrect_order_row_entry.configure(font="TkFixedFont")
        self.incorrect_order_row_entry.configure(foreground="#000000")
        self.incorrect_order_row_entry.configure(insertbackground="black")

        # Incorrect order of row point label
        self.incorrect_order_row_label_point = tk.Label(
            self.requirement_deduction_canvas)
        self.incorrect_order_row_label_point.place(
            relx=0.85, rely=0.45, relheight=0.05, relwidth=0.1)
        self.incorrect_order_row_label_point.configure(background="white")
        self.incorrect_order_row_label_point.configure(background="#ffffff")
        self.incorrect_order_row_label_point.configure(
            font="-family {Segoe UI Historic} -size 11")
        self.incorrect_order_row_label_point.configure(foreground="#000000")
        self.incorrect_order_row_label_point.configure(text='''point(s)''')

        # Executed inefficiently label
        self.executed_inefficiently_label = tk.Label(
            self.requirement_deduction_canvas)
        self.executed_inefficiently_label.place(
            relx=0.03, rely=0.55, relheight=0.05, relwidth=0.5)
        self.executed_inefficiently_label.configure(background="white")
        self.executed_inefficiently_label.configure(background="#ffffff")
        self.executed_inefficiently_label.configure(
            font="-family {Segoe UI Historic} -size 11")
        self.executed_inefficiently_label.configure(foreground="#000000")
        self.executed_inefficiently_label.configure(
            text='''Query executed inefficiently:''')

        # Executed inefficiently textbox
        self.executed_inefficiently_entry = tk.Text(
            self.requirement_deduction_canvas)
        self.executed_inefficiently_entry.insert(END, str(deductions[5]))
        self.executed_inefficiently_entry.place(
            relx=0.7, rely=0.55, relheight=0.06, relwidth=0.12)
        self.executed_inefficiently_entry.configure(background="white")
        self.executed_inefficiently_entry.configure(font="TkFixedFont")
        self.executed_inefficiently_entry.configure(foreground="#000000")
        self.executed_inefficiently_entry.configure(insertbackground="black")

        # Executed inefficiently point label
        self.executed_inefficiently_label_point = tk.Label(
            self.requirement_deduction_canvas)
        self.executed_inefficiently_label_point.place(
            relx=0.85, rely=0.55, relheight=0.05, relwidth=0.1)
        self.executed_inefficiently_label_point.configure(background="white")
        self.executed_inefficiently_label_point.configure(background="#ffffff")
        self.executed_inefficiently_label_point.configure(
            font="-family {Segoe UI Historic} -size 11")
        self.executed_inefficiently_label_point.configure(foreground="#000000")
        self.executed_inefficiently_label_point.configure(text='''point(s)''')

        # Incorrect join label
        self.incorrect_join_label = tk.Label(self.requirement_deduction_canvas)
        self.incorrect_join_label.place(
            relx=0.03, rely=0.65, relheight=0.05, relwidth=0.5)
        self.incorrect_join_label.configure(background="white")
        self.incorrect_join_label.configure(background="#ffffff")
        self.incorrect_join_label.configure(
            font="-family {Segoe UI Historic} -size 11")
        self.incorrect_join_label.configure(foreground="#000000")
        self.incorrect_join_label.configure(
            text='''Query used incorrect join:''')

        # Incorrect join textbox
        self.incorrect_join_entry = tk.Text(self.requirement_deduction_canvas)
        self.incorrect_join_entry.insert(END, str(deductions[6]))
        self.incorrect_join_entry.place(
            relx=0.7, rely=0.65, relheight=0.06, relwidth=0.12)
        self.incorrect_join_entry.configure(background="white")
        self.incorrect_join_entry.configure(font="TkFixedFont")
        self.incorrect_join_entry.configure(foreground="#000000")
        self.incorrect_join_entry.configure(insertbackground="black")

        # Incorrect join point label
        self.incorrect_join_label_point = tk.Label(
            self.requirement_deduction_canvas)
        self.incorrect_join_label_point.place(
            relx=0.85, rely=0.65, relheight=0.05, relwidth=0.1)
        self.incorrect_join_label_point.configure(background="white")
        self.incorrect_join_label_point.configure(background="#ffffff")
        self.incorrect_join_label_point.configure(
            font="-family {Segoe UI Historic} -size 11")
        self.incorrect_join_label_point.configure(foreground="#000000")
        self.incorrect_join_label_point.configure(text='''point(s)''')

        # Incorrect used TOP label
        self.incorrect_used_TOP_label = tk.Label(
            self.requirement_deduction_canvas)
        self.incorrect_used_TOP_label.place(
            relx=0.03, rely=0.75, relheight=0.05, relwidth=0.5)
        self.incorrect_used_TOP_label.configure(background="white")
        self.incorrect_used_TOP_label.configure(background="#ffffff")
        self.incorrect_used_TOP_label.configure(
            font="-family {Segoe UI Historic} -size 11")
        self.incorrect_used_TOP_label.configure(foreground="#000000")
        self.incorrect_used_TOP_label.configure(
            text='''Query incorrectly used TOP:''')

        # Incorrect used TOP textbox
        self.incorrect_used_TOP_entry = tk.Text(
            self.requirement_deduction_canvas)
        self.incorrect_used_TOP_entry.insert(END, str(deductions[7]))
        self.incorrect_used_TOP_entry.place(
            relx=0.7, rely=0.75, relheight=0.06, relwidth=0.12)
        self.incorrect_used_TOP_entry.configure(background="white")
        self.incorrect_used_TOP_entry.configure(font="TkFixedFont")
        self.incorrect_used_TOP_entry.configure(foreground="#000000")
        self.incorrect_used_TOP_entry.configure(insertbackground="black")

        # Incorrect used TOP point label
        self.incorrect_used_TOP_label_point = tk.Label(
            self.requirement_deduction_canvas)
        self.incorrect_used_TOP_label_point.place(
            relx=0.85, rely=0.75, relheight=0.05, relwidth=0.1)
        self.incorrect_used_TOP_label_point.configure(background="white")
        self.incorrect_used_TOP_label_point.configure(background="#ffffff")
        self.incorrect_used_TOP_label_point.configure(
            font="-family {Segoe UI Historic} -size 11")
        self.incorrect_used_TOP_label_point.configure(foreground="#000000")
        self.incorrect_used_TOP_label_point.configure(text='''point(s)''')

        # Save button for deduction window
        self.deduction_save_button = tk.Button(
            self.requirement_deduction_canvas)
        self.deduction_save_button.place(
            relx=0.8, rely=0.86, relheight=0.1, relwidth=0.14)
        self.deduction_save_button.configure(activebackground="white")
        self.deduction_save_button.configure(activeforeground="#000000")
        self.deduction_save_button.configure(background="#0052A0")
        self.deduction_save_button.configure(foreground="white")
        self.deduction_save_button.configure(pady="0")
        self.deduction_save_button.configure(text='''Save''')
        self.deduction_save_button.configure(command=lambda: self.deduction_message(selectedQuestion, self.incorrect_column_entry.get("1.0", 'end-1c'), self.incorrect_row_entry.get("1.0", 'end-1c'), self.incorrect_value_entry.get("1.0", 'end-1c'), self.incorrect_order_column_entry.get(
            "1.0", 'end-1c'), self.incorrect_order_row_entry.get("1.0", 'end-1c'), self.executed_inefficiently_entry.get("1.0", 'end-1c'), self.incorrect_join_entry.get("1.0", 'end-1c'), self.incorrect_used_TOP_entry.get("1.0", 'end-1c')))

    # Function that appends the database name into the server connection string
    @staticmethod
    def makeConnectionString(serverString, databaseString):
        index = 0
        stringOne = ""
        stringTwo = ""
        finalString = ""
        for char in serverString:
            if char == "=" and serverString[index + 1] == ";":
                stringOne = serverString[0:index+1]
                stringTwo = serverString[index+1:]
                break
            index += 1
        finalString = stringOne + databaseString + stringTwo
        print(finalString)
        return finalString

    # Function to turn on main menu
    def turn_on_main_menu(self):
        # Forget unused canvas
        self.input_canvas.place_forget()
        self.select_canvas.place_forget()
        self.test_query_management_label.place_forget()
        self.student_canvas.place_forget()
        self.main_SVT_canvas.place_forget()
        self.graph_SVT_canvas.place_forget()
        self.export_SVT_canvas.place_forget()
        self.generate_SVT_canvas.place_forget()
        self.database_canvas.place_forget()

        # Make the Main Menu label appear
        self.main_menu_label.place(relx=0.0, rely=0.3, relheight=1, relwidth=1)

    # Function to turn on test query menu
    def turn_on_test_query_menu(self):
        # forget unused canvas
        self.main_menu_label.place_forget()
        self.select_canvas.place_forget()
        self.input_canvas.place_forget()
        self.student_canvas.place_forget()
        self.main_SVT_canvas.place_forget()
        self.graph_SVT_canvas.place_forget()
        self.export_SVT_canvas.place_forget()
        self.generate_SVT_canvas.place_forget()
        self.database_canvas.place_forget()

        # Make the Test Query Management label appear
        self.test_query_management_label.place(
            relx=0.0, rely=0.3, relheight=1, relwidth=1)

    # Function to turn on input query functionality
    def turn_on_input_query(self):
        # Forget unused canvas
        self.main_menu_label.place_forget()
        self.select_canvas.place_forget()
        self.test_query_management_label.place_forget()
        self.student_canvas.place_forget()
        self.main_SVT_canvas.place_forget()
        self.graph_SVT_canvas.place_forget()
        self.export_SVT_canvas.place_forget()
        self.generate_SVT_canvas.place_forget()
        self.database_canvas.place_forget()

        # Make the Input Questions/Test Queries label appear
        self.input_canvas.place(relx=0.0, rely=0.3, relheight=1, relwidth=1)

    # Function to turn on select query menu
    def turn_on_select_query(self):
        # Forget unused canvas
        self.main_menu_label.place_forget()
        self.test_query_management_label.place_forget()
        self.input_canvas.place_forget()
        self.student_canvas.place_forget()
        self.main_SVT_canvas.place_forget()
        self.graph_SVT_canvas.place_forget()
        self.export_SVT_canvas.place_forget()
        self.generate_SVT_canvas.place_forget()
        self.database_canvas.place_forget()
        self.select_area_canvas.place_forget()

        # Make the Select Assignment Questions canvas appear
        self.select_canvas.place(relx=0.0, rely=0.3, relheight=1, relwidth=1)

    # Function to turn on Student Query menu
    def turn_on_student_query_menu(self):
        # Forget unused canvas
        self.main_menu_label.place_forget()
        self.test_query_management_label.place_forget()
        self.input_canvas.place_forget()
        self.select_canvas.place_forget()
        self.main_SVT_canvas.place_forget()
        self.graph_SVT_canvas.place_forget()
        self.export_SVT_canvas.place_forget()
        self.generate_SVT_canvas.place_forget()
        self.database_canvas.place_forget()
        self.selected_canvas.place_forget()

        # Make the Student Query canvas appear
        self.student_canvas.place(relx=0.0, rely=0.3, relheight=1, relwidth=1)

    # Function to turn on Student vs. Test query menu
    def turn_on_SVT_query_menu(self):
        # Forget unused canvas
        self.main_menu_label.place_forget()
        self.test_query_management_label.place_forget()
        self.input_canvas.place_forget()
        self.select_canvas.place_forget()
        self.student_canvas.place_forget()
        self.graph_SVT_canvas.place_forget()
        self.export_SVT_canvas.place_forget()
        self.generate_SVT_canvas.place_forget()
        self.database_canvas.place_forget()
        self.SVT_selected_student_query_canvas.place_forget()
        self.search_SVT_selected_student_query_canvas.place_forget()

        # Make the first page of Student vs. Test Query canvas appear
        self.SVT_canvas.place(relx=0.0, rely=0, relheight=1, relwidth=1)
        self.main_SVT_canvas.place(relx=0.0, rely=0.3, relheight=1, relwidth=1)

    # Function on_configure to select the scroll region for the scrollbar
    def on_configure(self, event=None):
        self.canvas_query.configure(scrollregion=self.canvas_query.bbox('all'))

    # Function on_configure to select the scroll region for the scrollbar (Select Assignment Questions table)
    def on_configure_findQues(self, event=None):
        self.select_table_canvas.configure(
            scrollregion=self.select_table_canvas.bbox('all'))

    # Function for setting scroll bar (speed) (Select Assignment Questions table)
    def on_mouse_scroll_findQues(self, event):
        self.select_table_canvas.yview_scroll(-1 *
                                              int((event.delta / 110)), "units")

    # Function for setting scroll bar (speed)
    def scrolling(self, event):
        self.canvas_query.yview_scroll(-1 * int((event.delta / 110)), "units")

    # Function to turn on generate menu
    def turn_on_generate(self):
        # Forget unused canvas
        self.graph_SVT_canvas.place_forget()
        self.generate_SVT_canvas.place_forget()
        self.main_menu_label.place_forget()
        self.test_query_management_label.place_forget()
        self.input_canvas.place_forget()
        self.select_canvas.place_forget()
        self.student_canvas.place_forget()
        self.graph_SVT_canvas.place_forget()
        self.export_SVT_canvas.place_forget()
        self.generate_SVT_canvas.place_forget()
        self.database_canvas.place_forget()

        # Make the first page of Student vs. Test Query canvas appear
        self.SVT_canvas.place(relx=0.0, rely=0, relheight=1, relwidth=1)
        self.main_SVT_canvas.place(relx=0.0, rely=0.3, relheight=1, relwidth=1)

        # Make the Student Vs. Test Query generate table canvas appear
        self.SVT_selected_student_query_canvas.place(
            relx=0.040, rely=0.1, relheight=0.494, relwidth=0.92)
        self.search_SVT_selected_student_query_canvas.place_forget()

    # Function to turn on Graph menu
    def turn_on_graph(self):
        # Forget unused canvas
        self.generate_SVT_canvas.place_forget()
        self.SVT_canvas.place_forget()
        self.export_SVT_canvas.place_forget()
        self.student_graph_canvas.place_forget()
        self.question_graph_canvas.place_forget()

        # Make the Graph canvas appear
        self.graph_SVT_types_canvas.place(
            relx=0.043, rely=0.08, relheight=0.62, relwidth=0.914)
        self.graph_SVT_canvas.place(relx=0.0, rely=0, relheight=1, relwidth=1)

    # Make the Student Vs. Test Query search table canvas appear
    def turn_on_search_treeview(self):
        self.SVT_selected_student_query_canvas.place_forget()
        self.search_SVT_selected_student_query_canvas.place(
            relx=0.040, rely=0.1, relheight=0.494, relwidth=0.92)

    # Function to turn on Setting page
    def turn_on_database(self):
        # Forget unused canvas
        self.main_menu_label.place_forget()
        self.test_query_management_label.place_forget()
        self.input_canvas.place_forget()
        self.select_canvas.place_forget()
        self.main_SVT_canvas.place_forget()
        self.graph_SVT_canvas.place_forget()
        self.export_SVT_canvas.place_forget()
        self.generate_SVT_canvas.place_forget()
        self.student_canvas.place_forget()

        # Make the Student Query canvas appear
        self.database_canvas.place(relx=0.0, rely=0.3, relheight=1, relwidth=1)

    # Function to input SQL query
    def input_SQL_query(self, difficuiltySelection):
        response = messagebox.askquestion(
            title='Input Assignment Question', message='Do you want to submit this question/testquery?')
        if response == 'yes':
            # Gets the difficuiltyId (from the database) associated with the user's difficuilty selection on the dropdown
            difficultyId = Difficulty.getDifficultyId(difficuiltySelection, DatabaseConnection.establishConnectionGUI(
                main_menu.makeConnectionString(self.server_connection_entry.get("1.0", 'end'), self.sql_db_entry.get("1.0", 'end-1c')), "No Pop Ups"))

            # Creates a question object from the user's input
            question = Question(Question.makeStorable(
                self.question_entry.get("1.0", 'end-1c')), difficultyId)

            # Stores the question in the database
            question.storeQuestion(DatabaseConnection.establishConnectionGUI(main_menu.makeConnectionString(
                self.server_connection_entry.get("1.0", 'end'), self.sql_db_entry.get("1.0", 'end-1c')), "No Pop Ups"))

            # Creates a query object from the user's input
            query = Query(question.questionId, Query.makeStorable(
                self.query_entry.get("1.0", 'end-1c')), 10.0)

            storeError = False
            # Stores the query in the database
            try:
                query.storeQuery(DatabaseConnection.establishConnectionGUI(main_menu.makeConnectionString(
                    self.server_connection_entry.get("1.0", 'end'), self.sql_db_entry.get("1.0", 'end-1c')), "No Pop Ups"))
                Deduction.populateDeductions(query, DatabaseConnection.establishConnectionGUI(main_menu.makeConnectionString(
                    self.server_connection_entry.get("1.0", 'end'), self.sql_db_entry.get("1.0", 'end-1c')), "No Pop Ups"))
            except:
                storeError = True

            if storeError == False:
                messagebox.showinfo(
                    title='Question saved', message='Assignment question has been saved successfully!')
                self.query_entry.delete("1.0", "end")
                self.question_entry.delete("1.0", "end")
            elif storeError == True:
                messagebox.showinfo(
                    title='Queries not saved', message='Assignment question did not save successfully, try again!')

    # Function to return select SQL query message
    def select_SQL_query_message(self):
        response = messagebox.askquestion(
            title='Select SQL queries', message='Do you want to select these queries?')
        if response == 'yes':
            messagebox.showinfo(
                title='Queries selected', message='Queries have been selected successfully!')

    # Student read in GUI functionality
    def upload_SQL(self):
        response = messagebox.askquestion(
            title='Upload SQL files', message='Do you want to upload these files?')
        if response == 'yes':
            folders = os.listdir('./Temporary Student File Directory')
            print(folders)
            for folder in folders:
                studentFiles = []
                if folder != '.DS_Store' and folder != '__MACOSX':
                    studentFiles = os.listdir(
                        './Temporary Student File Directory/' + folder)
                    print(studentFiles)
                    for studentFile in studentFiles:
                        if studentFile != '.DS_Store':
                            try:
                                mark = Query.readIn('./Temporary Student File Directory/' + folder + '/' + studentFile, DatabaseConnection.establishConnectionGUI(
                                    main_menu.makeConnectionString(self.server_connection_entry.get("1.0", 'end'), self.sql_db_entry.get("1.0", 'end-1c')), "No Pop Up"))
                                mark.storeMarks(DatabaseConnection.establishConnectionGUI(main_menu.makeConnectionString(
                                    self.server_connection_entry.get("1.0", 'end'), self.sql_db_entry.get("1.0", 'end-1c')), "No Pop Up"))
                            except:
                                "There was an error reading in the files. Make sure you have established connection to the SQL Checker database first"
                    messagebox.showinfo(
                        title='Files uploaded', message='Files have been uploaded successfully!')
                    self.add_table_student_query()
                    self.selected_canvas.place(
                        relx=0.040, rely=0.4, relheight=0.28, relwidth=0.8)

    # Function to return message when user try to save a SQL file containing students' queries
    def save_SQL_files_of_student_message(self):
        response = messagebox.askquestion(
            title="Save students'SQL files", message='Do you want to save these files?')
        if response == 'yes':
            messagebox.showinfo(title='Files saved',
                                message='Files have been saved successfully!')

    # Function to return message when user try to export students' result
    def export_result_message(self):
        response = messagebox.askquestion(title='Exports student results',
                                          message="Do you want to export these students'result?")
        if response == 'yes':
            filePath = self.export_files()
            Marks.exportToCSV(filePath, DatabaseConnection.establishConnectionGUI(main_menu.makeConnectionString(
                self.server_connection_entry.get("1.0", 'end'), self.sql_db_entry.get("1.0", 'end-1c')), "No Pop Up"))

    # Function to return message when user try to save a deduction format a assingmnet question
    def deduction_message(self, question, columnValue, rowValue, valueValue, columnOrderValue, rowOrderValue, executionValue, joinValue, topValue):
        deductionValues = [columnValue, rowValue, valueValue,
                           columnOrderValue, rowOrderValue, executionValue, joinValue, topValue]
        testQuery = Query.retrieveTestQueryFromQuestionId(question[0], DatabaseConnection.establishConnectionGUI(
            main_menu.makeConnectionString(self.server_connection_entry.get("1.0", 'end'), self.sql_db_entry.get("1.0", 'end-1c')), "No Pop Ups"))
        response = messagebox.askquestion(title='Save deduction query',
                                          message="Do you want to save this deduction query?")
        if response == 'yes':
            Deduction.saveUpdatedDeductionsGUI(testQuery, deductionValues, DatabaseConnection.establishConnectionGUI(
                main_menu.makeConnectionString(self.server_connection_entry.get("1.0", 'end'), self.sql_db_entry.get("1.0", 'end-1c')), "No Pop Ups"))
            messagebox.showinfo(title='Deduction query saved',
                                message='The deduction query been saved successfully')
            self.new_window.destroy()

    # Makes the treeview for the student file read in page
    def add_table_student_query(self, event=None):
        # Treeview for select query table
        select_column = ('#studentID', '#questionno', '#studentquery')

        self.select_tree = ttk.Treeview(
            self.selected_canvas, columns=select_column, show='headings')
        self.select_tree.place_forget()

        # Define headings
        self.select_tree.heading('#studentID', text='Username')
        self.select_tree.heading('#questionno', text='Question No')
        self.select_tree.heading('#studentquery', text='Student Query')

        # Create a student query array
        student_query = []

        # Get the student queries' data from database
        studentQueries = Query.readAllStudentQueries(DatabaseConnection.establishConnectionGUI(main_menu.makeConnectionString(
            self.server_connection_entry.get("1.0", 'end'), self.sql_db_entry.get("1.0", 'end-1c')), "No Pop Ups"))
        students = User.getAllUsers(DatabaseConnection.establishConnectionGUI(main_menu.makeConnectionString(
            self.server_connection_entry.get("1.0", 'end'), self.sql_db_entry.get("1.0", 'end-1c')), "No Pop Ups"))
        assignmentQuestions = AssignmentQuestion.getAllAssignmentQuestions(DatabaseConnection.establishConnectionGUI(
            main_menu.makeConnectionString(self.server_connection_entry.get("1.0", 'end'), self.sql_db_entry.get("1.0", 'end-1c')), "No Pop Ups"))

        # Add data to the exist array for student queries' data
        for student in students:
            marksForStudent = Marks.getMarksForUserId(DatabaseConnection.establishConnectionGUI(main_menu.makeConnectionString(
                self.server_connection_entry.get("1.0", 'end'), self.sql_db_entry.get("1.0", 'end-1c')), "No Pop Ups"), student.UserId)
            for mark in marksForStudent:
                for studentQuery in studentQueries:
                    if mark.queryId == studentQuery.queryId:
                        for assignmentQuestion in assignmentQuestions:
                            if studentQuery.questionId == assignmentQuestion.questionId:
                                storedQuestion = assignmentQuestion
                        newTableRow = [
                            student.UserName, storedQuestion.questionNumber, studentQuery.sql]
                        student_query.append(newTableRow)

        # Insert data from student queries' data array to the treeview
        for query in student_query:
            self.select_tree.insert('', tk.END, values=query)

        # Vertical scrollbar for treeview
        self.select_query_yscrollbar = Scrollbar(
            self.selected_canvas, orient=VERTICAL)
        self.select_query_yscrollbar.grid(row=0, column=1, sticky=(N, S, W, E))
        self.select_query_yscrollbar.config(command=self.select_tree.yview)
        self.select_tree.config(
            yscrollcommand=self.select_query_yscrollbar.set)

        # Horizontal scrollbar for treeview
        self.select_query_xscrollbar = Scrollbar(
            self.selected_canvas, orient=HORIZONTAL)
        self.select_query_xscrollbar.grid(row=1, column=0, sticky=(N, S, W, E))
        self.select_tree.config(
            xscrollcommand=self.select_query_xscrollbar.set)
        self.select_query_xscrollbar.config(command=self.select_tree.xview)

        # Make resizable treeview
        self.selected_canvas.grid_rowconfigure(0, weight=1)
        self.selected_canvas.grid_columnconfigure(0, weight=1)
        self.select_tree.grid(row=0, column=0, sticky='nsew')

    # Function to clear the table after change the filter search
    def clear_select_table_fucntion(self):
        self.second_frame_find_ques.delete(0, 'end')
        self.add_table_select(self.search_variable.get()[2])

    # Function to add the grid table for Select Assignment Questions table
    def add_table_select(self, difflevel):
        self.select_table_canvas.delete(ALL)
        self.num_of_row = 0
        self.select_area_canvas.place(
            relx=0.04, rely=0.35, relheight=0.27, relwidth=0.92)

        first_row = ['Question ID', 'Question',
                     'Difficulty', 'Deduction', 'Select']
        self.select_table_canvas.configure(bg="white")

        # Heading row of the Select Assignment Questions table

        # Question ID heading
        first_quesID_lab = tk.Label(
            self.select_area_canvas, text=first_row[0], bg="white", relief=RIDGE)
        first_quesID_lab.configure(
            font="-family {Segoe UI Historic} -size 12 -weight bold")
        first_quesID_lab.place(relx=0.0015, rely=0,
                               relheight=0.2, relwidth=0.2)

        # Question heading
        first_ques_lab = tk.Label(
            self.select_area_canvas, text=first_row[1], bg="white", relief=RIDGE)
        first_ques_lab.configure(
            font="-family {Segoe UI Historic} -size 12 -weight bold")
        first_ques_lab.place(relx=0.2015, rely=0,
                             relheight=0.2, relwidth=0.4455)

        # Difficulty heading
        first_difficulty_lab = tk.Label(
            self.select_area_canvas, text=first_row[2], bg="white", relief=RIDGE)
        first_difficulty_lab.configure(
            font="-family {Segoe UI Historic} -size 12 -weight bold")
        first_difficulty_lab.place(
            relx=0.647, rely=0, relheight=0.2, relwidth=0.1)

        # Deduction heading
        first_deduction_lab = tk.Label(
            self.select_area_canvas, text=first_row[3], bg="white", relief=RIDGE)
        first_deduction_lab.configure(
            font="-family {Segoe UI Historic} -size 12 -weight bold")
        first_deduction_lab.place(
            relx=0.747, rely=0, relheight=0.2, relwidth=0.1775)

        # Select heading
        first_select_lab = tk.Label(
            self.select_area_canvas, text=first_row[4], bg="white", relief=RIDGE)
        first_select_lab.configure(
            font="-family {Segoe UI Historic} -size 12 -weight bold")
        first_select_lab.place(relx=0.9245, rely=0,
                               relheight=0.2, relwidth=0.076)

        # Vertical scrollbar for treeview
        self.select_yscrollbar = Scrollbar(
            self.select_table_canvas, orient=VERTICAL)
        self.select_yscrollbar.place(
            relx=0.95, rely=0.39, relheight=0.2, relwidth=0.02)
        self.select_yscrollbar.config(command=self.select_table_canvas.yview)
        self.select_table_canvas.config(
            yscrollcommand=self.select_yscrollbar.set)

        # horizontal scrollbar for treeview
        # self.select_xscrollbar = Scrollbar(self.select_table_canvas, orient=HORIZONTAL)
        # self.select_xscrollbar.grid(row=1, column=0, sticky=(N, S, W, E))
        # self.select_table_canvas.config(xscrollcommand=self.select_xscrollbar.set)
        # self.select_xscrollbar.config(command=self.select_table_canvas.xview)

        # Assign the scroll function to the mousewheel to make the connection between mousewheel and scroll bar
        self.select_table_canvas.bind_all(
            "<MouseWheel>", self.on_mouse_scroll_findQues)
        
        # Create a new frame to store a new row for the Select Assignment Questions table
        self.second_frame_find_ques = tk.Frame(self.select_table_canvas)
        self.second_frame_find_ques.place(
            relx=0, rely=0, relheight=1, relwidth=1)
        self.select_table_canvas.create_window(
            0, 0, window=self.second_frame_find_ques)
        
        # Assign the scroll region for the new frame
        self.second_frame_find_ques.bind(
            '<Configure>', self.on_configure_findQues)

        # New array for store data from database
        select_labelRows = []
        # Get data from database for Select Assignment Questions table
        allQuestions = Question.readAllQuestions(DatabaseConnection.establishConnectionGUI(main_menu.makeConnectionString(
            self.server_connection_entry.get("1.0", 'end'), self.sql_db_entry.get("1.0", 'end-1c')), "No Pop Ups"))

        # Append data from database to the exist array
        for question in allQuestions:
            difficulty = Difficulty.getDifficultyFromId(question.difficultyId, DatabaseConnection.establishConnectionGUI(
                main_menu.makeConnectionString(self.server_connection_entry.get("1.0", 'end'), self.sql_db_entry.get("1.0", 'end-1c')), "No Pop Ups"))
            if int(difflevel) == int(difficulty.diffLevel):
                tableRow = [question.questionId,
                            question.question, difficulty.diffLevel]
                select_labelRows.append(tableRow)

        # Insert data from the select_labelRows array to the Select Assignment Questions table
        for row in select_labelRows:
            row_ques = FoundQuestion(self.second_frame_find_ques, row, self, self.num_of_row, select_labelRows, DatabaseConnection.establishConnectionGUI(
                main_menu.makeConnectionString(self.server_connection_entry.get("1.0", 'end'), self.sql_db_entry.get("1.0", 'end-1c')), "No Pop Ups"))
            self.num_of_row += 1
            row_ques.rePlace()

        # Place the Select Assignment Questions table
        self.select_table_canvas.place(
            relx=0, rely=0.2, relheight=0.7, relwidth=1)

    # Function to turn on question graph functionality canvas
    def turn_on_question_graph(self, connection):

        # Question ID dropdown for Question Graph function
        # Question ID array for the Question ID dropdown
        QUESTIONID = self.retrieveAssignmentQuestions(connection)
        global questionid_variable
        questionid_variable = StringVar(self.question_graph_canvas)
        # Default drowdown value
        questionid_variable.set(QUESTIONID[0])

        # GUI dropdown that allows the user to select the question ID they wish to select from (and the label next to it)
        input_questionid = tk.OptionMenu(
            self.question_graph_canvas, questionid_variable, *QUESTIONID)
        input_questionid.place(relx=0.2, rely=0.27, relheight=0.05, relwidth=0.2)

        # Forget unused canvas
        self.main_menu_label.place_forget()
        self.test_query_management_label.place_forget()
        self.input_canvas.place_forget()
        self.select_canvas.place_forget()
        self.main_SVT_canvas.place_forget()
        self.export_SVT_canvas.place_forget()
        self.generate_SVT_canvas.place_forget()
        self.student_canvas.place_forget()
        self.student_graph_canvas.place_forget()

        # Make the Student Query canvas appear
        self.main_SVT_canvas.place(relx=0.0, rely=0.3, relheight=1, relwidth=1)
        self.graph_SVT_canvas.place(relx=0.0, rely=0, relheight=1, relwidth=1)
        self.question_graph_canvas.place(
            relx=0, rely=0, relheight=1, relwidth=1)

    # Function to turn on student graph functionality canvas
    def turn_on_student_graph(self, connection):
        # Student ID dropdown for Student Graph function
        # Student ID array for the Student ID dropdown
        STUDENTID = self.retrieveStudents(connection)
        global studentid_variable 
        studentid_variable = StringVar(self.student_graph_canvas)
        # Default drowdown value
        studentid_variable.set(STUDENTID[0])

        # GUI dropdown that allows the user to select the student ID they wish to select from (and the label next to it)
        input_studentid = tk.OptionMenu(
            self.student_graph_canvas, studentid_variable, *STUDENTID)
        input_studentid.place(relx=0.15, rely=0.27, relheight=0.05, relwidth=0.2)

        # Forget unused canvas
        self.main_menu_label.place_forget()
        self.test_query_management_label.place_forget()
        self.input_canvas.place_forget()
        self.select_canvas.place_forget()
        self.main_SVT_canvas.place_forget()
        self.export_SVT_canvas.place_forget()
        self.generate_SVT_canvas.place_forget()
        self.student_canvas.place_forget()
        self.question_graph_canvas.place_forget()
        # Make the Student Query canvas appear
        self.main_SVT_canvas.place(relx=0.0, rely=0.3, relheight=1, relwidth=1)
        self.graph_SVT_canvas.place(relx=0.0, rely=0, relheight=1, relwidth=1)
        self.student_graph_canvas.place(
            relx=0, rely=0, relheight=1, relwidth=1)

    # Function to create the generate results table
    def generate_table(self, checkerConnection, dataConnection):
        # Treeview for generate_table
        # Gets all the test queries
        testQueries = Query.readAllTestQueries(checkerConnection)
        # Gets all the student queries
        studentQueries = Query.readAllStudentQueries(checkerConnection)
        # Compares all the student queries with all the test queries
        Query.compareAll(testQueries, studentQueries,
                         checkerConnection, dataConnection)
        # Gets all the assignment questions
        assignmentQuestions = AssignmentQuestion.getAllAssignmentQuestions(
            checkerConnection)
        print(assignmentQuestions)
        # Gets all the students
        students = User.getAllUsers(checkerConnection)
        print(students)
        # Compares all the test queries and student queries
        #Query.generateResultsGUI(checkerConnection, dataConnection)
        # The number of questions
        num_of_question = len(assignmentQuestions)
        # Selected_column
        selected_column = ['#studentID']
        for n in range(1, num_of_question + 1):
            selected_column.append((f'#{n}'))
            selected_column.append((f'#{n}'))

        self.selected_tree = ttk.Treeview(self.SVT_selected_student_query_canvas, columns=selected_column,
                                          show='headings')
        self.selected_tree.place(relx=0, rely=0, relheight=1, relwidth=1)

        # Define headings
        self.selected_tree.heading('#studentID', text='StudentID')
        index = 2
        for question in assignmentQuestions:
            self.selected_tree.heading(
                (f'#{index}'), text=(str(question.questionNumber)))
            self.selected_tree.heading((f'#{index + 1}'), text=("Feedback"))
            index += 2

        # Create the big array to store all studentGrade array
        students_grade = []
        index = 0
        # Create an array to store every data of a row in Generate table
        studentGrade = []

        # Get the data from database and add it to the exist array named studentGrade
        for student in students:
            studentGrade = []
            feedback = Query.retrievedQuestionNumberAndFeedback(
                student.UserId, checkerConnection)
            print(feedback)
            feedbackString = ""

            for record in feedback:
                feedbackString += str(record[0]) + ": " + str(record[1]) + "\n"

            studentGrade.append(student.UserName)
            marksForStudent = Marks.marksWithQNumForUser(
                checkerConnection, student.UserId)
            for question in assignmentQuestions:
                for mark in marksForStudent:
                    if question.questionNumber == mark[4]:
                        studentGrade.append(mark[3])
                for record in feedback:
                    if question.questionNumber == record[0]:
                        studentGrade.append(record[1])
            
            # Add data from all studentGrade array to the big array named students_grade
            students_grade.append(studentGrade)

        # Adding data from student_grade array to the treeview 
        for grade in students_grade:
            self.selected_tree.insert('', tk.END, values=grade)

        # Vertical scrollbar for treeview
        self.selected_yscrollbar = Scrollbar(
            self.SVT_selected_student_query_canvas, orient=VERTICAL)
        self.selected_yscrollbar.grid(row=0, column=1, sticky=(N, S, W, E))
        self.selected_yscrollbar.config(command=self.selected_tree.yview)
        self.selected_tree.config(yscrollcommand=self.selected_yscrollbar.set)

        # Horizontal scrollbar for treeview
        self.selected_xscrollbar = Scrollbar(
            self.SVT_selected_student_query_canvas, orient=HORIZONTAL)
        self.selected_xscrollbar.grid(row=1, column=0, sticky=(N, S, W, E))
        self.selected_tree.config(xscrollcommand=self.selected_xscrollbar.set)
        self.selected_xscrollbar.config(command=self.selected_tree.xview)

        # Make resizable treeview
        self.SVT_selected_student_query_canvas.grid_rowconfigure(0, weight=1)
        self.SVT_selected_student_query_canvas.grid_columnconfigure(
            0, weight=1)
        self.selected_tree.grid(row=0, column=0, sticky='nsew')

        self.turn_on_generate()

    # Function to create the search results table
    def search_table(self):
        # Treeview after using search function
        # The number of questions
        search_num_of_question = 10
        search_selected_column = ['#studentID']
        for n in range(1, search_num_of_question + 1):
            search_selected_column.append((f'#{n}'))

        self.search_selected_tree = ttk.Treeview(self.search_SVT_selected_student_query_canvas,
                                                 columns=search_selected_column, show='headings')
        self.search_selected_tree.place(
            relx=0, rely=0, relheight=1, relwidth=1)

        # Define headings
        self.search_selected_tree.heading('#studentID', text='StudentID')
        for n in range(2, search_num_of_question + 2):
            self.search_selected_tree.heading((f'#{n}'), text=(f'Q100{n - 1}'))

        # Generate sample data
        search_students_grade = []
        for n in range(99):
            search_students_grade.append((f'value{n}', f'value{n}', f'value{n}', f'value{n}', f'value{n}', f'value{n}',
                                          f'value{n}', f'value{n}', f'value{n}'))

        # Adding data to the treeview
        for search_grade in search_students_grade:
            self.search_selected_tree.insert('', tk.END, values=search_grade)

        # Vertical scrollbar for treeview
        self.search_selected_yscrollbar = Scrollbar(
            self.search_SVT_selected_student_query_canvas, orient=VERTICAL)
        self.search_selected_yscrollbar.grid(
            row=0, column=1, sticky=(N, S, W, E))
        self.search_selected_yscrollbar.config(
            command=self.search_selected_tree.yview)
        self.search_selected_tree.config(
            yscrollcommand=self.search_selected_yscrollbar.set)

        # Horizontal scrollbar for treeview
        self.search_selected_xscrollbar = Scrollbar(
            self.search_SVT_selected_student_query_canvas, orient=HORIZONTAL)
        self.search_selected_xscrollbar.grid(
            row=1, column=0, sticky=(N, S, W, E))
        self.search_selected_tree.config(
            xscrollcommand=self.search_selected_xscrollbar.set)
        self.search_selected_xscrollbar.config(
            command=self.search_selected_tree.xview)

        # Make resizable treeview
        self.search_SVT_selected_student_query_canvas.grid_rowconfigure(
            0, weight=1)
        self.search_SVT_selected_student_query_canvas.grid_columnconfigure(
            0, weight=1)
        self.search_selected_tree.grid(row=0, column=0, sticky='nsew')

        self.turn_on_search_treeview()

    # Function to export files
    def export_files(self):
        files = [('All Files', '*.*'),
                 ('CSV Files', '*.csv'),
                 ('Text Document', '*.txt')]
        file = asksaveasfile(filetypes=files, defaultextension=files)
        return (file.name)

if __name__ == '__main__':
    vp_start_gui()
