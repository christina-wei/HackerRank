#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    binary = []
    max_len = 0
    tmp_len = 0

    while(n > 0):

        remainder = n%2
        n = n//2
        binary.insert(0,remainder)

        if remainder == 1:
            tmp_len += 1
        else:
            max_len = max(max_len, tmp_len)
            tmp_len = 0
    
    max_len = max(max_len, tmp_len)
    print(max_len)
