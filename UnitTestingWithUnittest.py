import unittest


assert 9 * 6 == 54, "nah its 54"

def test_one():

    assert 5 * 5 == 25, "must be 25"

def test_two():

    assert 5 * 4 == 20, "must be 20"


if __name__ == "__main__":

    test_one()
    test_two()

    print("all the test good ")






class MyTestClass(unittest.TestCase):

    def test_one(self):

        self.assertTrue(100 > 50 , "Must be True")

    def test_two(self):

        self.assertEqual(5 * 5, 25, "Must be 25")

    def test_three(self):

        self.assertGreater(100, 22, "Must be True")


if __name__ == "__main__":

    unittest.main()




