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
from IntegrationTests.DBBuilder import DBBuilder

class QueryTests(unittest.TestCase):
   
    def testQueryIntegration(self): # Part of DB Integration testing, Order is important.
        # Variables
        difficulty = Difficulty(10,'Pretty Hard')
        question = Question('find the left join of tables 1 and 2', difficulty.difficultyId)
        semester = Semester(2,'2021',datetime.date(2021,3,1),datetime.date(2021,7,1),'INFS2023')
        query = Query(question.questionId,'some sql here',10)
        connection = DBBuilder.getSQLCheckerConnection()
        
        # Store
        difficulty.storeDifficulty(connection)
        question.storeQuestion(connection)
        semester.storeSemester(connection)
        
        # Generate Assignment Question
        questionNumber = AssignmentQuestion.generateAssignmentQuestionNumber(difficulty.difficultyId,connection)
        assignmentQuestion = AssignmentQuestion(question.questionId,question.question,difficulty.difficultyId,semester.semesterId,questionNumber)
     
        # Store Assignment Question
        assignmentQuestion.storeAssignmentQuestion(connection)
        query.storeQuery(connection)

        # Retrieve and Check
        result = Query.getTestQuery(connection,questionNumber)

        self.assertEqual(result.queryId, query.queryId)
        self.assertEqual(result.questionId, query.questionId)
        self.assertEqual(result.score, query.score)
        self.assertEqual(result.sql, query.sql)

        # Cleanup
        DBBuilder.RemoveQuery(self,connection,query.queryId)
        AssignmentQuestion.destoreAssignmentQuestion(assignmentQuestion.questionId,connection)
        DBBuilder.RemoveQuestion(self,connection,question.questionId)
        DBBuilder.RemoveDifficulty(self,connection,difficulty.difficultyId)
        DBBuilder.RemoveSemester(self,connection,semester.semesterId)


if __name__ == '__main__':
    unittest.main()