import unittest
from asm.models import StudentModel

class GpaCalculationTest(unittest.TestCase):
    def test_valid_gpa(self):
        student = StudentModel("John Doe", [("Math", 9.0, 3), ("English", 8.0, 2)])
        self.assertEqual(student.calculate_gpa(), 8.6)

        student = StudentModel("Jane Doe", [("Math", 7.0, 3), ("English", 8.0, 2)])
        self.assertEqual(student.calculate_gpa(), 7.4)

        student = StudentModel("Alice Smith", [("Math", 10.0, 3), ("English", 9.0, 2)])
        self.assertEqual(student.calculate_gpa(), 9.6)

        student = StudentModel("Bob Johnson", [("Math", 6.0, 3), ("English", 7.0, 2)])
        self.assertEqual(student.calculate_gpa(), 6.4)

    def test_empty_grades(self):
        student = StudentModel("Charlie Brown", [])
        self.assertEqual(student.calculate_gpa(), 0)

if __name__ == "__main__":
    unittest.main()