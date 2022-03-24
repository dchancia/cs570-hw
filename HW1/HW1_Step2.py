# CS570 - Data Mining - HW1: Frequent Pattern Mining
# Created by: Daniela Chanci Arrubla

'''
THIS CODE IS MY OWN WORK, IT WAS WRITTEN WITHOUT CONSULTING
A TUTOR OR CODE WRITTEN BY OTHER STUDENTS - DANIELA CHANCI ARRUBLA
'''

# Step 2.1: Generate a Dictionary

# Open and read the source file
f1 = open("paper.txt", "r")
titles = f1.readlines()

# Initialize dictionary
dictionary = []

# Create dictionary
for title in titles:
    for term in title.split("\t")[1].split("\n")[0].split(" "):
        # Check that the term is not already included in the dictionary
        if term not in dictionary:
            dictionary.append(term)

print("There are " + str(len(dictionary)) + " terms in the dictionary")

# Save dictionary
f2 = open("vocab.txt", "w")
for term in dictionary:
    f2.write(term + "\n")
f2.close()

# Step 2.2: Tokenize plain text by dictionary

# Initialize tokenized dictionary
tok_dictionary = []

# Loop through each title
for title in titles:
    indexes = []
    counts = []
    # Loop through each term of the title
    for term in title.split("\t")[1].split("\n")[0].split(" "):
        # Check if the term is in the dictionary
        if term in dictionary:
            # Check if the term is repeated within the title
            if dictionary.index(term) not in indexes:
                indexes.append(dictionary.index(term))
                counts.append(1)
            else:
                counts[indexes.index(dictionary.index(term))] += 1
    # Organized required format for the tokenized dictionary
    tok_title = str(len(indexes))
    for i in range(len(indexes)):
        tok_title += " " + (str(indexes[i]) + ":" + str(counts[i]))
    tok_dictionary.append(tok_title)

# Save tokenized dictionary
f3 = open("title.txt", "w")
for title in tok_dictionary:
    f3.write(title + "\n")
f3.close()




