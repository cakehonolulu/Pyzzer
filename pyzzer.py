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
        print("Specify which string options you want (Press ENTER for default options): ")
        m_stropt = input()

        m_strarg = 0

        if len(m_stropt) == 0:
            print("Using default options (Upper(+Lower) case letters, numbers and symbols)...")
            m_strarg = string.ascii_letters + string.digits + string.punctuation;

        if len(m_stropt) > 3:
            print("String options cannot exceed 3 chars!")
            exit()

        #if "a" in m_stropt:
        #    m_strarg += string.ascii_letters
        #    print(f"Args for now: {m_strarg}")

        m_rndstr = ''.join(random.choices(m_strarg, k = int(m_strsz)))
        print(f"Random generated string: {m_rndstr}")
        m_prog = Popen(m_progname, stdin=PIPE)
        m_prog.communicate(m_rndstr.encode())


    if m_fuzzstr == "int":
        m_fuzzalgo = 2

#
# Call main on init
if __name__ == "__main__":
    main()