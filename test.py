import unittest
from datetime import datetime
from Student import Assignment, Event, Student

class TestAssignment(unittest.TestCase):
	def test_getPercentage(self):
		# Test getPercentage with full credit
		assignment = Assignment('Test', 10, 10)
		self.assertEqual(assignment.getPercentage(), 1.0)

		# Test getPercentage with partial credit
		assignment = Assignment('Test', 7, 10)
		self.assertEqual(assignment.getPercentage(), 0.7)

		# Test getPercentage with zero credit
		assignment = Assignment('Test', 0, 10)
		self.assertEqual(assignment.getPercentage(), 0.0)

class TestStudent(unittest.TestCase):
	def setUp(self):
		# Create a Student instance and some test Events and Assignments
		self.student = Student('Test Student', '12345')
		self.event1 = Event('Test Event 1', 'meeting', 0)
		self.event2 = Event('Test Event 2', 'meeting', 0)
		self.event3 = Event('Test Event 3', 'workshop', 10)
		self.assignment1 = Assignment('Test Assignment 1', 7, 10)
		self.assignment2 = Assignment('Test Assignment 2', 9, 10)

	def test_addEvent(self):
		# Test addEvent with a single event
		self.student.addEvent(self.event1)
		self.assertEqual(self.student.countEvents(), 1)

		# Test addEvent with multiple events
		self.student.addEvent([self.event2, self.event3])
		self.assertEqual(self.student.countEvents(), 3)

		# Test addEvent with a non-Event object
		with self.assertRaises(TypeError):
			self.student.addEvent('Not an Event')

	def test_countMeetings(self):
		# Test countMeetings with no meetings
		self.assertEqual(self.student.countMeetings(),  2)

		# Test countMeetings with one meeting
		self.student.addEvent(self.event1)
		self.assertEqual(self.student.countMeetings(), 3)

		# Test countMeetings with multiple meetings
		self.student.addEvent(self.event2)
		self.assertEqual(self.student.countMeetings(), 4)

		# Test countMeetings with a non-meeting event
		self.student.addEvent(self.event3)
		self.assertEqual(self.student.countMeetings(), 4)

	def test_getGrade(self):
		# Test getGrade with no assignments
		self.assertIsNone(self.student.getGrade())

		# Test getGrade with one assignment
		self.student.addAssignment(self.assignment1)
		self.assertAlmostEqual(self.student.getGrade(), 0.7)

		# Test getGrade with multiple assignments
		self.student.addAssignment(self.assignment2)
		self.assertAlmostEqual(self.student.getGrade(), 0.8)

	def test_getLetterGrade(self):
		# Test getLetterGrade with no assignments
		self.assertEqual(self.student.getLetterGrade(), 'B')

		# Test getLetterGrade with a failing grade
		self.student.addAssignment(self.assignment1)
		self.assertEqual(self.student.getLetterGrade(), 'C')

		# Test getLetterGrade with a passing grade
		self.student.addAssignment(self.assignment2)
		self.assertEqual(self.student.getLetterGrade(), 'B')

if __name__ == '__main__':
	unittest.main()
