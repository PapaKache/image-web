from user_info import UserInfo,UserManage

SAVE = False
um = UserManage()
if SAVE:
    u = UserInfo()
    u.setInfo('ouyang','123456', "Tommy")
    um.saveUserInfo(u)

    u.setInfo('adfads','123456', "Tommy")
    um.saveUserInfo(u)
    u.setInfo('ganadfads','1456', "Tmmy")
    um.saveUserInfo(u)
    exit()
(r,u) = um.getUserInfo('adfads')
if r == False:
    print('get userinfo fail')
    exit()

s = u.toString()
print('to s')
print(s)
