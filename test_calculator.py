import unittest
from take_input import add

class StringCalculator(unittest.TestCase):
    # 1.1
    def test_EmptyString(self):
        res = add("")
        self.assertEqual(res, 0)
    
    # 1.2
    def test_OneNum(self):
        res = add("2")
        self.assertEqual(res, 2)

    # 1.3
    def test_TwoNums(self):
        res = add("2,3")
        self.assertEqual(res, 5)
    
    # 2
    def test_ManyNums(self):
        res = add("2,3,4,5")
        self.assertEqual(res, 14)

    # 3
    def test_Alpha(self):
        self.assertEqual(add("1,2,a,b"), 6)

    # 4, 5
    def test_Neg(self):
        res = add("2,3,-4,-5")
        self.assertEqual(res, 14)

    # 6
    def test_IgnoreBig(self):
        res = add("2,3,1002,1000")
        self.assertEqual(res, 1005)

    # 7
    def test_HandleNewLine(self):
        res = add("2\n3,5")
        self.assertEqual(res, 10)


if __name__ == '__main__':
    unittest.main()