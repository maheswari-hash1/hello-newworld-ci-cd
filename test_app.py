
import unittest
from app import hello_newworld
 
class TestApp(unittest.Testcase):
    def test_hello_newworld(self):
        self.assertEqual(hello_newworld(), "Hello, world")

if __name__ == '__main__':
    unittest.main()