import unittest, os
import Password_Generator as passgen

RED = "\033[1;31;40m"
RESET = "\033[0m"

class TestSum(unittest.TestCase):
    print(RED,"-------------------------------------------------------")
    print(RED,"------- Generated errors will be printed in red -------")
    print(RED,"-------------------------------------------------------",RESET)
    def test_password(self):
        try:
            pwlength = [3,4,5,6,7,9,"a"]
            passgen.generatePassword(pwlength)
        except Exception as e:
            print(RED, e)
    def test_main(self):
        try:
            passgen.main()
        except EOFError:
            print("\n",RED," EOF error is expected with empty input in GitHub Action")
        except Exception as e:
            print(e)