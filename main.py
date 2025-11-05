import numpy as np
import argparse
from utils import question

@question
def q1(debug_mode=False):
    print("Make a numpy array with elements 1,3,7,8")
    userInput = input()
    try:
        if (eval(userInput) == np.array([1,3,7,8])).all():
            return True
    except Exception as e:
        print("Error: ",e) if debug_mode else None
    return False

@question
def q2(debug_mode=False):
    print("Make a numpy array with elements 1-10")
    print(np.arange(1,11))
    userInput = input()
    try:
        if (eval(userInput) == np.arange(1,11)).all():
            return True
    except Exception as e:
        print("Error: ",e) if debug_mode else None
    return False

def main():
    parser = argparse.ArgumentParser(description="Try numpy question")

    parser.add_argument("-q", "--question", type=int, default=1, help="Question number to try")
    parser.add_argument("-r", "--random", type=int, default=1, help="Number of questions to try")
    parser.add_argument("-a", "--all", action="store_true",help="All questions")
    parser.add_argument("-d", "--debug", action="store_true", help="Debug mode")

    args = parser.parse_args()

    debug_mode = args.debug

    try:
        eval(f'q{args.question}(debug_mode)')
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
