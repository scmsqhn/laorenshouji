#!/usr/bin/env python
# coding=utf-8

# Based on tornado.ioloop.IOLoop.instance() approach.
# See https://github.com/facebook/tornado

import threading

class SingleFlags(object):
  __singleton_lock = threading.Lock()
  __singleton_instance = None

  @classmethod
  def instance(cls, arg1, arg2, arg3):
    if not cls.__singleton_instance:
      with cls.__singleton_lock:
        if not cls.__singleton_instance:
          cls.__singleton_instance = cls(arg1, arg2, arg3)
    return cls.__singleton_instance
    
  def __init__(self, arg1, arg2, arg3):
      # this is called in "cls.__singleton_instance = cls(arg1, arg2, arg3)"

      print("__init__")
      self.CLUSTER_NUM = arg1
      self.DEBUG = arg2
      self.TEST = arg3

  def set_flag_debug(self, arg0):
      self.DEBUG = arg0

  def set_flag_test(self, arg0):
      self.TEST = arg0

  def set_flag_cluster_num(self, arg0):
      self.CLUSTER_NUM = arg0

if __name__ == '__main__':
	class A(SingleFlags):
		pass

	class B(SingleFlags):
		pass

	a, a2 = A.instance(90,False,False), A.instance(90,False,False)
	b, b2 = B.instance(90,False,False), B.instance(90,False,False)

	assert a is a2
	assert b is b2
	assert a is not b

	print('a:  %s\na2: %s' % (a, a2))
	print('b:  %s\nb2: %s' % (b, b2))