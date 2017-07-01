#!/usr/bin/env python

import pickle

s={}
f=open('friendsinfo.txt','wb')
s['dsq']=('13125083714','1198016334@qq.com')
s['jia']=('2859253','none')
pickle.dump(s,f)
f.close()
print('over')
