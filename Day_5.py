#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    if n>=2 or n<= 20:
        for i in range(1, 11):
            print('{} x {} = {}'.format(n, i, n*i))
