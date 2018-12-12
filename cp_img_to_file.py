# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 17:40:51 2018

@author: huyz
"""


'''
该代码实现的功能是复制图片，从一个文件夹复制到另外一个文件夹（原来所有的图片都在同一个文件夹下），
并按照图片名称建立子文件夹，将同一个人的照片复制到对应的子文件夹下
'''

import os

src_path = 'E:/Cross-Pose_LFW/CPLFW/images_landmarks/cp-aligned/'
root_dir = 'E:/Cross-Pose_LFW/CPLFW/images_landmarks/CPLFW/'

names_list = []
for name in os.listdir(src_path):
	if name.endswith('.jpg'):     # 这样只复制.jpg 结尾的文件
		names_list.append(name)
    
#print(names_list)
name_set = set()          # list转set可以去掉重复的元素，通过set来新建子文件夹
for single_name in names_list:
    name_split = single_name.split("_")
    name_join = "_".join(s for s in name_split[:-1])
    name_set.add(name_join)
print(len(name_set))

names_path = []
for name in name_set:
    names_path.append(root_dir + name)
    #print(name_path)
    
    for name_path in names_path:
        try:
            os.makedirs(name_path)
        except OSError:
            pass
    
    
for img in names_list:
    print(img)
    img_split = img.split("_")
    for name_path in names_path:
        if "_".join(s for s in img_split[:-1]) in name_path:
            src_file = src_path + img
            target_file = name_path + "/" + img
            print(src_file)
            print(target_file)
            os.system("cp %s %s"%(src_file, target_file))
            print("---")
    

    