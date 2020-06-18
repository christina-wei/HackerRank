#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    arrStr = str(arr[n-1])
    for i in range(1,n):
        arrStr = arrStr + ' ' + str(arr[n-i-1])
    
    print(arrStr)
