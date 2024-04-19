import unittest
import Password_Generator as passgen

RED = "\033[31;40m"
BLUE = "\033[34;40m"
RESET = "\033[0m"

class TestSum(unittest.TestCase):
    print("\n",RED,"-------------------------------------------------------")
    print(RED," ------- Generated errors will be printed in red -------")
    print(RED," -------------------------------------------------------",RESET)
    def tests(self):
        try:
            print(BLUE,"Testing string:")
            pwlength = [3,"a"]
            passgen.generatePassword(pwlength)
        except Exception as e:
            print(RED,"Value",BLUE,pwlength[1],RED,"raised error",e,RESET)       
        try:
            print(BLUE,"Testing float:")
            pwlength = [3,3.1]
            passgen.generatePassword(pwlength)
        except Exception as e:
            print(RED,"Value",BLUE,pwlength[1],RED,"raised error",e,RESET)
        try:
            print(BLUE,"Testing Integer:")
            pwlength = [3,4]
            passgen.generatePassword(pwlength)
        except Exception as e:
            print(RED,"Value",BLUE,pwlength[1],RED,"raised error",e,RESET)            
    def test_main(self):
        try:
            print(BLUE,"Testing __main__ without input",RESET)
            passgen.main()
        except EOFError:
            print("\n",RED," EOF error is expected with empty input in GitHub Action")
        except Exception as e:
            print(e)