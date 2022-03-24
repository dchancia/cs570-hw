# CS570 - Data Mining - HW1: Frequent Pattern Mining
# Created by: Daniela Chanci Arrubla

'''
THIS CODE IS MY OWN WORK, IT WAS WRITTEN WITHOUT CONSULTING
A TUTOR OR CODE WRITTEN BY OTHER STUDENTS - DANIELA CHANCI ARRUBLA
'''

import os

# Submission: Generate a mapping for all the files

folders = ["patterns", "closed", "max", "purity"]

f = open("vocab.txt", "r")
vocab = f.readlines()

dictionary = []

for term in vocab:
    dictionary.append(term.split("\n")[0])

base_path = "."

for i in range(len(folders)):
    for file in os.listdir(os.path.join(base_path, folders[i])):

        fi = open(os.path.join(base_path, folders[i], str(file)), "r")
        patterns = fi.readlines()
        save_file = os.path.join(base_path, folders[i], str(file) + ".phrase")
        fo = open(save_file, "w")


        for elem in patterns:
            tosave = str(elem.split("\n")[0].split(" ")[0]) + " "
            for term in elem.split("\n")[0].split(" ")[1:]:
                index = int(term)
                if len(elem.split("\n")[0].split(" ")[1:]) > 1:
                    if term == elem.split("\n")[0].split(" ")[1:][-1]:
                        tosave += dictionary[index]
                    else:
                        tosave += (dictionary[index] + " ")
                else:
                    tosave += dictionary[index]
            tosave += "\n"
            fo.write(tosave)

        fo.close()



