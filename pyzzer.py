#!/bin/python3

import sys
from subprocess import Popen, PIPE

import random
import string

# main()
def main():
    print("Pyfuzzer - A simple Python Program Fuzzer")

    try:
        m_progname = (f"./{str(sys.argv[1])}")
        print(f"Target: {str(sys.argv[1])}")
    except IndexError:
        print(f"No file to fuzz, exiting...")
        exit()
    else:
        pass

    try:
        m_fuzzstr = str(sys.argv[2])
        print(f"Fuzzing method: {sys.argv[2]}")
    except IndexError:
        print(f"No fuzzing method given, exiting...")
        exit()
    else:
        pass

    if m_fuzzstr == "string":
        m_fuzzalgo = 1
        print("Input the string size: ")
        m_strsz = input()
        m_rndstr = ""
        m_rndstr = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k = int(m_strsz)))
        print(f"Random generated string: {m_rndstr}")


    if m_fuzzstr == "int":
        m_fuzzalgo = 2

    m_prog = Popen(m_progname, stdin=PIPE)
    #m_prog.communicate(m_fuzzstr.encode())
#
# Call main on init
if __name__ == "__main__":
    main()