#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/10/10 22:53
# @Author  : Gs
# @Site    : 
# @File    : FileProcess.py
# @Software: PyCharm
import os
import shutil

def walkFile(file):
    FileList = []
    for root, dirs, files in os.walk(file):
        # root 表示当前正在访问的文件夹路径
        # dirs 表示该文件夹下的子目录名list
        # files 表示该文件夹下的文件list
        # 遍历文件
        for f in files:
            if ("._" or ".DS_Store" or ".torrent" or '.srt' or 'piece_part') in f:
                continue
            FileList.append(os.path.join(root, f))
    return FileList


path=r"G:\movie\电影2\x.zip"
path=r"G:\movie\电影2\x2.zip"
path=r"G:\movie\电影2\x3.zip"
path=r"G:\movie\电影2\x4.zip"
print("修改")
print("修改分支")
print("修改分支4")
print("修改master1")

outputpath=r"G:\movie\电影2"
files = walkFile(path)
for a in files:
    new_name = "_".join(a.split("\\")[4:]).split(".")[:-1]
    if len(new_name) == 1:
        new_name = new_name[0]
    else:
        new_name = "_".join(new_name)
    outputFile = os.path.join(outputpath, new_name)
    if os.path.exists(outputFile):
        shutil.move(outputFile, outputFile + "_A")
        new_name = new_name + "_B"
        outputFile = os.path.join(outputpath, new_name)
    print(a, new_name)
    try:
        shutil.move(a, outputFile)
    except Exception:
        continue
# for filename in files:
#     portion = os.path.splitext(filename)
#     print(filename)
