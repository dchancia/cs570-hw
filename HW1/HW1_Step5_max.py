# CS570 - Data Mining - HW1: Frequent Pattern Mining
# Created by: Daniela Chanci Arrubla

'''
THIS CODE IS MY OWN WORK, IT WAS WRITTEN WITHOUT CONSULTING
A TUTOR OR CODE WRITTEN BY OTHER STUDENTS - DANIELA CHANCI ARRUBLA
'''

'''
For Step 5, I use the previous output
'''

import os

for idx in range(5):

    fi = open(os.path.join(".", "patterns", "pattern-" + str(idx) + ".txt"), "r")
    fo = open(os.path.join(".", "max", "max-" + str(idx) + ".txt"), "w")
    patterns = fi.readlines()

    list_patterns = []
    list_terms = []
    list_support = []
    non_max = []
    non_max_unique = []

    for pattern in patterns:
        list_patterns.append((pattern.split("\n")[0].split(" ")[0], pattern.split("\n")[0].split(" ")[1:]))
        list_terms.append(pattern.split("\n")[0].split(" ")[1:])
        list_support.append(pattern.split("\n")[0].split(" ")[0])

    for i in range(len(list_terms)):
        for j in range(len(list_terms)):
            if i != j:
                if (set(list_terms[i]).issubset(set(list_terms[j]))):
                    non_max.append((list_support[i], list_terms[i]))

    for elems in non_max:
        if elems not in non_max_unique:
            non_max_unique.append(elems)

    for item in non_max_unique:
        list_patterns.remove(item)
   
    for patt in list_patterns:
        toprint = str(patt[0]) + " "
        if len(patt[1]) == 1:
            toprint += str(patt[1][0])
        else:
            for elem in patt[1]:
                if elem == patt[1][-1]:
                    toprint += str(elem)
                else:
                    toprint += (str(elem) + " ")
        toprint += "\n"
        fo.write(toprint)

    fo.close()