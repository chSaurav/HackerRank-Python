#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):#ab bc ca
    s = s.split(" ")#["ab","bc","ca"]
    k = [j.capitalize() for j in s] #["Ab","Bc","Ca"]
    return(" ".join(k))#Ab Bc Ca



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
