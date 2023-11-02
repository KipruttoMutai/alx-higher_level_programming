#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    a = len(sys.argv)
    if a == 1:
        print("{} arguments.".format(a - 1))
    elif a == 2:
        print("{} argument:".format(a - 1))
    else:
        print("{} arguments:".format(a - 1))
    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]))
