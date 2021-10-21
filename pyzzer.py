#!/bin/python3

import sys
from subprocess import Popen, PIPE

# main()
def main():
    print("Pyfuzzer - A simple Python Program Fuzzer")
    print(f"Command line arguments: {str(sys.argv[1])}")

    m_progname = (f"./{str(sys.argv[1])}")

    m_fuzzstr = (f"{str(sys.argv[2])}")

    print(f"Program name: {m_progname}")
    print(f"Fuzzing string: {m_fuzzstr}")

    m_prog = Popen(m_progname, stdin=PIPE)
    m_prog.communicate(m_fuzzstr.encode())

# Call main on init
if __name__ == "__main__":
    main()