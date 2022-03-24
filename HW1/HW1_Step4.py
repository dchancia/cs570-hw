# CS570 - Data Mining - HW1: Frequent Pattern Mining
# Created by: Daniela Chanci Arrubla

'''
THIS CODE IS MY OWN WORK, IT WAS WRITTEN WITHOUT CONSULTING
A TUTOR OR CODE WRITTEN BY OTHER STUDENTS - DANIELA CHANCI ARRUBLA
'''

'''
For Step 4, I chose the Apriori algorithm, and used the pseudocode found in page 253 of the book as a guide
for this code.
'''

from itertools import combinations
import os

# Step 4: Mining frequent patterns for each topic

for idx in range(5):

    fi = open("topic-" + str(idx) + ".txt", "r")
    titles = fi.readlines()
    total_lines = len(titles)

    C1 = {}
    L1 = {}
    exc = []
    min_sup = 0.01

    for title in titles:
        for term in title.split("\n")[0].split(" ")[:-1]:
            if term not in C1:
                C1[term] = 1
            else:
                C1[term] += 1

    for elem in C1:
        C1[elem] = round(C1[elem]/total_lines, 3)

    for term in C1:
        if C1[term] >= min_sup:
            L1[term] = C1[term]
        else:
            exc.append([term])

    L_dict = [L1]
    L = [list(L1.keys())]
    for i in range(len(L[0])):
        L[0][i] = [L[0][i]]
    excluded = [exc]
    k = 1

    while (len(L[k-1]) > 0):
        C_old = []
        C_comb = []
        C = []
        C_rem = []
        C_final = {}
        L_next = {}
        exc_next = []
        for i in range(len(L[k-1])):
            for j in range(i + 1, len(L[k-1])):
                C_old.append(set(L[k-1][i]).union(set(L[k-1][j])))
        for elem in C_old:
            for i in combinations(elem,k+1):
                C_comb.append(set(i))
        for elem in C_comb:
            if elem not in C:
                C.append(elem)
        for itemset in C:
            for element in excluded[k-1]:
                if set(element).issubset(itemset):
                    C_rem.append(itemset)
                    break
        for element in C_rem:
            C.remove(element)
        for title in titles:
            create_set = set(title.split("\n")[0].split(" ")[:-1])
            for itemset in C:
                if itemset.issubset(create_set):
                    if tuple(itemset) not in C_final:
                        C_final[tuple(itemset)] = 1
                    else:
                        C_final[tuple(itemset)] += 1
        for elem in C_final:
            C_final[elem] = round(C_final[elem]/total_lines, 3)
        for itemset in C_final:
            if C_final[itemset] >= min_sup:
                L_next[itemset] = C_final[itemset]
            else:
                temp = []
                for elem in itemset:
                    temp.append(elem)
                exc_next.append(temp)
        L_dict.append(L_next)
        L.append(list(L_next.keys()))
        excluded.append(exc_next)

        k += 1

    patterns_dict = {}
    for dictionary in L_dict[:-1]:
        for terms in dictionary.keys():
            patterns_dict[terms] = dictionary[terms]

    patterns_sorted = sorted(patterns_dict.items(), key=lambda x:x[1], reverse=True)

    fo = open(os.path.join(".", "patterns", "pattern-" + str(idx) + ".txt"), "w")
    for pattern in patterns_sorted:
        if type(pattern[0]) is tuple:
            toprint = str(pattern[1]) + " "
            for term in pattern[0]:
                if term == pattern[0][-1]:
                    toprint += term
                else:
                    toprint += (term + " ")
        else:
            toprint = str(pattern[1]) + " " + pattern[0]
        toprint += "\n"
        fo.write(toprint)
    fo.close()

