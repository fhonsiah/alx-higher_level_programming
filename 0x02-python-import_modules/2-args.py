#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    n = len(argv)
    if n == 0:
        print("Number of argument(s): 0.")
    else:
        print("Number of argument(s):", n)
        print("Argument(s):")
        for i, arg in enumerate(argv):
            print(i+1, ":", arg)
