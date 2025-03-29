import unittest
from asm.models import StudentModel

class CreateStudentTest(unittest.TestCase):
    def test_valid_student_creation(self):
        student = StudentModel("John Doe", [("Math", 9.0, 3), ("English", 8.0, 2)])
        self.assertEqual(student.get_name(), "John Doe")
        self.assertEqual(student.get_grades(), [("Math", 9.0, 3), ("English", 8.0, 2)])
        self.assertEqual(student.calculate_gpa(), 8.6)

        student = StudentModel("Jane Doe", [("Math", 7.0, 3), ("English", 8.0, 2)])
        self.assertEqual(student.get_name(), "Jane Doe")
        self.assertEqual(student.get_grades(), [("Math", 7.0, 3), ("English", 8.0, 2)])
        self.assertEqual(student.calculate_gpa(), 7.4)

        student = StudentModel("Alice Smith", [("Math", 10.0, 3), ("English", 9.0, 2)])
        self.assertEqual(student.get_name(), "Alice Smith")
        self.assertEqual(student.get_grades(), [("Math", 10.0, 3), ("English", 9.0, 2)])
        self.assertEqual(student.calculate_gpa(), 9.6)

    def test_invalid_student_creation(self):
        with self.assertRaises(ValueError):
            StudentModel("", [("Math", 9.0, 3)])

        with self.assertRaises(ValueError):
            StudentModel("John Doe", [("Math", 9.0, -1)])

        with self.assertRaises(ValueError):
            StudentModel("John Doe", [("Math", 9.0, 3), ("English", 8.0, 0)])

    def test_add_valid_grade(self):
        student = StudentModel("John Doe", [("Math", 9.0, 3)])
        student.add_grade(("English", 8.0, 2))
        self.assertEqual(student.get_grades(), [("Math", 9.0, 3), ("English", 8.0, 2)])
        self.assertEqual(student.calculate_gpa(), 8.6)

    def test_add_invalid_grade(self):
        student = StudentModel("John Doe", [("Math", 9.0, 3)])
            
        with self.assertRaises(ValueError):
            student.add_grade(("", 8.0, 2))

        with self.assertRaises(ValueError):
            student.add_grade(("English", -1, 2))

        with self.assertRaises(ValueError):
            student.add_grade(("English", 8.0, -1))