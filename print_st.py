#!/usr/bin/env python

problem = input("problem url: ")

tp = problem.split('/')


prob_url = problem
if '?' in problem:
    prob_url = problem.split('?')[0]

if "acmicpc" in prob_url:
    pre_val = "BOJ_"
    filename = tp[-1]

if "hacker" in prob_url:
    pre_val = "HR_"
    filename = tp[-2]

print("\n======filename")
print(pre_val+filename+".py")
print("\n======PRE PR")
print("git add .")
print('git commit -m "')
print("\n======PR MSG #1")
print("Init source code from "+filename+" problem")
print("\nprob : "+prob_url+'"')
print("\n======PR MSG #2")
print("Update code that solved "+filename+" problem")
print("\nprob : "+prob_url+'"')
print("\n======PR MSG #3")
print("Add code that solved "+filename+" problem")
print("\nprob : "+prob_url+'"'+"\n")
