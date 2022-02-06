import unittest
import sys
import datetime
sys.path.append("..")
from difficuiltyclass import Difficulty
from Marks import Marks
from queryclass import Query
from questionclass import Question, AssignmentQuestion
from User import User
from Semester import Semester
from Enrollmet import Enrollment
from IntegrationTests.DBBuilder import DBBuilder

class MarksTests(unittest.TestCase):
   
    def testMarksCRUD(self): # Part of DB Integration testing, Order is important.
        # Variables
        user = User('bitmon976','Bith montigue')
        difficulty = Difficulty(10,'Pretty Hard')
        question = Question('find the left join of tables 1 and 2', difficulty.difficultyId)
        semester = Semester(2,'2021',datetime.date(2021,3,1),datetime.date(2021,7,1),'INFS2023')
        enrollment = Enrollment(semester.semesterId, user.UserId)
        query = Query(question.questionId,'some sql here',10)
        marks = Marks(user.UserId,query.queryId,10)
        connection = DBBuilder.getSQLCheckerConnection()
        
        # Store
        difficulty.storeDifficulty(connection)
        question.storeQuestion(connection)
        semester.storeSemester(connection)
        User.storeUser(connection, user)
        Enrollment.storeEnrollment(connection,enrollment)
        
        # Store Assignment Question
        questionNumber = AssignmentQuestion.generateAssignmentQuestionNumber(difficulty.difficultyId,connection)
        assignmentQuestion = AssignmentQuestion(question.questionId,question.question,difficulty.difficultyId,semester.semesterId,questionNumber)
        assignmentQuestion.storeAssignmentQuestion(connection)
        query.storeQuery(connection)

        # Store Marks
        marks.storeMarks(connection)

        # Retrieve from user id
        retrievedmarks = Marks.getMarksForUserId(connection,user.UserId)
        self.assertEqual(len(retrievedmarks), 1)
        result = retrievedmarks[0]
        self.assertEqual(result.marksId,marks.marksId)
        self.assertEqual(result.userId,marks.userId)
        self.assertEqual(result.queryId,marks.queryId)
        self.assertEqual(result.marks,marks.marks)

        # Retrieve from question id
        retrievedmarks = Marks.getMarksForQuestionId(connection,question.questionId)
        self.assertEqual(len(retrievedmarks), 1)
        result = retrievedmarks[0]
        self.assertEqual(result.marksId,marks.marksId)
        self.assertEqual(result.userId,marks.userId)
        self.assertEqual(result.queryId,marks.queryId)
        self.assertEqual(result.marks,marks.marks)

        # Retrieve all marks, (only 1)
        retrievedmarks = Marks.readAllMarks(connection)
        self.assertEqual(len(retrievedmarks), 1)
        result = retrievedmarks[0]
        self.assertEqual(result.marksId,marks.marksId)
        self.assertEqual(result.userId,marks.userId)
        self.assertEqual(result.queryId,marks.queryId)
        self.assertEqual(result.marks,marks.marks)

        # Cleanup
        DBBuilder.RemoveMarks(self,connection,marks.marksId)
        DBBuilder.RemoveQuery(self,connection,query.queryId)
        AssignmentQuestion.destoreAssignmentQuestion(assignmentQuestion.questionId,connection)
        DBBuilder.RemoveQuestion(self,connection,question.questionId)
        DBBuilder.RemoveDifficulty(self,connection,difficulty.difficultyId)
        DBBuilder.RemoveEnrollment(self,connection,enrollment.EnrollmentId)
        DBBuilder.RemoveSemester(self,connection,semester.semesterId)
        DBBuilder.RemoveUser(self,connection,user.UserId)

if __name__ == '__main__':
    unittest.main()