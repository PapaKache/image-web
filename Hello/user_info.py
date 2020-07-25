
class UserInfo():
    def __init__(self):
        self.name = ''
        self.pwd = ''
        self.label = ''

    def setInfo(self,name,pwd,label):
        self.name = name
        self.pwd = pwd
        self.label = label
    def toString(self):
        s = '%s,%s,%s\n'%(self.name,self.pwd,self.label)
        return s

PATH_INFO = '/home/djiango/users/infos'
USER_LOGIN_SUCC = 1
USER_LOGIN_FAIL = 2
USER_LOGIN_NO_USER = 3
USER_REGISTER_EXISTS =9
USER_REGISTER_SUCC =10
USER_REGISTER_FAIL=11
def createUserInfo(name,pwd,label):
    u = UserInfo()
    u.setInfo(name,pwd,label)
    return u
def saveUserInfo(inf):
    s = '%s,%s,%s\n'%(inf.name,inf.pwd,inf.label)
    f = open(PATH_INFO,'a+')
    f.write(s)
    f.close()


def getUserInfo( name):
    f = open(PATH_INFO,'r')
    lines = f.readlines()
    f.close()
    for line in lines:
        #print(line)
        ss = line.split(',')
            #print(ss)
            #print('------------------------')
        if len(ss) != 3:
            continue
        if ss[0] == name:
            u = UserInfo()
            u.name = ss[0]
            u.pwd =  ss[1]
            u.label =ss[2]
            return (True,u)
        
    return (False,None)



def deleteUserInfo(name):
    return
