import pyodbc as po
import mysql.connector as mysql
import csv
import uuid
import mainGUI
class Query():
    queryId = str
    questionId = str
    sql = str
    dataRetrieved = str
    timeToExecute = float
    score = float

    # Constructor
    def __init__(self, *args):
        # Constructor for a new query object (a query Id is generated in the constructor and therefore 
        # is not passed in as an argument, hence, 5 arguments instad of 6)
        if len(args)==5:
            self.queryId = self.generateId()
            self.questionId = args[0]
            self.sql = args[1]
            self.dataRetrieved = args[2]
            self.timeToExecute = args[3]
            self.score = args[4]
        
        # Constructor for an existing query in the database (i.e. a query that already has an Id, hence, 
        # 6 arguments instead of 5
        elif len(args)==6:
            self.queryId = args[0]
            self.questionId = args[1]
            self.sql = args[2]
            self.dataRetrieved = args[3]
            self.timeToExecute = args[4]
            self.score = args[5]
            
    # Function to create a SQL database connection
    def createMSSQLConnection(self, server, database, user, password, Error):

        # Get input of instance name, database name, username, password and return a SQL database connection

        try:
            return mysql.connect(
                Server = server,
                Database = database,
                User = user,
                Password = password)

        # Exception for error    
        except Error as e:
            print (e)

    
    # Function to close the SQL database connection  
    def closeMSSQLConnection(self, connection):

        # Get input of connection and close the database connection
        try: 
            connection.close()
        except po.ProgrammingError:
            pass

    # Function to save query attributes to the database
    def insertQuery(self, connection, *args):
        # Create a connection to the database
        connection = po.connect('Driver={ODBC Driver 17 for SQL Server};''Server=192.168.1.6\localhost,1433;''Database=AdventureWorks2019;''UID=SA;''PWD=reallyStrongPwd123;')

        # Create a cursor as an input connection
        c = connection.cursor()
        c.execute('INSET INTO Query(QueryID) VALUES ("%s")', )
        # Command for creating a new table in database
        create_query = '''CREATE TABLE testquery(
            queryId VARCHAR(255) NOT NULL,
            questionId VARCHAR(255) NOT NULL,
            sql VARCHAR (255) NOT NULL,
            dataRetrieved VARCHAR (255) NOT NULL, 
            timeToExecute FLOAT (0) NOT NULL,
            score FLOAT (0) DEFAULT 10.0,
            PRIMARY KEY (queryId)
        )'''
        
        '''# Drop table if the database already had it
        c.execute("DROP TABLE IF EXISTS testquery")
        # Run the creating table command
        c.execute(create_query)'''

        # Open a csv file which contain information of queries' attributes
        with open('./testquery.csv', 'r') as queryfile:

            # Read the csv data
            query_data = csv.reader(queryfile)

            # Insert data for each row
            for row in query_data:

                # Create tuple for each row to store all attributes
                row_tuple = tuple(row)
                
                # Insert data to testquery table
                c.execute('INSERT INTO Query(QueryID, QuestionID, Sql, DataRetrieved, TimeToExecute, Score) VALUES ("%s", "%s", "%s", "%s", "%f", "%f")', row_tuple)
                c.execute('INSERT INTO Difficulty(DifficultyID, Level, Description) VALUES ("%s", "%s", "%s")', row_tuple)
                c.execute('INSERT INTO Question(QuestionID, DifficultyID, Question) VALUES ("%s", "%s", "%s")', row_tuple)
        '''c.execute("SELECT * FROM testquery")
        print(c.fetchall())'''
        # Commit changes
        connection.commit()


        c.close()

        
    def createQueryObject(self, connection, *args, testquery):
        # Create a connection to the database
        connection = po.connect('Driver={ODBC Driver 17 for SQL Server};''Server=192.168.1.6\localhost,1433;''Database=AdventureWorks2019;''UID=SA;''PWD=reallyStrongPwd123;')

        # Create a cursor as an input connection
        c = connection.cursor()

        # Create a list to store query object
        query_objects = []

        newQueryObject = Query()

        # Get data from table
        c.execute('SELECT * from testquery')

        # Create an attribute to store all information of queries
        info_query = c.fetchall()

        ''' Get data from each row of info_query and
        store it as attributes of a new query object'''
        for row in info_query:
            newQueryObject.queryId = row[0]
            newQueryObject.questionId = row[1]
            newQueryObject.sql = row[2]
            newQueryObject.dataRetrieved = row[3]
            newQueryObject.timeToExecute = row[4]
            newQueryObject.score = row[5]

            # Save query object to a list of query object
            query_objects.append(newQueryObject)

        # Commit changes
        connection.commit()

        # Close database connection
        connection.close()

    # Function to generate generateId
    def generateId(self):
        return str(uuid.uuid1())
