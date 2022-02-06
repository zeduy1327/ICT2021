import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

import support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = TestQuery (root)
    support.init(root, top)
    root.mainloop()

w = None
def create_TestQuery(rt, *args, **kwargs):

    global w, w_win, root

    root = rt
    w = tk.Toplevel (root)
    top = TestQuery (w)
    support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_TestQuery():
    global w
    w.destroy()
    w = None

class TestQuery:
    def __init__(self, top=None):

        _bgcolor = '#d9d9d9'
        _fgcolor = '#000000'
        _compcolor = '#d9d9d9'
        _ana1color = '#d9d9d9'
        _ana2color = '#ececec'

        top.geometry("690x600+471+175")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1,  1)
        top.title("Python BE SQL Checker")
        top.configure(background="#ffffff")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Header = tk.Canvas(top)
        self.Header.place(relx=0.0, rely=0.0, relheight=0.2, relwidth=1.0)
        self.Header.configure(background="#0052A0")
        self.Header.configure(borderwidth="2")
        self.Header.configure(highlightbackground="#d9d9d9")
        self.Header.configure(highlightcolor="black")
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
        self.MainMenuNavBut.configure(disabledforeground="#a3a3a3")
        self.MainMenuNavBut.configure(foreground="#000000")
        self.MainMenuNavBut.configure(highlightbackground="#d9d9d9")
        self.MainMenuNavBut.configure(highlightcolor="black")
        self.MainMenuNavBut.configure(pady="0")
        self.MainMenuNavBut.configure(text='''Main Menu''')

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
        self.StudentQueryNavBut.place(relx=0.32, rely=0.225, height=28
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

        self.InputTestBut = tk.Button(top)
        self.InputTestBut.place(relx=0.043, rely=0.395, height=284, width=277)
        self.InputTestBut.configure(activebackground="#0052A0")
        self.InputTestBut.configure(activeforeground="white")
        self.InputTestBut.configure(activeforeground="#000000")
        self.InputTestBut.configure(anchor='n')
        self.InputTestBut.configure(background="#A4CAED")
        self.InputTestBut.configure(disabledforeground="#a3a3a3")
        self.InputTestBut.configure(font="-family {Segoe UI Historic} -size 15 -weight bold")
        self.InputTestBut.configure(foreground="#000000")
        self.InputTestBut.configure(highlightbackground="#d9d9d9")
        self.InputTestBut.configure(highlightcolor="black")
        self.InputTestBut.configure(pady="0")
        self.InputTestBut.configure(text='''Input Test Queries''')

        self.SelectTestBut = tk.Button(top)
        self.SelectTestBut.place(relx=0.558, rely=0.395, height=284, width=277)
        self.SelectTestBut.configure(activebackground="#0052A0")
        self.SelectTestBut.configure(activeforeground="white")
        self.SelectTestBut.configure(activeforeground="#000000")
        self.SelectTestBut.configure(anchor='n')
        self.SelectTestBut.configure(background="#A4CAED")
        self.SelectTestBut.configure(disabledforeground="#a3a3a3")
        self.SelectTestBut.configure(font="-family {Segoe UI Historic} -size 15 -weight bold")
        self.SelectTestBut.configure(foreground="#000000")
        self.SelectTestBut.configure(highlightbackground="#d9d9d9")
        self.SelectTestBut.configure(highlightcolor="black")
        self.SelectTestBut.configure(pady="0")
        self.SelectTestBut.configure(text='''Select Test Queries''')
        
        self.Message1 = tk.Message(top)
        self.Message1.place(relx=0.383, rely=0.333, relheight=0.051
                , relwidth=0.1)
        self.Message1.configure(background="#d9d9d9")
        self.Message1.configure(foreground="#000000")
        self.Message1.configure(highlightbackground="#d9d9d9")
        self.Message1.configure(highlightcolor="black")
        self.Message1.configure(text='''Message''')
        self.Message1.configure(width=60)


if __name__ == '__main__':
    vp_start_gui()


