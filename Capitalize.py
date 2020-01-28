#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    s = s.split(" ")
    fname = s[0]
    lname = s[1]
    fname = fname.capitalize()
    lname = lname.capitalize()
    fullname = fname + " " + lname
    return(fullname)



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
