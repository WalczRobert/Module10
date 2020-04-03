"""
Robert Walczak
"""

import unittest
from class_definitions import student_class as sc

class MyStudentClass(unittest.TestCase):
    def setUp(self):
        self.student = sc.Student('Walczak', 'Robert', 'Data_Analyis', 3.6)

    def tearDown(self):
        del self.student

    def test_object_created_required_attributes(self):
        self.assertEqual(self.student.last_name, 'Walczak')
        self.assertEqual(self.student.first_name, 'Robert')

    def test_object_created_all_attributes(self):
        student = sc.Student('Walczak', 'Robert', 'Data_Analyis', 3.6)
        assert student.last_name == 'Walczak'
        assert student.first_name == 'Robert'
        assert student.major == 'Data_Analyis'
        assert student.gpa == 3.6

    def test_student_str(self):
        self.assertEqual(str(self.student), 'Walczak, Robert has major in Data_Analyis with gpa: 3.6')

    def test_object_not_created_error_last_name(self):
        with self.assertRaises(ValueError):
            s = sc.Student('567', 'Robert', 'Data_Analyis', 3.6)

    def test_object_not_created_error_first_name(self):
        with self.assertRaises(ValueError):
            s = sc.Student('Walczak', '567', 'Data_Analyis', 3.6)

    def test_object_not_created_error_major(self):
        with self.assertRaises(ValueError):
            s = sc.Student('Walczak', 'Robert', '567', 3.6)

    def test_object_not_created_error_gpa(self):
        with self.assertRaises(ValueError):
            s = sc.Student('Walczak', 'Robert', 'Data_Analyis', 'None')

    def test_object_not_created_error_gpa_range_check(self):
        with self.assertRaises(ValueError):
            s = sc.Student('Walczak', 'Robert', 'Data_Analyis', 3.6)

if __name__ == '__main__':
    unittest.main()
