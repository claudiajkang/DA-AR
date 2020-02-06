#!/usr/bin/env python

problem = input('problem url: ')

tp = problem.split('/')


prob_url = problem
if '?' in problem:
    prob_url = problem.split('?')[0]

if 'acmicpc' in prob_url:
    filename = 'BOJ-' + tp[-1]

if 'hacker' in prob_url:
    filename = 'HR-' + tp[-2]

print('\n======filename')
print(filename+'.py')
print('\n======PR MSG #1')
print('git add .;git commit -m "Init source code from '+filename+' problem')
print('\nprob : '+prob_url+'"')
print('\n======PR MSG #2')
print('git add .;git commit -m "Update code that solved '+filename+' problem')
print('\nprob : '+prob_url+'"')
print('\n======PR MSG #3')
print('git add .;git commit -m "Add code that solved '+filename+' problem')
print('\nprob : '+prob_url+'"'+'\n')
