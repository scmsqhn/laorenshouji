#!/usr/bin/env python
# coding=utf-8

import data_helpers
import sys  
import re  
import codecs  
import os  
import shutil  
import jieba  
import jieba.analyse  
  
#导入自定义词典  
jieba.load_userdict("./data/dict.txt")  
pick_hanzi= u'[\u4e00-\u9fa5]'
#Read file and cut  

def read_file_cut(samplename):
    respath = "./data/input/"
    path = "./data/output/"
#    if os.path.isdir(respath):  
#        shutil.rmtree(respath, True)  
#    os.makedirs(respath)  
    name = samplename   
    fileName = path + str(name) + ".txt"  
    resName = respath + str(name) + ".txt"  
    source = open(resName, 'r')  
    if os.path.exists(fileName):  
      os.remove(fileName)  
    result = codecs.open(fileName, 'w', 'utf-8')  
    lines = source.readlines()  
    for line in lines:
      if line=="":
        continue
      line=line.decode("utf-8")
      line = data_helpers.clean_str(line)
      seglist = jieba.cut(line,cut_all=False)  #精确模式  
      output = ' '.join(list(seglist))         #空格拼接  
      output = re.sub(r"  ", " ", output)
      output = re.sub(r"   ", " ", output)
      result.write(output + '\r\n')  
      print(output)
    source.close()  
    result.close()  

def read_files_cut():  
    #create path  
    path = "./data/"  
    respath = "./data/output/"  
    if os.path.isdir(respath):  
        shutil.rmtree(respath, True)  
    os.makedirs(respath)  
    num = 1
    
    while num<=204:  
        name = "%04d" % num   
        fileName = path + str(name) + ".txt"  
        resName = respath + str(name) + ".txt"  
        source = open('./data/sample1.txt', 'r')  
#        source = open(fileName, 'r')  
        if os.path.exists(resName):  
            os.remove(resName)  
        result = codecs.open(resName, 'w', 'utf-8')  
        line = source.readline()  
        line = line.rstrip('\n')  
          
        while line!="":
            print(type(line))
#            line = unicode(line, "utf-8")
            line = data_helpers.clean_str(line)
            line=line.decode("utf-8")
            print(line)
            seglist = jieba.cut(line,cut_all=False)  #精确模式  
            print(line)
            output = ' '.join(list(seglist))         #空格拼接  
            print output  
            result.write(output + '\r\n')  
            line = source.readline()  
        else:  
            print 'End file: ' + str(num)  
            source.close()  
            result.close()  
        num = num + 1  
    else:  
        print 'End All'  
  
#Run function  
if __name__ == '__main__':  
    read_file_cut('sample0001')  
