# -*- coding: utf-8 -*-
"""
实现一个磁盘文件的Map，用来序列化存储数据

@author: robert
"""

import os
import pickle


def __getStoragePath():
    return "./storage"


def __initDir():
    map_path = __getStoragePath()
    if os.path.isdir(map_path) == False:
        os.mkdir(map_path)


def __path(name):
    return os.path.join(__getStoragePath(), name)


def put(name, content):
    __initDir()
    f = open(__path(name), 'wb')
    pickle.dump(content, f)


def get(name):
    f = open(__path(name), 'rb')
    return pickle.load(f)


def has(name):
    return os.path.isfile(__path(name))
