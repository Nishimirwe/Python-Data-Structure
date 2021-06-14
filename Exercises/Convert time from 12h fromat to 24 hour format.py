#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    if s[-2]=="P":
        n=s[:2]
        n=int(n)
        if n!=12:
            n=n+12
        ss=str(n)+s[2:-2]
        return ss
    else:
        n=s[:2]
        n=int(n)
        ss=s[2:-2]
        if n==12:
            n="00"
            ss=n+ss
            return ss
        else:
            if n<10:
                n="0"+str(n)
                return n+ss
            else:
                return str(n)+ss
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()

