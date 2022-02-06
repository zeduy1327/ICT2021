import unittest
import sys
import datetime
sys.path.append("..")
from Semester import Semester
from Enrollmet import Enrollment
from User import User
from IntegrationTests.DBBuilder import DBBuilder

class EnrollmentTests(unittest.TestCase):

    def test(self):
        # Variables
        semester = Semester(2,'2020',datetime.date(2020,3,1),datetime.date(2020,7,1),'INFS2022')
        user = User('batman385','Bathumat Manfred')
        enrollment = Enrollment(semester.semesterId, user.UserId)
        connection = DBBuilder.getSQLCheckerConnection()
        
        # Store Semester and User
        semester.storeSemester(connection)
        User.storeUser(connection, user)
        
        # Store Enrollment
        Enrollment.storeEnrollment(connection,enrollment)

        # Cleanup
        DBBuilder.RemoveEnrollment(self,connection,enrollment.EnrollmentId)        
        DBBuilder.RemoveSemester(self,connection,semester.semesterId)
        DBBuilder.RemoveUser(self,connection,user.UserId)
        

if __name__ == '__main__':
    unittest.main()