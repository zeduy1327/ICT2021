import User
import pyodbc
import uuid
from databaseconnectionclass import DatabaseConnection
from User import User

class Enrollment(object):
    """description of class"""
    
    #def __init__(self, SemesterId, UserId):
        #self.EnrollmentId=uuid.uuid1()
        #self.EnrollmentId=str(self.EnrollmentId)
        #self.SemesterId=SemesterId
        #self.UserId=UserId
     

    def __init__(self,*args):

        if len(args)==2:
            self.EnrollmentId=uuid.uuid1()
            self.EnrollmentId=str(self.EnrollmentId)
            self.SemesterId=args[0]
            self.UserId=args[1]
        elif len(args)==3:
            self.EnrollmentId=args[0]
            self.SemesterId=args[1]
            self.UserId=args[2]

    def checkExists(SemesterId):
        pass



    @staticmethod
    def storeEnrollment(connection,enrollment):
       
        cursor=connection.cursor()
        query="Insert into dbo.Enrollment (EnrollmentId, SemesterId, UserId) values ('"+enrollment.EnrollmentId+"','"+enrollment.SemesterId+"','"+enrollment.UserId+"')"
        cursor.execute(query)
        cursor.commit()
       

if __name__=='__main__':
    connectionString = DatabaseConnection('Driver={SQL Server};', 'Server=DESKTOP-NFLVEPF;', 'Database=SQLCheckerV2;','Trusted_Connection=yes;')
    dbConnection=DatabaseConnection.getConnection(connectionString)
    userid=User.getIdFromUserName(dbConnection,"TestUserName1")
    print(userid)
    testEnrollment1=Enrollment("c476b76f-ab00-11eb-bafa-00155dd652d9",userid)
    Enrollment.storeEnrollment(dbConnection,testEnrollment1)