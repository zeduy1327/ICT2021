import unittest
import sys
sys.path.append("..")
from databaseconnectionclass import DatabaseConnection

class DBBuilder(): # More flexible testing
    
    @staticmethod
    def getSQLCheckerConnectionPath():
        return DatabaseConnection('Driver={ODBC Driver 17 for SQL Server};', 'Server=DESKTOP-R7DFSAV;', 'Database=SQLCheckerV2;', 'Trusted_Connection=yes;')

    @staticmethod
    def getSQLCheckerConnection():
        connection = DatabaseConnection('Driver={ODBC Driver 17 for SQL Server};', 'Server=DESKTOP-R7DFSAV;', 'Database=SQLCheckerV2;', 'Trusted_Connection=yes;')
        return DatabaseConnection.getConnection(connection,'None')

    @staticmethod
    def getAdventureWorkConnection():
        connection = DatabaseConnection('Driver={ODBC Driver 17 for SQL Server};', 'Server=DESKTOP-R7DFSAV;', 'Database=AdventureWorks2019;', 'Trusted_Connection=yes;')
        return DatabaseConnection.getConnection(connection,'None')

    @staticmethod
    def RemoveUser(self, connection, userId):
        cursor=connection.cursor()
        cursor.commit()
        query="DELETE FROM dbo.UserAccount WHERE UserId = '"+userId+"';"
        
        # Attempt to run the query
        try:
            cursor.execute(query)
            cursor.commit() # we want to make sure it's inserted so we can delete it
        # Catches any errors with the query 
        except Exception as e:
            print('error')
            print(e)
            self.fail('error:' + e + ' thrown')

    @staticmethod
    def RemoveSemester(self, connection, semesterId):
        cursor=connection.cursor()
        cursor.commit()
        query="DELETE FROM dbo.Semester WHERE SemesterId = '"+semesterId+"';"
        
        # Attempt to run the query
        try:
            cursor.execute(query)
            cursor.commit() # we want to make sure it's inserted so we can delete it
        # Catches any errors with the query 
        except Exception as e:
            print('error')
            print(e)
            self.fail('error:' + e + ' thrown')

    @staticmethod
    def RemoveEnrollment(self, connection, enrollmentId):
        cursor=connection.cursor()
        cursor.commit()
        query="DELETE FROM dbo.Enrollment WHERE EnrollmentId = '"+enrollmentId+"';"
        
        # Attempt to run the query
        try:
            cursor.execute(query)
            cursor.commit() # we want to make sure it's inserted so we can delete it
        # Catches any errors with the query 
        except Exception as e:
            print('error')
            print(e)
            self.fail('error:' + e + ' thrown')

    @staticmethod
    def RemoveDifficulty(self, connection, difficultyId):
        cursor=connection.cursor()
        cursor.commit()
        query="DELETE FROM dbo.Difficulty WHERE DifficultyId = '"+difficultyId+"';"
        
        # Attempt to run the query
        try:
            cursor.execute(query)
            cursor.commit() # we want to make sure it's inserted so we can delete it
        # Catches any errors with the query 
        except Exception as e:
            print('error')
            print(e)
            self.fail('error:' + e + ' thrown')

    @staticmethod
    def RemoveQuestion(self, connection, questionId):
        cursor=connection.cursor()
        cursor.commit()
        query="DELETE FROM dbo.Question WHERE QuestionId = '"+questionId+"';"
        
        # Attempt to run the query
        try:
            cursor.execute(query)
            cursor.commit() # we want to make sure it's inserted so we can delete it
        # Catches any errors with the query 
        except Exception as e:
            print('error')
            print(e)
            self.fail('error:' + e + ' thrown')

    @staticmethod
    def RemoveQuery(self, connection, queryId):
        cursor=connection.cursor()
        cursor.commit()
        query="DELETE FROM dbo.Query WHERE QueryId = '"+queryId+"';"
        
        # Attempt to run the query
        try:
            cursor.execute(query)
            cursor.commit() # we want to make sure it's inserted so we can delete it
        # Catches any errors with the query 
        except Exception as e:
            print('error')
            print(e)
            self.fail('error:' + e + ' thrown')

    @staticmethod
    def RemoveMarks(self, connection, marksId):
        cursor=connection.cursor()
        cursor.commit()
        query="DELETE FROM dbo.Marks WHERE MarkId = '"+marksId+"';"
        
        # Attempt to run the query
        try:
            cursor.execute(query)
            cursor.commit() # we want to make sure it's inserted so we can delete it
        # Catches any errors with the query 
        except Exception as e:
            print('error')
            print(e)
            self.fail('error:' + e + ' thrown')