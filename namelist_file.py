# -*- coding: utf-8 -*-
# 该程序是为了进行将正负样本图片的文件名进行提取的文件
import os

def getFileName(path):
    ''' 获取指定目录下的所有指定后缀的文件名 '''
    f_list = os.listdir(path)
    fopen = open('list_1.txt', 'w')  # 替换为你的路径
    # print f_list
    for i in f_list:
        # os.path.splitext():分离文件名与扩展名
        if os.path.splitext(i)[1] == '.bmp':
            #fopen.write('F:/Me/Graduation_project/HaarTiQu/postive/' + i + ' 1 0 0 36 36'+ '\n')  # 写入文件中
            #fopen.write('F:/Me/Graduation_project/HaarTiQu/negative/' + i + '\n')  # 写入文
            fopen.write('E:/VIVE_Reflex/0001_170629/Left/' + i + '\n')
            print i
    fopen.close()
if __name__ == '__main__':
    #path = 'F:/Me/Graduation_project/HaarTiQu/negative'
   # path = 'F:/Me/Graduation_project/HaarTiQu/postive'
    path = 'E:/VIVE_Reflex/0001_170629/Left/'
    getFileName(path)

