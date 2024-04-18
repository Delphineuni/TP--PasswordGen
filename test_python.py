import unittest, os
import Password_Generator as passgen

class TestSum(unittest.TestCase):
    
    def test_password(self):
        pwlength = [3,4,5,6,7,9,"a"]
        passgen.generatePassword(pwlength)
