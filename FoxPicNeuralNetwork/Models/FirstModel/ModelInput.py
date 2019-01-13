# -*- coding: utf-8 -*

'''
读取文件,分成两个类型
可能需要额外的预处理
'''

import  os
import configparser
import random

from  Config.GlobalConfig import GlobalConfig
class ImageReader:
    __rootPath = "";

    def __init__(self,rootPath):
        cp = configparser.ConfigParser();
        _rootPath = rootPath;
        if(os.path.isdir(_rootPath)):
            print("路径:{0} 存在".format(_rootPath))
        else:
            print("路径:{0} 不存在,创建中".format(_rootPath))
            os.makedirs(_rootPath)

    def GetBatch(self,batchSize):
        if(batchSize <= 0):
            exit(-1);

        # 读取指定大小的图片 以及标签数量
        # 验证集数量 训练集数量 测试集数量
        # 批次大小指的是训练集的

        # 获取不同等级的数据,进行输入

        # 获取所有所有图片路径


if __name__ == "__main__":
    pathOfImages = GlobalConfig().GetPicBufPath()
    print("图片路径:{0}".format(pathOfImages))
    imageReader = ImageReader(pathOfImages)
    exit(0)