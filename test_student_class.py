"""
Robert Walczak
"""

import unittest
from class_definitions import student_class as sc

class MyStudentClass(unittest.TestCase):
    def setUp(self):
        self.student = sc.Student('Blankenship', 'Ryan', 'Web Development', 2.0)

    def tearDown(self):
        del self.student

    def test_object_created_required_attributes(self):
        self.assertEqual(self.student.last_name, 'Blankenship')
        self.assertEqual(self.student.first_name, 'Ryan')

    def test_object_created_all_attributes(self):
        student = sc.Student('Blankenship', 'Ryan', 'Web Development', 2.0)
        assert student.last_name == 'Blankenship'
        assert student.first_name == 'Ryan'
        assert student.major == 'Web Development'
        assert student.gpa == 2.0

    def test_student_str(self):
        self.assertEqual(str(self.student), 'Blankenship, Ryan has major Web Development with gpa: 2.0')

    def test_object_not_created_error_last_name(self):
        with self.assertRaises(ValueError):
            s = sc.Student('123', 'Ryan', 'Web Development', 2.0)

    def test_object_not_created_error_first_name(self):
        with self.assertRaises(ValueError):
            s = sc.Student('Blankenship', '123', 'Web Development', 2.0)

    def test_object_not_created_error_major(self):
        with self.assertRaises(ValueError):
            s = sc.Student('Blankenship', 'Ryan', '123', 2.0)

    def test_object_not_created_error_gpa(self):
        with self.assertRaises(ValueError):
            s = sc.Student('Blankenship', 'Ryan', 'Web Development', 'None')

    def test_object_not_created_error_gpa_range_check(self):
        with self.assertRaises(ValueError):
            s = sc.Student('Blankenship', 'Ryan', 'Web Development', 4.0)

if __name__ == '__main__':
    unittest.main()
