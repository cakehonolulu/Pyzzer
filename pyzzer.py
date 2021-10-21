#!/bin/python3

import sys
from termcolor import colored

import pyfiglet
from pyfiglet import Figlet

import random
import string

from subprocess import Popen, PIPE

# main()
def main():
    m_ascii_fnt = Figlet(font="larry3d")
    m_ascii_banner = m_ascii_fnt.renderText("pyzzer")
    print(colored(m_ascii_banner, "blue"))
    
    if (len(sys.argv) == 1) or (str(sys.argv[1]) == "-h"):
        print("Usage: pyzzer.py [file] [fuzztype]")
        print("Fuzzing Types:")
        print("string - Generates a customizable string and starts the fuzzing process")
        print("int - Generates a customizable integer and starts the fuzzing process")
        exit()

    try:
        m_progname = (f"{str(sys.argv[1])}")
        if not m_progname.startswith("/"):
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
        m_stropt = str(input())

        m_strarg = ""

        if len(m_stropt) == 0:
            print("Using default options (Upper(+Lower) case letters, numbers and symbols)...")
            m_strarg = string.ascii_letters + string.digits + string.punctuation;

        if len(m_stropt) > 3:
            print("String options cannot exceed 3 chars!")
            exit()

        if "a" in m_stropt:
            m_strarg += string.ascii_letters

        if "d" in m_stropt:
            m_strarg += string.digits

        if "p" in m_stropt:
            m_strarg += string.punctuation

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