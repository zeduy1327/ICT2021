import unittest
import sys
import datetime
sys.path.append("..")
from IntegrationTests.DBBuilder import DBBuilder
from difficuiltyclass import Difficulty
from Semester import Semester
from questionclass import Question, AssignmentQuestion

class QuestionTests(unittest.TestCase):

    def testQuestionIntegration(self):
        # Variables
        difficulty = Difficulty(1,'path prefabs')
        question = Question('what is the average velocity of a laiden swallow?', difficulty.difficultyId)
        connection = DBBuilder.getSQLCheckerConnection()

        # Store Semester and User
        difficulty.storeDifficulty(connection)
        question.storeQuestion(connection)

        # Fetch by ID
        result = Question.getQuestionRecord(question.questionId,connection)
        self.assertEqual(result.difficultyId,question.difficultyId)
        self.assertEqual(result.questionId,question.questionId)
        self.assertEqual(result.question,question.question)

        # readAllQuestions
        result = Question.readAllQuestions(connection)
        self.assertEqual(len(result),1)
        result = result[0]
        self.assertEqual(result.difficultyId,question.difficultyId)
        self.assertEqual(result.questionId,question.questionId)
        self.assertEqual(result.question,question.question)

        # readAllDifficultyQuestions
        result = Question.readAllDifficultyQuestions(connection,difficulty.difficultyId)
        self.assertEqual(len(result),1)
        result = result[0]
        self.assertEqual(result.difficultyId,question.difficultyId)
        self.assertEqual(result.questionId,question.questionId)
        self.assertEqual(result.question,question.question)

        # Cleanup
        DBBuilder.RemoveQuestion(self,connection,question.questionId)
        DBBuilder.RemoveDifficulty(self,connection,difficulty.difficultyId)

    def testGenerateQuestionNumber(self):
        #variables
        difficulty = Difficulty(2,'assignment diff 2')
        connection = DBBuilder.getSQLCheckerConnection()   
        
        # Store difficulty
        difficulty.storeDifficulty(connection)
        result = AssignmentQuestion.generateAssignmentQuestionNumber(difficulty.difficultyId,connection)

        # Cleanup before Assert
        DBBuilder.RemoveDifficulty(self,connection,difficulty.difficultyId)

        # Assert generated id
        self.assertEqual('Q1002',result)

    def testAssignmentQuestionIntegration(self):
        # Variables
        difficulty = Difficulty(2,'assignment diff 2')
        question = Question('what is a select method', difficulty.difficultyId)
        semester = Semester(2,'2021',datetime.date(2021,3,1),datetime.date(2021,7,1),'INFS2023')
        connection = DBBuilder.getSQLCheckerConnection()        

        # Store variables in sequentual order
        difficulty.storeDifficulty(connection)
        question.storeQuestion(connection)
        semester.storeSemester(connection)

        # Generate Assignment Question
        questionNumber = AssignmentQuestion.generateAssignmentQuestionNumber(difficulty.difficultyId,connection)
        assignmentQuestion = AssignmentQuestion(question.questionId,question.question,difficulty.difficultyId,semester.semesterId,questionNumber)
     
        # Store Assignment Question
        assignmentQuestion.storeAssignmentQuestion(connection)

        # Fetch
        result = AssignmentQuestion.getAssignmentQuestionRecord(questionNumber, connection)

        # Assert on question
        self.assertEqual(assignmentQuestion.assignmentQuestionId,result.assignmentQuestionId)
        self.assertEqual(assignmentQuestion.question,result.question)
        self.assertEqual(assignmentQuestion.difficultyId,result.difficultyId)
        self.assertEqual(assignmentQuestion.assignmentQuestionId,result.assignmentQuestionId)
        self.assertEqual(assignmentQuestion.semesterId,result.semesterId)
        self.assertEqual(assignmentQuestion.questionNumber,result.questionNumber)
        
        # Fetch
        result = AssignmentQuestion.getAssignmentQuestionRecordQuestionId(assignmentQuestion.questionId, connection)

        # Assert on question
        self.assertEqual(assignmentQuestion.assignmentQuestionId,result.assignmentQuestionId)
        self.assertEqual(assignmentQuestion.question,result.question)
        self.assertEqual(assignmentQuestion.difficultyId,result.difficultyId)
        self.assertEqual(assignmentQuestion.assignmentQuestionId,result.assignmentQuestionId)
        self.assertEqual(assignmentQuestion.semesterId,result.semesterId)
        self.assertEqual(assignmentQuestion.questionNumber,result.questionNumber)

        # Fetch All Assignment Questions
        result = AssignmentQuestion.getAllAssignmentQuestions(connection)
        self.assertEqual(1,len(result)) # only the one we entered exists

        # Assert on question
        result = result[0]
        self.assertEqual(assignmentQuestion.assignmentQuestionId,result.assignmentQuestionId)
        self.assertEqual(assignmentQuestion.question,result.question)
        self.assertEqual(assignmentQuestion.difficultyId,result.difficultyId)
        self.assertEqual(assignmentQuestion.assignmentQuestionId,result.assignmentQuestionId)
        self.assertEqual(assignmentQuestion.semesterId,result.semesterId)
        self.assertEqual(assignmentQuestion.questionNumber,result.questionNumber)

        # Cleanup
        AssignmentQuestion.destoreAssignmentQuestion(assignmentQuestion.questionId,connection)
        DBBuilder.RemoveQuestion(self,connection,question.questionId)
        DBBuilder.RemoveDifficulty(self,connection,difficulty.difficultyId)
        DBBuilder.RemoveSemester(self,connection,semester.semesterId)

        # Assert cleanup and empty still works
        result = AssignmentQuestion.getAssignmentQuestionRecord(questionNumber, connection)
        self.assertEqual([],result)

if __name__ == '__main__':
    unittest.main()