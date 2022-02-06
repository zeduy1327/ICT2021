import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

import support
def vp_start_gui():
    global val, w, root
    root = tk.Tk()
    top = input (root)
    support.init(root, top)
    root.mainloop()

w = None
def create_Input(rt, *args, **kwargs):

    global w, w_win, root

    root = rt
    w = tk.Toplevel (root)
    top = input (w)
    support.init(w, top, *args, **kwargs)
    return (w, top)
def destroy_Input():
    global w
    w.destroy()
    w = None

class input:

    def __init__(self, top=None):

        _bgcolor = '#d9d9d9' 
        _fgcolor = '#000000' 
        _compcolor = '#d9d9d9'
        _ana1color = '#d9d9d9'
        _ana2color = '#ececec'

        top.geometry("697x666+1154+289")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1,  1)
        top.title("Python BE SQL Checker")
        top.configure(background="#ffffff")

        self.Header = tk.Canvas(top)
        self.Header.place(relx=0.0, rely=0.0, relheight=0.2, relwidth=1.0)
        self.Header.configure(background="#0052A0")
        self.Header.configure(borderwidth="2")
        self.Header.configure(insertbackground="black")
        self.Header.configure(relief="ridge")
        self.Header.configure(selectbackground="blue")
        self.Header.configure(selectforeground="white")

        self.MainMenuNavBut = tk.Button(top)
        self.MainMenuNavBut.place(relx=0.043, rely=0.225, height=28, width=87)
        self.MainMenuNavBut.configure(activebackground="#0052A0")
        self.MainMenuNavBut.configure(activeforeground="white")
        self.MainMenuNavBut.configure(activeforeground="#000000")
        self.MainMenuNavBut.configure(background="#A4CAED")
        self.MainMenuNavBut.configure(cursor="fleur")
        self.MainMenuNavBut.configure(disabledforeground="#a3a3a3")
        self.MainMenuNavBut.configure(foreground="#000000")
        self.MainMenuNavBut.configure(highlightbackground="#d9d9d9")
        self.MainMenuNavBut.configure(highlightcolor="black")
        self.MainMenuNavBut.configure(pady="0")
        self.MainMenuNavBut.configure(text='''Main Menu''')
        '''self.MainMenuNavBut.configure(command= lambda: navigate("database"))'''

        self.TestQueryNavBut = tk.Button(top)
        self.TestQueryNavBut.place(relx=0.168, rely=0.225, height=28, width=107)
        self.TestQueryNavBut.configure(activebackground="#0052A0")
        self.TestQueryNavBut.configure(activeforeground="white")
        self.TestQueryNavBut.configure(activeforeground="#000000")
        self.TestQueryNavBut.configure(background="#A4CAED")
        self.TestQueryNavBut.configure(disabledforeground="#a3a3a3")
        self.TestQueryNavBut.configure(foreground="#000000")
        self.TestQueryNavBut.configure(highlightbackground="#d9d9d9")
        self.TestQueryNavBut.configure(highlightcolor="black")
        self.TestQueryNavBut.configure(pady="0")
        self.TestQueryNavBut.configure(text='''Test Query''')

        self.StudentQueryNavBut = tk.Button(top)
        self.StudentQueryNavBut.place(relx=0.321, rely=0.225, height=28
                , width=127)
        self.StudentQueryNavBut.configure(activebackground="#0052A0")
        self.StudentQueryNavBut.configure(activeforeground="white")
        self.StudentQueryNavBut.configure(activeforeground="#000000")
        self.StudentQueryNavBut.configure(background="#A4CAED")
        self.StudentQueryNavBut.configure(disabledforeground="#a3a3a3")
        self.StudentQueryNavBut.configure(foreground="#000000")
        self.StudentQueryNavBut.configure(highlightbackground="#d9d9d9")
        self.StudentQueryNavBut.configure(highlightcolor="black")
        self.StudentQueryNavBut.configure(pady="0")
        self.StudentQueryNavBut.configure(text='''Student Query''')

        self.StudentVsTestQueryNavBut = tk.Button(top)
        self.StudentVsTestQueryNavBut.place(relx=0.504, rely=0.225, height=28
                , width=157)
        self.StudentVsTestQueryNavBut.configure(activebackground="#0052A0")
        self.StudentVsTestQueryNavBut.configure(activeforeground="white")
        self.StudentVsTestQueryNavBut.configure(activeforeground="#000000")
        self.StudentVsTestQueryNavBut.configure(background="#A4CAED")
        self.StudentVsTestQueryNavBut.configure(cursor="fleur")
        self.StudentVsTestQueryNavBut.configure(disabledforeground="#a3a3a3")
        self.StudentVsTestQueryNavBut.configure(foreground="#000000")
        self.StudentVsTestQueryNavBut.configure(highlightbackground="#d9d9d9")
        self.StudentVsTestQueryNavBut.configure(highlightcolor="black")
        self.StudentVsTestQueryNavBut.configure(pady="0")
        self.StudentVsTestQueryNavBut.configure(text='''Student vs. Test Query''')

        self.DatabaseNavBut = tk.Button(top)
        self.DatabaseNavBut.place(relx=0.729, rely=0.225, height=28, width=159)
        self.DatabaseNavBut.configure(activebackground="#0052A0")
        self.DatabaseNavBut.configure(activeforeground="white")
        self.DatabaseNavBut.configure(activeforeground="#000000")
        self.DatabaseNavBut.configure(background="#A4CAED")
        self.DatabaseNavBut.configure(disabledforeground="#a3a3a3")
        self.DatabaseNavBut.configure(foreground="#000000")
        self.DatabaseNavBut.configure(highlightbackground="#d9d9d9")
        self.DatabaseNavBut.configure(highlightcolor="black")
        self.DatabaseNavBut.configure(pady="0")
        self.DatabaseNavBut.configure(text='''Database Connection''')

        self.ThumbLabel = tk.Label(top)
        self.ThumbLabel.place(relx=0.043, rely=0.286, height=51, width=644)
        self.ThumbLabel.configure(background="#0052A0")
        self.ThumbLabel.configure(disabledforeground="#a3a3a3")
        self.ThumbLabel.configure(font="-family {Segoe UI} -size 20 -weight bold")
        self.ThumbLabel.configure(foreground="#ffffff")
        self.ThumbLabel.configure(text='''Input Test Queries''')

        self.OrdinalLabel = tk.Label(top)
        self.OrdinalLabel.place(relx=0.043, rely=0.377, height=22, width=94)
        self.OrdinalLabel.configure(anchor='w')
        self.OrdinalLabel.configure(background="#ffffff")
        self.OrdinalLabel.configure(disabledforeground="#a3a3a3")
        self.OrdinalLabel.configure(font="-family {Segoe UI} -size 12 -weight bold -underline 1")
        self.OrdinalLabel.configure(foreground="#000000")
        self.OrdinalLabel.configure(text='''Query 1:''')

        self.QueryLabel = tk.Label(top)
        self.QueryLabel.place(relx=0.043, rely=0.422, height=21, width=64)
        self.QueryLabel.configure(anchor='w')
        self.QueryLabel.configure(background="#ffffff")
        self.QueryLabel.configure(disabledforeground="#a3a3a3")
        self.QueryLabel.configure(font="-family {Segoe UI Historic} -size 10")
        self.QueryLabel.configure(foreground="#000000")
        self.QueryLabel.configure(text='''Query''')

        self.QueryEntry = tk.Entry(top)
        self.QueryEntry.place(relx=0.043, rely=0.467, height=30, relwidth=0.925)
        self.QueryEntry.configure(background="white")
        self.QueryEntry.configure(cursor="fleur")
        self.QueryEntry.configure(disabledforeground="#a3a3a3")
        self.QueryEntry.configure(font="TkFixedFont")
        self.QueryEntry.configure(foreground="#000000")
        self.QueryEntry.configure(insertbackground="black")

        self.QueryIDLabel = tk.Label(top)
        self.QueryIDLabel.place(relx=0.043, rely=0.527, height=21, width=64)
        self.QueryIDLabel.configure(anchor='w')
        self.QueryIDLabel.configure(background="#ffffff")
        self.QueryIDLabel.configure(disabledforeground="#a3a3a3")
        self.QueryIDLabel.configure(font="-family {Segoe UI Historic} -size 10")
        self.QueryIDLabel.configure(foreground="#000000")
        self.QueryIDLabel.configure(text='''Query ID''')

        self.QueryIDEntry = tk.Entry(top)
        self.QueryIDEntry.place(relx=0.129, rely=0.527, height=30
                , relwidth=0.408)
        self.QueryIDEntry.configure(background="white")
        self.QueryIDEntry.configure(cursor="fleur")
        self.QueryIDEntry.configure(disabledforeground="#a3a3a3")
        self.QueryIDEntry.configure(font="TkFixedFont")
        self.QueryIDEntry.configure(foreground="#000000")
        self.QueryIDEntry.configure(insertbackground="black")

        self.DifficultyLabel = tk.Label(top)
        self.DifficultyLabel.place(relx=0.546, rely=0.527, height=21, width=64)
        self.DifficultyLabel.configure(anchor='w')
        self.DifficultyLabel.configure(background="#ffffff")
        self.DifficultyLabel.configure(cursor="fleur")
        self.DifficultyLabel.configure(disabledforeground="#a3a3a3")
        self.DifficultyLabel.configure(foreground="#000000")
        self.DifficultyLabel.configure(text='''Difficulty''')

        self.AddQuestionLabel = tk.Label(top)
        self.AddQuestionLabel.place(relx=0.043, rely=0.617, height=21, width=374)

        self.AddQuestionLabel.configure(anchor='w')
        self.AddQuestionLabel.configure(background="#ffffff")
        self.AddQuestionLabel.configure(disabledforeground="#a3a3a3")
        self.AddQuestionLabel.configure(font="-family {Segoe UI} -size 12 -weight bold")
        self.AddQuestionLabel.configure(foreground="#000000")
        self.AddQuestionLabel.configure(text='''+ Add one more question''')
        

    
if __name__ == '__main__':
    vp_start_gui()

