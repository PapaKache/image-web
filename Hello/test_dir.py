# -*- coding: utf-8 -*-
import os 

def get_files(file_dir):   
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
            print(fn) 
    if fnum <= 0:
        return []
        
   
get_files('/home/djiango/static/images')
