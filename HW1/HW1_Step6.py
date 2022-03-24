# CS570 - Data Mining - HW1: Frequent Pattern Mining
# Created by: Daniela Chanci Arrubla

'''
THIS CODE IS MY OWN WORK, IT WAS WRITTEN WITHOUT CONSULTING
A TUTOR OR CODE WRITTEN BY OTHER STUDENTS - DANIELA CHANCI ARRUBLA
'''

import math

# Step 6: Re-rank patterns by purity

files_topic = ["topic-0.txt", "topic-1.txt", "topic-2.txt", "topic-3.txt", "topic-4.txt"]
files_patterns = [".\patterns\pattern-0.txt", ".\patterns\pattern-1.txt", ".\patterns\pattern-2.txt", ".\patterns\pattern-3.txt", ".\patterns\pattern-4.txt"]
files_purity = [".\purity\purity-0.txt", ".\purity\purity-1.txt", ".\purity\purity-2.txt", ".\purity\purity-3.txt", ".\purity\purity-4.txt"]

total_documents = []
unique_documents = []

for topic in files_topic:
    f = open(topic, "r")
    titles = f.readlines()
    for title in titles:
        total_documents.append(title.split("\n")[0])

for document in total_documents:
    if document not in unique_documents:
        unique_documents.append(document)

Dttprime = len(unique_documents)

for i in range(len(files_topic)):

    f_topic = open(files_topic[i], "r")
    documents = f_topic.readlines()
    Dt = len(documents)

    f_pattern = open(files_patterns[i], "r")
    patterns = f_pattern.readlines()

    fo = open(files_purity[i], "w")
    final_dict = {}

    for pattern in patterns:

        ft = round(float(pattern.split("\n")[0].split(" ")[0]) * Dt)
        pat = pattern.split("\n")[0].split(" ")[1:]
        print(pat)

        list_ftprime = []

        for j in range(len(files_topic)):
            if i != j:

                fprime_pattern = open(files_patterns[j], "r")
                patterns_prime = fprime_pattern.readlines()
                total_lines = len(patterns_prime)
                ft_prime = 0

                for pattern_prime in patterns_prime:

                    pat_prime = pattern_prime.split("\n")[0].split(" ")[1:]

                    if pat == pat_prime:
                        ft_prime = round(float(pattern_prime.split("\n")[0].split(" ")[0]) * total_lines)

                list_ftprime.append(ft_prime)

        for k in range(len(list_ftprime)):
            list_ftprime[k] = (ft + list_ftprime[k]) / Dttprime


        max_eq = max(list_ftprime)
        purity = math.log(ft/Dt, 2) - math.log(max_eq)

        # Combine purity and support

        measure = round(purity*0.9 + float(pattern.split("\n")[0].split(" ")[0])*0.1, 3)

        final_dict[tuple(pat)] = measure

    patterns_sorted = sorted(final_dict.items(), key=lambda x: x[1], reverse=True)

    for elem in patterns_sorted:
        toprint = str(elem[1]) + " "

        if len(elem[0]) > 1:
            for item in elem[0]:
                if item == elem[0][-1]:
                    toprint += str(item)
                else:
                    toprint += (str(item) + " ")
        else:
            toprint += str(elem[0][0])
        toprint += "\n"
        fo.write(toprint)

    fo.close()


