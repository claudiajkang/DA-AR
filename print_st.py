#!/usr/bin/env python

problem = input("problem name: ")

tp = problem.split()

filename = '-'.join(tp)

prob_url = "https://www.hackerrank.com/challenges/{}/problem".format(filename.lower())

print("\n======filename")
print("HR_"+filename+".py")
print("\n======PR MSG #1")
print("Init source code from "+problem+" problem")
print("\nprob : "+prob_url)
print("\n======PR MSG #2")
print("Update code that solved "+problem+" problem")
print("\nprob : "+prob_url+"\n")
