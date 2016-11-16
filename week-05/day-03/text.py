
import exercise_01, exercise_02, exercise_03
import unittest

class Test_your_name_work(unittest.TestCase):

    def test_null_divide(self):
        self.assertEqual(exercise_01.divide_ten(0), 'fail')

    def test_string(self):
       self.assertEqual(exercise_01.divide_ten('sgsfg'), 'Number please!')

    def test_file_exists(self):

        self.assertEqual(exercise_02.text_lines('fil.txt'), 0)

    def test_wrong_birthdate(self):
        self.assertRaises(ValueError, exercise_03.Person,'Jozsi', 2017)

    def test_vaild_birtdate(self):
        i = exercise_03.Person('Jozsi', 2016)
        self.assertEqual(i.name, 'Jozsi')
        self.assertEqual(i.birth_date, 2016)

if __name__ == '__main__':
    unittest.main()
