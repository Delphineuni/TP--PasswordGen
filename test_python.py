import unittest
import Password_Generator as passgen

RED = "\033[31;40m"
BLUE = "\033[34;40m"
RESET = "\033[0m"

class TestSum(unittest.TestCase):
    def test_string(self):
        print(BLUE,"Testing string:")
        pwlength = [3,"a"]
        passgen.generatePassword(pwlength)   
    def test_float(self):
        print(BLUE,"Testing float:")
        pwlength = [3,3.1]
        passgen.generatePassword(pwlength)
    def test_int(self):
        print(BLUE,"Testing Integer:")
        pwlength = [3,4]
        passgen.generatePassword(pwlength)          
    def test_main(self):
        print(BLUE,"Testing __main__ without input",RESET)
        passgen.main()