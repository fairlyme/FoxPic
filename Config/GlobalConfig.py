# -*- coding: utf-8 -*
import configparser
import os

class Singleton(object):
    _instance = None
    def __new__(cls, *args, **kw):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kw)
        return cls._instance

class GlobalConfig(Singleton):
    __parser = configparser.ConfigParser();
    __configFileFullPath = ""
    __fileName = "FoxPicConfig.ini"
    def __init__(self):
        strThisFilePath =  os.path.split(os.path.realpath(__file__))[0];
        self.__configFileFullPath = os.path.join(strThisFilePath, self.__fileName)
        if not (os.path.isfile(self.__configFileFullPath)):
            open(self.__configFileFullPath, "w").close()

        self.__parser.read(self.__configFileFullPath)

    def GetPicBufPath(self):
        return self.__parser.get("DataPath","PicRootPath")