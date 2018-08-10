# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 10:49:41 2018

@author: al-khatib
"""
list1 = ["a","b","c","d"]
DECTIONARY = {'egypt': '001','palestine':'005','grmany':'004'}
print(DECTIONARY)
dic = DECTIONARY.fromkeys(list1)
print(dic)
c = list(DECTIONARY.items())
print(c)

SET = {1,1,1,2,5,6,33,33,4}
print(SET)

print('001' in DECTIONARY.values())
print(DECTIONARY.get('egypt','253'))
TUBLE = (1,2,3,4,5,6,7,8,9,10,11,12)
print(TUBLE)


std = ['salam','hasan','aya']
grades = {'salam':'1','hasan':'5','aya':'3'}


x = sorted(std, key=grades.__getitem__)
print(x)