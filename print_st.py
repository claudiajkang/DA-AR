#!/usr/bin/env python

problem = input("problem url: ")

tp = problem.split('/')

filename = tp[-2]

prob_url = problem
if '?' in problem:
    prob_url = problem.split('?')[0]

print("\n======filename")
print("HR_"+filename+".py")
print("\n======PR MSG #1")
print("git add .")
print('git commit -m "')
print("Init source code from "+filename+" problem")
print("\nprob : "+prob_url+'"')
print("\n======PR MSG #2")
print("git add .")
print('git commit -m "')
print("Update code that solved "+filename+" problem")
print("\nprob : "+prob_url+'"'+"\n")
