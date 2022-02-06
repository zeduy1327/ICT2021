import pyodbc 
import uuid
from databaseconnectionclass import DatabaseConnection

class User():
    """description of class"""
   
    #Constructor
    def __init__(self,*args):
        #Constructor that takes 2 Arguement UserName and FullName
        #Used to instantiate new User Record
        # Generates UUID for UserId
        if len(args)==2:
            self.UserId=uuid.uuid1()
            self.UserId=str(self.UserId)
            self.FullName=args[0]
            self.UserName=args[1]
        #Constructor that takes 3 Arguement UserId, UserName and FullName
        #Used to instantiate records retrieved from the database
        elif len(args)==3:
            self.UserId=args[0]
            self.FullName=args[1]
            self.UserName=args[2]
    
    '''
    Function to store User record in the database
    Takes databaseConnection instance and User Instance as Arguement
    '''
    @staticmethod
    def storeUser(connection,user):
        cursor=connection.cursor()
        # Check if the User exist 
        if (User.getIdFromUserName(connection,user.UserName)==None):
            # Query to store User
            query="Insert into dbo.UserAccount (UserID, FullName, UserName) values "+"('"+user.UserId+"' , '"+user.FullName+"' , '"+user.UserName+"')"
            # Attempt to execute the query
            try:    
                cursor.execute(query)
            # Catch any exceptions
            except Exception as e:
                print(e)
            #Commit connection
            connection.commit()
        # If the UserName Exists in the database print User Exists
        else:
            print("User Exists")


    # Static method that retrieves all the users in the database (for graphing/exporting purposes)
    @staticmethod
    def getAllUsers(connection):
        # Create cursor (basically what takes commands to the database and returns the data from it) 
        cursor=connection.cursor()
        
        query="select * from dbo.UserAccount"

        # Attempt to query the database to retrieve all the users
        try:
            cursor.execute(query)
        # Catch any errors querying the database
        except Exception as e:
            print (e)
        
        # Stores all the data retrieved by the cursor
        data = cursor.fetchall()

        allUsers = []
        # Converts each user record into a user object
        for row in data:
            user = User(row[0], row[1], row[2])
            allUsers.append(user)
        
        # Returns an array of User objects
        return allUsers
       
    '''
    Retrieve UserId for any given UserName
    Takes databaseConnection instance and Username As Arguement
    Returns UserId
    '''
    @staticmethod
    def getIdFromUserName(connection,userName):
        # Create cursor (basically what takes commands to the database and returns the data from it) 
        cursor=connection.cursor()
        
        # Query to Check for any record that has the given UserName
        query="Select u.UserId from dbo.UserAccount u where CONVERT(VARCHAR,u.UserName) ='"+userName+"'"
        
        # Attempt to run the query
        try:
            cursor.execute(query)
        # Catches any errors with the query 
        except Exception as e:
            print(e)
            
        #Return the result of the query    
        for row in cursor:
            return(row[0])


    '''
    Function to retrieve userId associated with userName
    '''
    @staticmethod
    def getUserNameFromId(connection,userId):
        # Create cursor (basically what takes commands to the database and returns the data from it) 
        cursor=connection.cursor()
        
        # Query to Check for any record that has the given UserName
        query="Select u.UserName from dbo.UserAccount u where u.UserId ='"+userId+"'"
        
        # Attempt to run the query
        try:
            cursor.execute(query)
        # Catches any errors with the query 
        except Exception as e:
            print(e)
            
        #Return the result of the query    
        for row in cursor:
            return(row[0])
     


if __name__=='__main__':
    testUser=User("TestUserName2", "TestFullName2")
    #connectionString = DatabaseConnection(Driver={SQL Server};, Server=DESKTOP-NFLVEPF;, Database=;, Trusted_Connection=yes;)
    #globalConnection=DatabaseConnection.getConnection(connectionString)
    #userId=User.getIdFromUserName(globalConnection,"TestUserName1")
    #print(userId)
    #User.storeUser(globalConnection,testUser)
    #allUsers=User.getAllUser(connection)
    #print(allUsers)

    #print(User.getUserNameFromId(globalConnection,"55a1614a-aaff-11eb-92f1-00155dd652d9"))

    '''  
    User.storeUser(connection,testUser)
    print(testUser.UserName)
    testUser2=User("TestUserName2", "TestFullName2")
    '''


    


