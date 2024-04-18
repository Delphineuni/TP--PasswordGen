import unittest, os
import Password_Generator as passgen

class TestSum(unittest.TestCase):
    
    def test_password(self):
        try:
            pwlength = [3,4,5,6,7,9,"a"]
            passgen.generatePassword(pwlength)
        except Exception as e:
            print(e)
    def test_main(self):
        try:
            passgen.main()
        except EOFError:
            print("\nEOF error is expected with empty input in GitHub Action")
        except Exception as e:
            print(e)
