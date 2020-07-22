# -*- coding: utf-8 -*-
 
from django.http import HttpResponse
from django.shortcuts import render
import os
from django.utils.safestring import mark_safe
import json
# 表单
def response(data):
    return HttpResponse(json.dumps(data))

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
        

        content =request.FILES.get("upload", None)
        if not content:
            print('not upload value')
            return HttpResponse("没有上传内容")
        print('name:%s'%content.name)
        position = os.path.join('/home/djiango/static/images/'+tselect + '/',content.name)
        print(position)

        storage = open(position,'wb+')       #打开存储文件
        for chunk in content.chunks():       #分块写入文件
            storage.write(chunk)
        storage.close()                      #写入完成后关闭文件
        return response("上传成功")      #返回客户端信息
    else:
        return response("不支持的请求方法")

def update_image(request):
    print('update image')
    print(request)
    tselect = request.POST['type_select']
    #print(a)
    idir = '/home/djiango/static/images/' + tselect
    print(idir)
    fs = get_files(idir)
    size = len(fs)
    if size <= 0:
        print('update image fail,get file:%d'%size)
        return render(request, "index.html", {})
        
    if size >= 10:
        size = 10
    ht = {}
    for i in range(size):
        key = 'img%d'% i      
        line = "<img id = 'img%d' src= '/static/images/%s/%s'  class='contain'/>"%(i,tselect,fs[i])
        ht[key] = line
    #print(ht)
    return render(request, "index.html", ht)
    
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

def get_files(file_dir):   
    filelist =  os.listdir(file_dir)  #
    vs = []
    fnum = 0
    for f in filelist:
        if os.path.isdir(f)== False:
            fnum += 1
            fn = file_dir + "/" + f
            t = os.path.getmtime(fn)
            item = [f,t]
            vs.append(item)
    
    if fnum <= 0:
        return []
        
    ns = sort(vs) 
    rs = [0] * len(vs)
    for i in range(len(ns)):
        rs[i] = ns[i][0]
        #print(rs[i])
        
    return rs
    
fs = get_files(".")
print(fs)
