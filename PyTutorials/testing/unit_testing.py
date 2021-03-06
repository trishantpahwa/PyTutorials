import unittest

'''
Unit Test is to basically test functions of a particular class or a module.
It tests by using 3 assertion methods:
1.) To check whether both values are equal or not, assertEqual
2.) To check whether the value is true or false, assertTrue/assertFalse
3.) To check whether the function raises an exception or not, assertRaise
'''

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        self.assertRaises(TypeError):
            s.split(2)
        

if __name__ == '__main__':
    unittest.main()