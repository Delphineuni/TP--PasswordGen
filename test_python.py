import unittest, sys
from io import StringIO
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
        f = StringIO("\n\n")
        sys.stdin = f
        passgen.main()
        f.close()
    def test_main_simulated(self):
        print(BLUE,"Testing __main__ with simulated input",RESET)
        f = StringIO("3\n3\n12\n154")
        sys.stdin = f
        passgen.main()
        f.close()