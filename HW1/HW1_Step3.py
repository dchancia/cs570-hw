# CS570 - Data Mining - HW1: Frequent Pattern Mining
# Created by: Daniela Chanci Arrubla

'''
THIS CODE IS MY OWN WORK, IT WAS WRITTEN WITHOUT CONSULTING
A TUTOR OR CODE WRITTEN BY OTHER STUDENTS - DANIELA CHANCI ARRUBLA
'''

# Step 3.2: Reorganize the terms by topic

# Read LDA output
f4 = open("./result/word-assignments.dat", "r")
titles = f4.readlines()

# Open files to save to organize terms by topic
f_topic0 = open("topic-0.txt", "w")
f_topic1 = open("topic-1.txt", "w")
f_topic2 = open("topic-2.txt", "w")
f_topic3 = open("topic-3.txt", "w")
f_topic4 = open("topic-4.txt", "w")

# Loop through the titles
for title in titles:
    string_0 = ""
    string_1 = ""
    string_2 = ""
    string_3 = ""
    string_4 = ""

    # Re-organize the different terms of each title according to the category
    for term in title.split("\n")[0].split(" ")[1:]:
        if term.split(":")[1] == "00":
            string_0 += (term.split(":")[0] + " ")
        elif term.split(":")[1] == "01":
            string_1 += (term.split(":")[0] + " ")
        elif term.split(":")[1] == "02":
            string_2 += (term.split(":")[0] + " ")
        elif term.split(":")[1] == "03":
            string_3 += (term.split(":")[0] + " ")
        else:
            string_4 += (term.split(":")[0] + " ")

    # Save information to the files
    if len(string_0) > 0:
        f_topic0.write(string_0 + "\n")
    if len(string_1) > 0:
        f_topic1.write(string_1 + "\n")
    if len(string_2) > 0:
        f_topic2.write(string_2 + "\n")
    if len(string_3) > 0:
        f_topic3.write(string_3 + "\n")
    if len(string_4) > 0:
        f_topic4.write(string_4 + "\n")

# Close files
f_topic0.close()
f_topic1.close()
f_topic2.close()
f_topic3.close()
f_topic4.close()