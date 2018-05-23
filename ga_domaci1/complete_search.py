# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 00:41:21 2018

@author: Radoica Draškić
"""

import math

INTERVAL_LEFT_END = -20
INTERVAL_RIGHT_END = 20


def f(x1, x2):
    return -x1 * math.sin(math.sqrt(abs(x1 - (x2 + 9)))) - \
           (x2 + 9) * math.sin(math.sqrt(abs(x2 + 0.5 * x1 + 9)))


if __name__ == '__main__':
    dimension = 100
    best_complete = 0
    for i in range(dimension + 1):
        for j in range(dimension + 1):
            x1 = INTERVAL_LEFT_END + (\
                    INTERVAL_RIGHT_END - INTERVAL_LEFT_END) * i / dimension
            x2 = INTERVAL_LEFT_END + (\
                    INTERVAL_RIGHT_END - INTERVAL_LEFT_END) * j / dimension
                    
            if best_complete > f(x1, x2):
                best_complete = f(x1, x2)
                
    print(best_complete)
