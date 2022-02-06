import pyodbc as po
import uuid
import datetime
from databaseconnectionclass import DatabaseConnection
from tkinter import messagebox

class Semester():
    semesterId = str
    studyPeriod = int
    Year = str
    startDate = str
    endDate = str
    code = str

    # Constructor 
    def __init__(self,*args):
        # Constructor for a new Semester object
        if len(args) == 5:
            self.semesterId=str(uuid.uuid1())
            self.studyPeriod=args[0]
            self.year=args[1]
            self.startDate=args[2]
            self.endDate=args[3]
            self.code=args[4]
        # Constructor for reading an existing Semester object back from the database
        if len(args) == 6:
            self.semesterId=args[0]
            self.studyPeriod=args[1]
            self.year=args[2]
            self.startDate=args[3]
            self.endDate=args[4]
            self.code=args[5]

    # Method for storing semesters in the database
    def storeSemester(self, connection):
        # Creates a cursor based of the connection (essentially what takes data too and from the database)
        cursor=connection.cursor()
        
        # Query to store the semester in the database
        query= "INSERT INTO dbo.Semester (SemesterId, StudyPeriod, Year, StartDate, EndDate, Code) VALUES ('" + self.semesterId + "', '" + str(self.studyPeriod) + "', '" + str(self.year) + "', '" + str(self.startDate) + "', '" + str(self.endDate) +"' , '"+self.code+"');"
        
        # Trys to query the database
        try:
            cursor.execute(query)
        
        # Catches any problems querying the database
        except Exception as e:
            print (e)
        
        # Commit changes
        connection.commit()
        
    # Method for retrieving the current semester from the database (semesterId is used for storing assignment questions in the db)
    @staticmethod
    def getCurrentSemester(connection):
        # Creates a cursor based of the connection (essentially what takes data too and from the database)
        cursor=connection.cursor()

        # Query for the database
        query="select top 1 * from dbo.Semester"

        # Trys to query the database
        try:
            cursor.execute(query)

        # Catches any problems querying the database
        except Exception as e:
            print(e)

        # Stores the retrieved semester
        semesterData=cursor.fetchall()
        
        # Converts it into a semester object
        semester = Semester(semesterData[0][0], semesterData[0][1], semesterData[0][2], semesterData[0][3], semesterData[0][4], semesterData[0][5])
        
        # Returns the retrieved semester object
        return semester

    '''
    This function gets called when Save semester button is called in the GUI
    '''
    @staticmethod
    def SaveSemesterGUI(*args):
        storeError = False
        enteredSemester=Semester(args[0], args[1], args[2], args[3], args[4])
        try:
            enteredSemester.storeSemester(args[5])
        except Exception:
            storeError = True
            messagebox.showinfo(title='Error', message='There was an error storing the semester. Make sure you establish connection to the SQL Checker database first and make sure all your semester parameters are valid.')
            print ("There was an error storing the semester. Make sure you establish connection to the SQL Checker database first and make sure all your semester parameters are valid.")
        if storeError == False:
            messagebox.showinfo(title='Success', message='The current semester was succesfully updated in the database.')
            print("Semester Saved")

   

if __name__=='__main__':
    testSemester=Semester(5,2020,datetime.date(2020,8,1),datetime.date(2020,12,1),"SP5-2020")
    connection = DatabaseConnection('Driver={SQL Server};', 'Server=DESKTOP-NFLVEPF;', 'Database=SQLCheckerV2;', 'Trusted_Connection=yes;')
    #testSemester.storeSemester(DatabaseConnection.getConnection(connection))
    print(Semester.getCurrentSemester(DatabaseConnection.getConnection(connection)))
    
    #id=uuid.uuid1()
   # print(id)