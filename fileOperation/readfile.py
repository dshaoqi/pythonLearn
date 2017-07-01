#!/usr/bin/env python

#read info from file
import pickle

s={}
f=open('friendsinfo.txt','rb')
s=pickle.load(f)
print(s)
f.close()
