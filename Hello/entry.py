# -*- coding: utf-8 -*-
 
from django.http import HttpResponse
from django.shortcuts import render
import os
from django.utils.safestring import mark_safe
import json
from django.http import JsonResponse
from . import user_info
# 表单
def response(data):
    return JsonResponse(data)
    #return HttpResponse(json.dumps(data))

def main(request):
    print('main')
    print(request)
    if request.method == 'GET':
        return render(request,'index.html')
    elif request.method == 'POST':
        print("post")

def test(request):
    print('test')
    #ht = "<img id = 'img2' src= '/static/images/animal/大象.jpg'  class='contain'/ >"
    #return mark_safe(ht)
    #HttpResponse("Hello world ! ")
    #ctx ={}
    #if request.POST:
    #    return render(request, "post.html", ctx)
    ht = "<img id = 'img1' src= '/static/images/2.png'  class='contain'/>"
    return render(request, "index.html", {"img": ht})

def upload(request):
    print('upload')
    print(request)
    if request.method == 'GET':
        print("upload get")
        #return render(request,'upload.html')
    elif request.method == 'POST':
        print("upload post")
        tselect= request.POST.get('type_select')
        print(tselect)
        user = request.POST['user']
        content =request.FILES.get("upload", None)
        if not content:
            print('not upload value')
            return HttpResponse("没有上传内容")
        print('name:%s'%content.name)

        position = os.path.join('/home/djiango/static/images',user,tselect,content.name)
        print(position)

        storage = open(position,'wb+')       #打开存储文件
        for chunk in content.chunks():       #分块写入文件
            storage.write(chunk)
        storage.close()                      #写入完成后关闭文件
        return response("上传成功")      #返回客户端信息
    else:
        return response("不支持的请求方法")

def login(request):
    print('login')
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        print('login post')
        print(request)
        user = request.POST['user']
        pwd = request.POST['pwd']
        (r,u) = user_info.getUserInfo(user)
        if r == True:
            if u.pwd == pwd:
                rc = user_info.USER_LOGIN_SUCC
            else:
                rc = user_info.USER_LOGIN_FAIL
        else:
            rc = user_info.USER_LOGIN_NO_USER

        print(user)
        print(rc) 
        ht = {'user':user,'result':rc}
    return response(ht)

def type_get(request):
    SUCC = 0
    EXISTS = 1
    OUT_LIMIT = 2
    FAIL = 3
    rc = FAIL
    ht = {}
    print('type get')
    if request.method == 'POST':
        print(request)
        user = request.POST['user']
        (r,u) = user_info.getUserInfo(user)
        if r == True:
            dirname = os.path.join('/home/djiango/static/images',user)
            if os.path.exists(dirname) == False:
                rc = FAIL
                print('path no exists')
            else:
                ds = get_dirs(dirname)
                for i in range(len(ds)):
                    key = 'dir%d'%(i+1)
                    value = ds[i]
                    ht[key] = value
                    rc = SUCC
    ht['result'] = rc
    ht['user'] = user
    print(ht)
    return response(ht)
 
def type_delete(request):
    SUCC = 0
    EXISTS = 1
    OUT_LIMIT = 2
    FAIL = 3
    ht = {}
    print('type delete')
    rc = FAIL
    if request.method == 'POST':
        print(request)
        user = request.POST['user']
        tselect = request.POST['type_select']
        (r,u) = user_info.getUserInfo(user)
        if r == True:
            dirname = os.path.join('/home/djiango/static/images',user,tselect)
            if os.path.exists(dirname):
                rc = SUCC
                os.system('rm -rvf ' + dirname)
        ht = {'user':user,'result':rc}
    return response(ht)
 
def type_add(request):
    SUCC = 0
    EXISTS = 1
    OUT_LIMIT = 2
    FAIL = 3
    ht = {}
    print('type add')
    rc = FAIL
    if request.method == 'POST':
        print(request)
        user = request.POST['user']
        cate = request.POST['type_add']
        (r,u) = user_info.getUserInfo(user)
        if r == True:
            dirname = os.path.join('/home/djiango/static/images',user,cate)
            if os.path.exists(dirname):
                rc = EXISTS
                print('path exists')
            else:
                os.system('mkdir ' + dirname)
                print('mkdir ' + dirname)
                rc = SUCC
        ht = {'user':user,'result':rc}
    return response(ht)
 
def register(request):
    print('register')
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        print('register post')
        print(request)
        user = request.POST['user']
        pwd = request.POST['pwd']
        label = request.POST['label']
        (r,u) = user_info.getUserInfo(user)
        if r == True:
            rc = user_info.USER_REGISTER_EXISTS
        else:
            u = user_info.createUserInfo(user,pwd,label)
            user_info.saveUserInfo(u)
            rc = user_info.USER_REGISTER_SUCC
            print('create base dir')
            create_base_link(user)
        print(user)
        print(rc) 
        ht = {'user':user,'result':rc}
    return response(ht)
    
def update_image(request, user = True):
    print('update image')
    print(request)
    if user == True: 
        tselect = request.POST['type_select']
        page_num = request.POST['page_no']
        user = request.POST['user']
        print('pageno:' + page_num)
        print('user:' + user)
        page_index = int(page_num) - 1 #start from zero
    else:
        tselect = 'animal'
    #print(a)
    idir = os.path.join('/home/djiango/static/images',user,tselect)
    #idir = '/home/djiango/static/images/' + tselect
    print(idir)
    fs = get_files(idir)
    size = len(fs)
    page_no_max = int(size/10)
    if page_index > page_no_max:
        page_index = page_no_max
    
    
    if size <= 0:
        print('update image fail,get file:%d'%size)
        return render(request, "index.html", {})
        
    if page_no_max == 0:
        start_index = 0
        end_index = (size -1)- start_index
    else:
        start_index = (page_index) * 10
        end_index = (size - 1)
        if end_index - start_index > 9:
            end_index = start_index + 9

    dt = {}
    imgid = 1
    for i in range(start_index,end_index + 1, 1):
        key = 'img%d'% (imgid)    
        src = os.path.join("/static/images/",user,tselect,fs[i])
        #src= "/static/images/%s/%s"%(tselect,fs[i])
        dt[key] = src
        imgid += 1
        
    dt['page_no'] = (page_index + 1)
    print(dt)
    #return HttpResponse(json.dumps(dt), content_type='application/json')
    #return render(request, "index.html", dt)
    return response(dt)


def sort(vs):
    NAME = 0
    TIME = 1
    for start in range(len(vs)):
        max_index = start
        for i in range(start,len(vs),1):
            if vs[i][TIME] > vs[max_index][TIME]:
                max_index = i
        vstart = vs[start]
        vmax = vs[max_index]
        vs[start] = vmax
        vs[max_index] = vstart
    return vs    

def get_dirs(file_dir):  
    if os.path.exists(file_dir) == False:
        return []

    filelist =  os.listdir(file_dir)  #
    vs = []
    fnum = 0
    for f in filelist:
        fn = file_dir + "/" + f
        if os.path.isdir(fn)== True:
            fnum += 1
            t = os.path.getmtime(fn)
            item = [f,t]
            vs.append(item)
            #print(fn) 
    if fnum <= 0:
        return []
        
    ns = sort(vs) 
    rs = [0] * len(vs)
    for i in range(len(ns)):
        rs[i] = ns[i][0]
        #print(rs[i])
        
    return rs

def get_files(file_dir):  
    if os.path.exists(file_dir) == False:
        return []

    filelist =  os.listdir(file_dir)  #
    vs = []
    fnum = 0
    for f in filelist:
        fn = file_dir + "/" + f
        if os.path.isdir(fn)== False:
            fnum += 1
            fn = file_dir + "/" + f
            t = os.path.getmtime(fn)
            item = [f,t]
            vs.append(item)
            #print(fn) 
    if fnum <= 0:
        return []
        
    ns = sort(vs) 
    rs = [0] * len(vs)
    for i in range(len(ns)):
        rs[i] = ns[i][0]
        #print(rs[i])
        
    return rs
def create_base_link(user):
    src_dir=['','','','']
    dst_dir=['','','','']
    dst_dir[0] = '/home/djiango/static/images/%s'%user
    os.system('mkdir ' + dst_dir[0])

    src_dir[0] = '/home/djiango/static/images/%s/animal'%'guest'
    src_dir[1] = '/home/djiango/static/images/%s/plant'%'guest'
    src_dir[2] = '/home/djiango/static/images/%s/color'%'guest'
    src_dir[3] = '/home/djiango/static/images/%s/people'%'guest'

    dst_dir[0] = '/home/djiango/static/images/%s/animal'%user
    dst_dir[1] = '/home/djiango/static/images/%s/plant'%user
    dst_dir[2] = '/home/djiango/static/images/%s/color'%user
    dst_dir[3] = '/home/djiango/static/images/%s/people'%user
    for i in range(len(dst_dir)):
        os.system('mkdir ' + dst_dir[i])
        print('mkdir %s'%dst_dir[i])
        fs = get_files(src_dir[i])
        
        for name in fs:
            src = os.path.join(src_dir[i],name)
            dst = os.path.join(dst_dir[i],name)
            print('ln -s %s %s'%(src,dst))
            os.system('ln -s %s %s'%(src,dst)) 
#fs = get_files(".")
#print(fs)
