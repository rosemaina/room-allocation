import unittest
from fellow import Fellow

class FellowTests(unittest.TestCase):

    def setUp(self):
        self.person = Fellow("JANE DOE", "Y", gender=None)

    def test_raises_error_if_gender_is_not_valid(self):
        with self.assertRaises(ValueError):
            Fellow("JOHN DOE", "N", gender="binklmskl")

    def test_raises_error_if_wants_living_is_not_valid(self):
        with self.assertRaises(ValueError):
            Fellow("JOHN DOE", "gjhklms", gender='M')

    def test_repr_returns_correct_values(self):
        self.assertEqual(str(self.person), "JANE DOE (FELLOW)")
        # test again with gender specified:
        self.person = Fellow("JANE DOE", "Y", gender='F')
        self.assertEqual(str(self.person), "JANE DOE (FELLOW F)")



if __name__ == '__main__':
    unittest.main()
