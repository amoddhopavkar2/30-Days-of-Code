#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    for i in range(1, 11, 1):
        print("{} x {} = {}".format(n, i, n * i))
