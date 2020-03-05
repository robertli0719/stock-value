# -*- coding: utf-8 -*-
"""
实现一个磁盘文件的Map，用来序列化存储数据

@author: robert
"""

import os
import pickle


def __get_storage_path():
    return "./storage"


def __init_dir():
    map_path = __get_storage_path()
    if not os.path.isdir(map_path):
        os.mkdir(map_path)


def __path(name):
    return os.path.join(__get_storage_path(), name)


def put(name, content):
    __init_dir()
    f = open(__path(name), 'wb')
    pickle.dump(content, f)


def get(name):
    f = open(__path(name), 'rb')
    return pickle.load(f)


def has(name):
    return os.path.isfile(__path(name))
