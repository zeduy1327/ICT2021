import pyodbc as po
import uuid
from databaseconnectionclass import DatabaseConnection

class Deduction():
    deductionId = str
    queryId = str
    description = str
    feedback = str
    deductionValue = float

    # Constructor
    def __init__(self, *args):
        # Constructor for a new deduction object (a deduction Id is generated in the constructor and therefore 
        # is not passed in as an argument, hence, 3 arguments instead of 4)
        if len(args) == 4:
            self.deductionId = self.generateId()
            self.queryId = args[0]
            self.description = args[1]
            self.feedback = args[2]
            self.deductionValue = args[3]
        # Constructor for an existing deduction in the database (i.e. a deduction that already has an Id, hence, 
        # 4 arguments instead of 3
        elif len(args) == 5:
            self.deductionId = args[0]
            self.queryId = args[1]
            self.description = args[2]
            self.feedback = args[3]
            self.deductionValue = args[4]
    
    # Function that applies the associated deduction value to the query score
    def applyDeduction(self, studentQuery):
        # Finds out which type of deduction is being applied based off the deduction objects description
        if self.description == "Column Deduction":
            # Determines whether or not the relevant deduction should be applied to the query objects score
            if studentQuery.comparisonCriteria[0] == False:
                studentQuery.score = studentQuery.score - self.deductionValue
        
        elif self.description == "Row Deduction":
            # Determines whether or not the relevant deduction should be applied to the query objects score
            if studentQuery.comparisonCriteria[1] == False:
                studentQuery.score = studentQuery.score - self.deductionValue
        
        elif self.description == "Values Deduction":
            # Determines whether or not the relevant deduction should be applied to the query objects score
            if studentQuery.comparisonCriteria[2] == False:
                studentQuery.score = studentQuery.score - self.deductionValue

        elif self.description == "Column Order Deduction":
            # Determines whether or not the relevant deduction should be applied to the query objects score
            if studentQuery.comparisonCriteria[3] == False:
                studentQuery.score = studentQuery.score - self.deductionValue
        
        elif self.description == "Row Order Deduction":
            # Determines whether or not the relevant deduction should be applied to the query objects score
            if studentQuery.comparisonCriteria[4] == False:
                studentQuery.score = studentQuery.score - self.deductionValue
        
        elif self.description == "Time To Execute Deduction":
            # Determines whether or not the relevant deduction should be applied to the query objects score
            if studentQuery.comparisonCriteria[5] == False:
                studentQuery.score = studentQuery.score - self.deductionValue
        
        elif self.description == "Join Deduction":  
            # Determines whether or not the relevant deduction should be applied to the query objects score
            if studentQuery.comparisonCriteria[6] == False:
                studentQuery.score = studentQuery.score - self.deductionValue 
        
        elif self.description == "Top Deduction":
            # Determines whether or not the relevant deduction should be applied to the query objects score
            if studentQuery.comparisonCriteria[7] == False:
                studentQuery.score = studentQuery.score - self.deductionValue
    
    # Function that changes the deduction value of the deduction object (called when the teacher wishes to change the value of a specific deduction object)
    def changeDeductionValue(self, value):
        self.deductionValue = value

    # Function that generates a GUID for the deduction object 
    def generateId(self):
        return str(uuid.uuid1())
    
    # Function that stores a deduction object in the database
    def storeDeduction(self, connection):
        query = "INSERT INTO Deduction (DeductionId, QueryId, Description, FeedBack, DeductionValue) VALUES ('" + self.deductionId + "', '" + self.queryId + "', '" + str(self.description) + "', '" + str(self.feedback) + "', '" + str(self.deductionValue) + "');"

        # Create cursor (basically what takes commands to the database and returns the data from it) 
        c = connection.cursor()

        # Try to query the database given the deduction object's values
        try:
            c.execute(query)
        # Catches any problems with the query
        except Exception as e:
            print(e)

        # Commit changes
        connection.commit()

    # Function that updates the deduction object's data in the database (called when the teacher wishes to change the value of a specific deduction object)
    def updateDeductionData(self, connection):
        query  = "UPDATE Deduction SET DeductionValue = '" + str(self.deductionValue) + "' WHERE DeductionId = '" + self.deductionId + "';"
            
        # Create cursor (basically what takes commands to the database and returns the data from it) 
        c = connection.cursor()

        # Attempts to update the deduction's data in the database 
        try:
            c.execute(query)
        # Catches any problems with the update query/connection to the database
        except Exception as e:
            print(e)

        # Commit changes
        connection.commit()
    
    # Function that reads all the deduction objects associated with a query object from the database and into an array of deduction objects
    @staticmethod
    def readAllDeductions(testQuery, connection):
        # Create cursor (basically what takes commands to the database and returns the data from it) 
        c = connection.cursor()

        # Try to query the database to identify the deduction objects associated with the given test query
        try:
            c.execute("SELECT * FROM Deduction WHERE QueryId = '" + testQuery.queryId + "';")
        # Catches any problems with the sql 
        except Exception as e: 
            print (e)

        # Stores the data retrieved by the cursor in a deductionData array variable
        deductionData = c.fetchall()

        # Commit changes
        connection.commit()

        deductionObjects = []
        # Converts each of the deduction records read from the database into an actual deduction object and stores them in an array
        for record in deductionData:
            deduction = Deduction(record[0], record[1], record[2], record[3], record[4])
            deductionObjects.append(deduction)
        
        # Returns the deduction object array
        return deductionObjects

    # Function that populates a Test Query object with deductions (the associated student queries are subject to these deductions)
    @staticmethod
    def populateDeductions(testQuery, databaseConnection):
        # 8 default deduction objects that every test query is populated with
        columnDeduction = Deduction(testQuery.queryId, "Column Deduction", "Deduction was applied for retrieving the incorrect number of columns.", 1.0)
        rowDeduction = Deduction(testQuery.queryId, "Row Deduction", "Deduction was applied for retrieving the incorrect number of rows.", 1.0)
        valueDeduction = Deduction(testQuery.queryId, "Values Deduction", "Deduction was applied for retrieving incorrect values.", 2.0)
        columnOrderDeduction = Deduction(testQuery.queryId, "Column Order Deduction", "Deduction was applied for retrieving the incorrect column order.", 1.0)
        rowOrderDeduction = Deduction(testQuery.queryId, "Row Order Deduction", "Deduction was applied for retrieving the incorrect row order.", 1.0)
        efficiencyDeduction = Deduction(testQuery.queryId, "Time To Execute Deduction", "Deduction was applied for executing inneficiently.", 1.0)
        joinDeduction = Deduction(testQuery.queryId, "Join Deduction", "Deduction was applied for the incorrect use of a join", 1.0)
        topDeduction = Deduction(testQuery.queryId, "Top Deduction", "Deduction was applied for the incorrect use of TOP", 2.0)
        
        # Stores them in an array for posting to the database
        deductions = [columnDeduction, rowDeduction, valueDeduction, columnOrderDeduction, rowOrderDeduction, efficiencyDeduction, joinDeduction, topDeduction]
        
        # Stores each of the deduction objects in the database
        for deduction in deductions:
            deduction.storeDeduction(databaseConnection)
    
    # Function that updates any changes made to the deduction values of a question 
    @staticmethod
    def saveUpdatedDeductionsGUI(testQuery, deductionValues, connection):
        # Reads all the deductions for the given testQuery
        deductions = Deduction.readAllDeductions(testQuery, connection)

        index = 0
        for deduction in deductions:
            deduction.deductionValue = deductionValues[index]
            deduction.updateDeductionData(connection)
            index += 1


            


        

