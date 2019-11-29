#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    if n >=1 and n <= 10000000:
        print (max(map(len, format(n, 'b').split('0')))) 
