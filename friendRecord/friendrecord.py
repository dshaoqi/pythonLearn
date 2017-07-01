import pickle
f=open('friendsinfo.txt','r+')
friendinfo={}
try:
    friendinfo=pickle.load(f)
except IOError:
    print('load from the file failed,please check the file content or open style')
else :
    print('load some info from friendinfo file')
    print(friendinfo)

def addFriend(name,phone='none',email='none'):
    global friendinfo;
    if name in friendinfo:
        print('name exists already')
    else :
        friendinfo[name]=(phone,email)
        print('add a new friend')

def changePhone(name,phone):
    global friendinfo
    if name in friendinfo:
        friendinfo[name]=(phone,friendinfo[name][1])
    else :
        print('cannt find the name')

def deleteFriend(name):
    global friendinfo
    if name in friendinfo:
        friendinfo.pop(name)
        print 'delete the friend',name
    else :
        print('no such name')

def saveInfo():
    global  friendinfo,f
    f.seek(0)
    pickle.dump(friendinfo,f)
    print('save the info')

