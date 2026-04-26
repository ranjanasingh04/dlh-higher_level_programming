#!/usr/bin/python3
import sys

if __name__ == "__main__":
    counter = len(sys.argv) - 1

    if counter == 0:
        print("0 arguments.")
    elif counter == 1:
        print("1 argument:")
    else:
        print(f"{counter} arguments:")

    for i in range(1, len(sys.argv)):
        print(f"{i}: {sys.argv[i]}")
