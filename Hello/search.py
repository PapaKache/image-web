# -*- coding: utf-8 -*-
 
from django.http import HttpResponse
#from django.shortcuts import render_to_response
from django.shortcuts import render
import os
# 表单
def search_form(request):
    print('search form')
    print(request)
    #return render_to_response('search_form.html')
    context          = {}
    #context['hello'] = 'Hello World!'
    return render(request, 'search_form.html', context)
 
# 接收请求数据
def search(request):  
    print('search')
    request.encoding='utf-8'
    if 'q' in request.GET and request.GET['q']:
        message = '你搜索的内容为: ' + request.GET['q']
    else:
        message = '你提交了空表单'
    return HttpResponse(message)
    
def fuck(request):  
    print('fuck')
    request.encoding='utf-8'
    if 'a' in request.GET and request.GET['a']:
        message = 'a你搜索的内容为: ' + request.GET['a'] + "\n"
        message += 'aa你搜索的内容为: ' + request.GET['aa'] + "\n"
        message += 'aaa你搜索的内容为: ' + request.GET['aaa'] + "\n"
        print(message)
    else:
        message = 'aa你提交了空表单'
    return HttpResponse(message)
    
def search_post(request):
    ctx ={}
    if request.POST:
        ctx['rlt'] = request.POST['q']
    return render(request, "post.html", ctx)
    
def upload(request):
    print('upload')
    print(request)
    print("1")
    if request.method == 'GET':
        print("1.1")
        return render(request,'upload.html')
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
        storage = open('/home/storage/abc','w')       #打开存储文件
        storage.write('afbadlfad')
        storage.close()

        storage = open(position,'wb+')       #打开存储文件
        for chunk in content.chunks():       #分块写入文件
            storage.write(chunk)
        storage.close()                      #写入完成后关闭文件
        return HttpResponse("上传成功")      #返回客户端信息
    else:
        return HttpResponseRedirect("不支持的请求方法")
