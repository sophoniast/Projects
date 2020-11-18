import math
import os
import random
import re
import sys

if __name__ == '__main__':
    try:
        N = int(input())

        if N >= 1 or N <= 100:
            if N % 2 == 1:
                print("Weird")
            else:
                if 2 <= N <= 5:
                    print("Not Weird")
                else:
                    if 6 <= N <= 20:
                        print("Weird")
                    else:
                        if N > 20:
                            print("Not Weird")
        else:
            print("Please enter an integer between 1 and 100")
    except:
        print("please enter a proper integer")