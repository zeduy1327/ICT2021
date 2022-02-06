import pyodbc as po
import uuid
from databaseconnectionclass import DatabaseConnection

class Difficulty(): 
    difficultyId = str
    diffLevel = int
    description = str

    # Constructor
    def __init__(self, *args):
        # Constructor for reading an existing difficuilty object back from the db (i.e. already has difficultyId)
        if len(args) == 3:
            self.difficultyId = args[0]
            self.diffLevel = args[1]
            self.description = args[2]
        # Constructor for creating a new difficulty object (i.e. needs a difficultyId to be generated in the constructor)
        if len(args) == 2:
            self.difficultyId = self.generateId()
            self.diffLevel = args[0]
            self.description = args[1]

    # Function that stores the difficuilty object in the database
    def storeDifficulty(self, connection):
        query = "INSERT INTO Difficulty (DifficultyId, DiffLevel, Description) VALUES ('" + self.difficultyId + "', '" + str(self.diffLevel) + "', '" + self.description + "');"

        # Create cursor (basically what takes commands to the database and returns the data from it) 
        c = connection.cursor()

        # Try to query the database given the difficuilty objects values
        try:
            c.execute(query)
        # Catches any problems with the query
        except:
            print ("There was an error querying the database. Check your database connection via the database connection page")

        # Commit changes
        connection.commit()

    # Function that generates a GUID for the difficulty object 
    def generateId(self):
        return str(uuid.uuid1())

    # Static Function that returns a difficulty record if it can be found
    @staticmethod
    def getDifficultyId(diffLevel, connection):
        query="Select * from dbo.Difficulty d where d.DiffLevel = '" + str(diffLevel) + "';"
        
        # Create cursor (basically what takes commands to the database and returns the data from it) 
        c = connection.cursor()

        # Try to query the database 
        try:
            c.execute(query)
        # Catches any problems with the query
        except:
            print ("There was an error querying the database. Check your database connection via the database connection page")
        
        # Stores the records retrieved by the cursor (if any)
        records = c.fetchall()
        
        # Commit changes
        connection.commit()

        # Returns the id of the identified difficulty record
        return records[0][0]

    # Static Function that returns a difficulty object from the difficulty id
    @staticmethod
    def getDifficultyFromId(difficultyId, connection):
        query="Select * from dbo.Difficulty d where d.DifficultyId = '" + difficultyId + "';"
        
        # Create cursor (basically what takes commands to the database and returns the data from it) 
        c = connection.cursor()

        # Try to query the database 
        try:
            c.execute(query)
        # Catches any problems with the query
        except:
            print ("There was an error querying the database. Check your database connection via the database connection page")
        
        # Stores the records retrieved by the cursor (if any)
        records = c.fetchall()
        
        # Commit changes
        connection.commit()

        difficulty = Difficulty(records[0][0], records[0][1], records[0][2])

        # Returns the id of the identified difficulty record
        return difficulty