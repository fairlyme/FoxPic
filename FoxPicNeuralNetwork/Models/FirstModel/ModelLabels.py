# -*- coding: utf-8 -*
from enum import Enum

'''
Fox Pic 的标签定义
包含 讨厌 不喜欢 无感 喜欢 超爱
'''
class FoxPicLable(Enum):
    Hate = 0
    DisLike = 1
    NoFelling = 2
    Like = 3
    Love = 4