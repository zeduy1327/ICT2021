import pyodbc as po
from tkinter import messagebox

class DatabaseConnection:
    driver = str
    serverName = str
    databaseName = str
    serverUsername = str
    serverPassword = str
    trustedConnection = str

    # Constructor 
    def __init__(self, *args):
        if len(args) == 5:
            self.driver = args[0]
            self.serverName = args[1]
            self.databaseName = args[2]
            self.serverUsername = args[3]
            self.serverPassword = args[4]
        elif len(args) == 4:
            self.driver = args[0]
            self.serverName = args[1]
            self.databaseName = args[2]
            self.trustedConnection = args[3]
    
    # Test Connection Function (will get called when the user clicks the test connection button on the GUI)
    def testConnection(self):
        # Attempts to establish connection to the database given the databaseConnection object (for mac)
        connectionError = False
        try:
            connection = po.connect(self.driver + self.serverName + self.databaseName + self.serverUsername + self.serverPassword)
        # Catches any problems with the connection
        except Exception as e:
            connectionError = True
            
        # Attempts to establish connection to the database given the databaseConnection object if there was an error with the mac connection (for windows)
        if connectionError == True:
            try:
                connectionError = False
                connection = po.connect(self.driver + self.serverName + self.databaseName + self.trustedConnection)
            # Catches any problems with the connection
            except Exception as e:
                connectionError = True
        
        # Returns if the connection is valid
        if connectionError == False:
            # print ("Connection is valid.")
            messagebox.showinfo(title='Success', message='Connection is valid.')
            return ("Connection is valid.")
        # Returns if the connection is invalid
        elif connectionError == True:
            # print ("Connection is invalid.") 
            messagebox.showinfo(title='Error', message='Connection is invalid. Check your connection string.')
            return ("Connection is invalid.")

    # Function that returns a connected database connection object
    @staticmethod
    def getConnection(databaseConnection, page):
        # Attempts to establish connection to the database given the databaseConnection object (for mac)
        connectionError = False
        try:
            connection = po.connect(databaseConnection.driver + databaseConnection.serverName + databaseConnection.databaseName + databaseConnection.serverUsername + databaseConnection.serverPassword)
        # Catches any problems with the connection
        except Exception as e:
            connectionError = True
            
        # Attempts to establish connection to the database given the databaseConnection object if there was an error with the mac connection (for windows)
        if connectionError == True:
            try:
                connectionError = False
                connection = po.connect(databaseConnection.driver + databaseConnection.serverName + databaseConnection.databaseName + databaseConnection.trustedConnection)
            # Catches any problems with the connection
            except Exception as e:
                connectionError = True

        # Returns an established connection and a pop up if no exception and the settings page is calling it
        if connectionError == False and page == "Settings":
            # print ("Connection Established.")
            messagebox.showinfo(title='Success', message='Connection Successfully Established.')
            return connection
        elif connectionError == False and page != "Settings":
            # print ("Connection Established.")
            return connection
        # Returns if there is an error with the connection and the settings page is calling the method
        elif connectionError == True and page == "Settings":
            print ("Error, connection not established. Test the connections validity before attempting to connect.")
            messagebox.showinfo(title='Error', message='Error, connection not established. Test the connections validity before attempting to connect.')
        elif connectionError == True and page != "Settings":
            print ("Error, connection not established. Test the connections validity before attempting to connect.")
            
    # Function thats called when the user wishes to change the database connection
    def updateDatabaseConnection(self, database):
        self.databaseName = database
    
    # Function thats called when the user wishes to change the server connection
    def updateServerConnection(self, server):
        self.serverName = server

    # Function that is attached to a button in the GUI for testing database/server connections
    # self.server_connection_test_button.configure(command = lambda: DatabaseConnection.testConnectionGUI(self.server_connection_entry.get("1.0",'end')))
    staticmethod
    def testConnectionGUI(userInputString):
            #Identifies the different parts of the users input i.e. driver, database, server name etc.)
            userInputArray = []
            startIndex = 0
            endIndex = 0
            for char in userInputString: 
                if char == ',' and userInputString[endIndex + 1] == " ":
                    userInputArray.append(userInputString[startIndex:endIndex])
                    startIndex = endIndex + 2
                endIndex += 1
            userInputArray.append(userInputString[startIndex:-1])
            
            # Its assumed the connection is entered as a string with 4 or 5 parameters (depends on mac or windows) seperated by a comma. This will be in the user manual. 
            if len(userInputArray) == 5:
                # Creates a DatabaseConnection object based off the users input
                connection = DatabaseConnection(userInputArray[0], userInputArray[1], userInputArray[2], userInputArray[3], userInputArray[4])
            elif len(userInputArray) == 4: 
                connection = DatabaseConnection(userInputArray[0], userInputArray[1], userInputArray[2], userInputArray[3])
            # Throws an error if the connection string is neither 4 or 5 parameters long
            elif len(userInputArray) != 5 and len(userInputArray) != 4: 
                print ("Connection is invalid.")
                messagebox.showinfo(title='Error', message='Connection is invalid. Check your connection string.')
                return ("Connection is invalid.")
            # Tests the connection and returns its validity
            return DatabaseConnection.testConnection(connection)

    # Function that is attached to a button in the GUI for actually establshing and returning a database connection 
    staticmethod
    def establishConnectionGUI(userInputString, page):
            #Identifies the different parts of the users input i.e. driver, database, server name etc.)
            userInputArray = []
            startIndex = 0
            endIndex = 0
            for char in userInputString: 
                if char == ',' and userInputString[endIndex + 1] == " ":
                    userInputArray.append(userInputString[startIndex:endIndex])
                    startIndex = endIndex + 2
                endIndex += 1
            userInputArray.append(userInputString[startIndex:-1])

             # Its assumed the connection is entered as a string with 4 or 5 parameters (depends on mac or windows) seperated by a comma. This will be in the user manual. 
            if len(userInputArray) == 5:
                # Creates a DatabaseConnection object based off the users input
                connection = DatabaseConnection(userInputArray[0], userInputArray[1], userInputArray[2], userInputArray[3], userInputArray[4])
            elif len(userInputArray) == 4: 
                connection = DatabaseConnection(userInputArray[0], userInputArray[1], userInputArray[2], userInputArray[3])
            # Throws an error if the connection string is neither 4 or 5 parameters long
            elif len(userInputArray) != 5 and len(userInputArray) != 4 and page == "Settings": 
                print ("Connection is invalid.")
                messagebox.showinfo(title='Error', message='Connection is invalid. Check your connection string.')
                return ("Connection is invalid.")
            # Attempts to connect to the database/server based on the user's input and returns the established connection (if valid)
            return DatabaseConnection.getConnection(connection, page)
            
