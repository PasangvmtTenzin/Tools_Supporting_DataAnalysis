#!/usr/bin python3

import sys

if __name__ == "__main__":
    print(", ".join(repr(x) for x in sys.argv[1:]))
