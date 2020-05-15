#!/usr/bin/env python
import os

P = os.environ['P']
problem = input('problem url: ')
tp = problem.split('/')

prob_url = problem
if '?' in problem:
    prob_url = problem.split('?')[0]

if 'acmicpc' in prob_url:
    filename = 'BOJ-' + tp[-1]

if 'hacker' in prob_url:
    filename = 'HR-' + tp[-2]

dir = os.getcwd()
filedir = f'{dir}/{P}/{filename}.sql' if 'SQL' in P else f'{dir}/{P}/{filename}.py'
f = open(filedir, 'w')
f.write('')
f.close()
#
# print('======filename')
# if 'SQL' in P:
#     print('touch '+P+'/'+filename+'.sql')
#     print('vim '+P+'/'+filename+'.sql')
# else:
#     print('touch '+P+'/'+filename+'.py')
#     print('vim '+P+'/'+filename+'.py')
#     print('python '+P+'/'+filename+'.py')
# print('\n======PR MSG #1')
# print('git add .;git commit -m "Add code that solved '+filename+' problem\n\nprob : '+prob_url+'"')
# print('\n======PR MSG #2')
# print('git add .;git commit -m "Update code that solved '+filename+' problem\n\nprob : '+prob_url+'"\n')
