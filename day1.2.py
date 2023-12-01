import pandas as pd
import re

strings = pd.read_csv("data1.2.lst", header=None, delim_whitespace=True)[0].values.tolist()

print(strings)

# Part 1
replacements = [
    ("one", 1),
    ("two", 2),
    ("three", 3),
    ("four", 4),
    ("five", 5),
    ("six", 6),
    ("seven", 7),
    ("eight", 8),
    ("nine", 9),
]

onlydigits = []
for i in range(len(strings)):
    accu = ""
    rowstring = strings[i]
    j = 0
    while j < len(rowstring):
        found = False
        if rowstring[j].isnumeric():
            found = True
            accu += str(rowstring[j])
        for lr,dr in replacements:
            if rowstring[j:j+len(lr)] == lr:
                accu += str(dr)
                found = True
        if found == False:
            j += 1
        if found == True:
            break
    j = len(rowstring)-1
    while j > 0:
        found = False
        if rowstring[j].isnumeric():
            found = True
            accu += str(rowstring[j])
        for lr,dr in replacements:
            if rowstring[j:j+len(lr)] == lr:
                accu += str(dr)
                found = True
        if found == False:
            j -= 1
        if found == True:
            break

    accufirst_last = accu[0]+accu[-1]
    onlydigits.append(accufirst_last)
    print(rowstring, "->", accu, "->", accufirst_last)
    

print(onlydigits)

somme = sum([int(d) for d in onlydigits])

print(somme)

