from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk


class QuestionCanvasClass:
    def __init__(self, input_frame, no_ques):
        input_frame.configure(background="white")
        # Create canvas for packaging
        self.package_canvas = tk.Canvas(input_frame, bg="white", width=700)
        # Create canvas for each question
        self.question_canvas = tk.Canvas(
            self.package_canvas, bg="white", borderwidth=2, relief="solid")

        # Question label
        self.question_number_label = tk.Label(self.question_canvas)
        self.question_number_label.place(
            relx=0.01, rely=0.02, relheight=0.2, relwidth=0.2)
        self.question_number_label.configure(anchor='w')
        self.question_number_label.configure(background="#ffffff")
        self.question_number_label.configure(
            font="-family {Segoe UI} -size 12 -weight bold -underline 1")
        self.question_number_label.configure(foreground="#000000")
        self.question_number_label.configure(
            text='Question ' + str(no_ques) + ": ")

        # Query label
        self.query_label = tk.Label(self.question_canvas)
        self.query_label.place(relx=0.01, rely=0.2,
                               relheight=0.2, relwidth=0.1)
        self.query_label.configure(anchor='w')
        self.query_label.configure(background="#ffffff")
        self.query_label.configure(font="-family {Segoe UI Historic} -size 10")
        self.query_label.configure(foreground="#000000")
        self.query_label.configure(text='''Question''')

        # Textbox for enter query
        self.query_entry = tk.Entry(self.question_canvas)
        self.query_entry.place(relx=0.01, rely=0.4,
                               relheight=0.2, relwidth=0.98)
        self.query_entry.configure(background="white")
        self.query_entry.configure(cursor="fleur")
        self.query_entry.configure(font="TkFixedFont")
        self.query_entry.configure(foreground="#000000")
        self.query_entry.configure(insertbackground="black")

        # Query ID label
        self.query_ID_label = tk.Label(self.question_canvas)
        self.query_ID_label.place(
            relx=0.01, rely=0.7, relheight=0.2, relwidth=0.1)
        self.query_ID_label.configure(anchor='w')
        self.query_ID_label.configure(background="#ffffff")
        self.query_ID_label.configure(
            font="-family {Segoe UI Historic} -size 10")
        self.query_ID_label.configure(foreground="#000000")
        self.query_ID_label.configure(text='''Query''')

        # Textbox for enter query ID
        self.query_ID_entry = tk.Entry(self.question_canvas)
        self.query_ID_entry.place(
            relx=0.11, rely=0.7, relheight=0.2, relwidth=0.4)
        self.query_ID_entry.configure(background="white")
        self.query_ID_entry.configure(cursor="fleur")
        self.query_ID_entry.configure(font="TkFixedFont")
        self.query_ID_entry.configure(foreground="#000000")
        self.query_ID_entry.configure(insertbackground="black")

        # Difficulty
        self.input_difficulty_label = tk.Label(self.question_canvas)
        self.input_difficulty_label.place(
            relx=0.52, rely=0.7, relheight=0.2, relwidth=0.1)
        self.input_difficulty_label.configure(anchor='w')
        self.input_difficulty_label.configure(background="#ffffff")
        self.input_difficulty_label.configure(cursor="fleur")
        self.input_difficulty_label.configure(foreground="#000000")
        self.input_difficulty_label.configure(text='''Difficulty''')

        # Difficulty array for the difficulty dropdown
        DIFFICULTY = ["001", "002", "003", "004", "005"]
        input_variable = StringVar(self.question_canvas)
        # Default drowdown value
        input_variable.set(DIFFICULTY[0])

        # GUI dropdown that allows the user to select the difficuilty of the queries they wish to select from (and the label next to it)
        input_difficulty = tk.OptionMenu(
            self.question_canvas, input_variable, *DIFFICULTY)
        input_difficulty.place(relx=0.72, rely=0.7,
                               relheight=0.2, relwidth=0.2)
        self.question_canvas.place(
            relx=0.05, rely=0.2, relheight=0.7, relwidth=0.914)

    def rePlace(self):
        self.package_canvas.pack(fill=BOTH, expand=True)
