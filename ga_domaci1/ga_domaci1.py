# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 00:41:21 2018

@author: Radoica Draškić
"""

import math
import random
import matplotlib.pyplot as plt

from numpy import mean

HROMOZOME_NUMBERS = [20, 100, 150]
NUMBER_OF_GENERATIONS = 100
NUMBER_OF_BITS = 40
INTERVAL_LEFT_END = -20
INTERVAL_RIGHT_END = 20
MUTATION_RATE = 3 # in percents
MARKERS = {20: '+', 100: 'o', 150: '^'}
COLORS = {20: 'r', 100: 'y', 150: 'b'}
BEST_COMPLETE_SEARCH = -25.230531030884485

"""Function to minimize
"""
def f(x1, x2):
    return -x1 * math.sin(math.sqrt(abs(x1 - (x2 + 9)))) - \
           (x2 + 9) * math.sin(math.sqrt(abs(x2 + 0.5 * x1 + 9)))


"""Creates offspring from provided
hromozomes
"""
def reproduce(a, b):
    i = random.randint(0, NUMBER_OF_BITS)
    c = a[:i] + b[i:]
    d = b[:i] + a[i:]
    return [c, d]

"""Mutates a hromozome
"""
def mutate(a):
    for i in range(len(a)):
        x = random.randint(1, 100)
        if x <= MUTATION_RATE:
            a[i] = 1 - a[i]
    return a


"""Converts binary hromozome
into real number
"""
def hromozome_to_number(a):
    x = 0
    one = 1
    for i in range(len(a) // 2):
        if a[i] == 1:
            x = x + one
        one = one * 2
    x1 = INTERVAL_LEFT_END + x * (\
            INTERVAL_RIGHT_END - INTERVAL_LEFT_END) / (one - 1)

    x = 0
    one = 1
    for i in range(len(a) // 2, len(a)):
        if a[i] == 1:
            x = x + one
        one = one * 2
    x2 = INTERVAL_LEFT_END + x * (\
            INTERVAL_RIGHT_END - INTERVAL_LEFT_END) / (one - 1)

    return [x1, x2]


"""Used for evaluating fitness
of a given hromozome
"""
def custom_key(a):
    b = hromozome_to_number(a)
    
    return f(b[0], b[1])


if __name__ == '__main__':
    
    print('NUMBER_OF_GENERATIONS:', NUMBER_OF_GENERATIONS)
    print('NUMBER_OF_BITS:       ', NUMBER_OF_BITS)
    print('MUTATION_RATE         ', MUTATION_RATE)
    print('\n\n')
    
    the_best_hromozome = 0
    for number_of_hromozomes in HROMOZOME_NUMBERS:
        print('#HROMOZOMES: ', number_of_hromozomes)
        print()
        
        best_hromozome = 0
        best_hromozomes = []
        for k in range(1, 11):
            hromozomes = []
            # create population
            # first half of bits is encoding x1
            # second hal is encoding x2
            for i in range(number_of_hromozomes):
                hromozome = []
                for j in range(NUMBER_OF_BITS):
                    hromozome.append(random.randint(0, 1))
                hromozomes.append(hromozome)
            
            # run genetic algorithm
            for i in range(NUMBER_OF_GENERATIONS):
                hromozomes.sort(key=custom_key)
               
                h_sum = 0
                for i in range(len(hromozomes)):
                    h_sum = h_sum + custom_key(hromozomes[i])
               
                # create new hromozomes
                hromozomes = hromozomes[:len(hromozomes) // 2]
                for i in range(len(hromozomes) // 2):
                    hromozomes.extend(reproduce(hromozomes[2 * i], hromozomes[2 * i + 1]))
             
                if number_of_hromozomes % 2 == 1:
                    hromozomes.append(hromozomes[number_of_hromozomes // 2 + 1])
                
                # mutate new hromozomes
                for i in range(len(hromozomes)//2, len(hromozomes)):
                    hromozomes[i] = mutate(hromozomes[i])
            
            best_hromozomes.append(custom_key(hromozomes[0]))
            
            # average hromozome
            average = mean([custom_key(hromozome) for hromozome in hromozomes])
            
            print('ITERATION', k, ':')
            print('    BEST:   ', custom_key(hromozomes[0]))
            print('    AVERAGE:', average)
            
        best_hromozome = best_hromozomes[0]
        for i in range(1, len(best_hromozomes)):
            if best_hromozomes[i] < best_hromozome:
                best_hromozome = best_hromozomes[i]
        
        if the_best_hromozome > best_hromozome:
            the_best_hromozome = best_hromozome
        
        print('\nBEST HROMOZOME: ', best_hromozome, '\n\n')
        
        plt.plot(range(1, 11), best_hromozomes, 
                 label='$hromozomes = {i}$'.format(i=number_of_hromozomes),
                 marker=MARKERS[number_of_hromozomes], linestyle='', 
                 color=COLORS[number_of_hromozomes])
    
    plt.legend(loc='best')
    plt.title('Best hromozomes over 10 iterations')
    plt.savefig('ga_domaci1.png', dpi=300)
    
    print('COMPLETE SEARCH:', BEST_COMPLETE_SEARCH)            
    print('DIFFERENCE:     ', BEST_COMPLETE_SEARCH - the_best_hromozome)
