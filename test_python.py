import unittest, os
import Password_Generator as passgen

class TestSum(unittest.TestCase):
    
    def test_password(self):
        pwlength = [3,4,5,6,7,9,"a"]
        passgen.generatePassword(pwlength)
    def test_main(self):
        try:
            passgen.main()
        except EOFError:
            print("Expected EOF error with input")
        except Exception as e:
            print(e)
