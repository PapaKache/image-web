# -*- coding: utf-8 -*-
 
from django.http import HttpResponse
from django.shortcuts import render
import os
from django.utils.safestring import mark_safe
# 表单
   
def main(request):
    print('upload')
    print(request)
    print("1")
    if request.method == 'GET':
        print("1.1")
        return render(request,'index.html')
    elif request.method == 'POST':
        print("2")

def test(request):
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
    print("1")
    if request.method == 'GET':
        print("1.1>>")
        #return render(request,'upload.html')
    elif request.method == 'POST':
        print("2")
        content =request.FILES.get("upload", None)
        print("3")
        if not content:
            return HttpResponse("没有上传内容")
        print('name:%s'%content.name)
        position = os.path.join('/home/storage/',content.name)
        print(position)
        #获取上传文件的文件名，并将其存储到指定位置
        #storage = open('/home/storage/abc','w')       #打开存储文件
        #storage.write('afbadlfad')
        #storage.close()

        storage = open(position,'wb+')       #打开存储文件
        for chunk in content.chunks():       #分块写入文件
            storage.write(chunk)
        storage.close()                      #写入完成后关闭文件
        return HttpResponse("上传成功")      #返回客户端信息
    else:
        return HttpResponseRedirect("不支持的请求方法")
