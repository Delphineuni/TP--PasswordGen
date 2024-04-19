import unittest
import Password_Generator as passgen

RED = "\033[1;31;40m"
BLUE = "\033[1;34;40m"
RESET = "\033[0m"

class TestSum(unittest.TestCase):
    #print("\n",RED,"-------------------------------------------------------")
    #print(RED," ------- Generated errors will be printed in red -------")
    #print(RED," -------------------------------------------------------",RESET)
    def test_string(self):
        pwlength = [3,"a"]
        passgen.generatePassword(pwlength)
    def test_float(self):
        pwlength = [3,3.1]
        passgen.generatePassword(pwlength)
    def test_integer(self):
        pwlength = [3,4]
        passgen.generatePassword(pwlength)
    #def test_password(self):
    #    pwlength = [3,4,5,6,7,9,"a",3.1]
    #    exceptions = {}
    #    for pw in pwlength:
    #            try:
    #                pws=[pw,3]
    #                passgen.generatePassword(pws)
    #            except Exception as e:
    #                exceptions[pw] = e
    #    print('')
    #    for exception in exceptions:
    #        print(RED,"Value",BLUE,exception,RED,"raised error",exceptions[exception],RESET)
    def test_main(self):
        try:
            passgen.main()
        except EOFError:
            print("\n",RED," EOF error is expected with empty input in GitHub Action")
        except Exception as e:
            print(e)