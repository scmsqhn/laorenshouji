#!/usr/bin/env python
# coding=utf-8
#from MyThread import *
import threading

Lock = threading.Lock()

# 定义簇分类的个数
class FLAGS(object):

    # 定义静态变量实例
    __instance = None
    print 'class FLAGS'

    def __init__(self):
        print '__init__'
        pass

    def __new__(cls, *args, **kwargs):
        print '__new__'
        if not cls.__instance: # __instance is none
            try:
                Lock.acquire()
                # double check
                if not cls.__instance:
                    cls.__instance = super(FLAGS, cls).__new__(cls, *args, **kwargs)
            finally:
                print '__new__'
                Lock.release()
        return cls.__instance

    def __init__(self, arg1, arg2, arg3):
        print "__init__"
        self.CLUSTER_NUM = arg1
        self.DEBUG = arg2
        self.TEST = arg3

    def set_flag_debug(self, arg0):
        self.DEBUG = arg0
    
    def set_flag_test(self, arg0):
        self.TEST = arg0
    
    def set_flag_cluster_num(self, arg0):
        self.CLUSTER_NUM = arg0


def test_singleton_in_thread():
    print "test_singleton_in_thread()"
    print id(Singleton())

if __name__ == "__main__":
    idx = 0
    while 1:
        MyThread(test_singleton_in_thread, []).start()
        idx += 1
        print idx
        if idx > 0X100:
            print 'idx > 0X100'
            print idx
            break

