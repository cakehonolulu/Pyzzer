#!/bin/python3

import subprocess
import os
import sys

# main()
def main():
    print("Pyfuzzer - A simple Python Program Fuzzer")
    print(f"Command line arguments: {str(sys.argv[1])}")
    os.system(str(sys.argv[1]))

# Call main on init
if __name__ == "__main__":
    main()