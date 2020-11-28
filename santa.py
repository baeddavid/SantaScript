#!/usr/bin/env python

import csv
from random import randrange

def main():
    candidates = open_csv()
    sattoloCycle(candidates)
    pairings = get_pairings(candidates)
    pairings_to_text(pairings)
    
def pairings_to_text(pairings):
    f = open("pairings.txt", "w+")
    for i in range(len(pairings)):
        person1 = pairings[i][0]
        person2 = pairings[i][1]
        f.write(person1["Name"] + " -- " + person1["Address"] + " <-----> "+ person2["Name"] + " -- " + person2["Address"] + "\n")
    f.close()
    
def get_pairings(items):
    i = 0
    pairings = []
    while i < len(items):
        pairings.append([items[i], items[i + 1]])
        i += 2
    return pairings
    
def sattoloCycle(items):
    for i in range(len(items) - 1, 0, -1):
        j = randrange(i)
        items[j], items[i] = items[i], items[j]

def open_csv():
    candidates = []
    with open('santa.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                candidates.append({
                    "Name": row[1],
                    "Address": row[2]
                })
                line_count += 1
    return candidates

main()
