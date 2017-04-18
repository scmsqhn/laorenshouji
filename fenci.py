#!/usr/bin/env python
# coding=utf-8
import traceback
import chardet
import json
import data_helpers
import sys  
import re  
import codecs  
import os  
import shutil  
#import jieba  
#import jieba.analyse  
  
#导入自定义词典  
#jieba.load_userdict("./data/dict.txt")  
pick_hanzi= '[\\u4e00-\\u9fa5]'
#Read file and cut  

def clean_input_sentences():
# sort the input sentences 
# and set them to 'sample0001.txt'
# befoe set to read_file_cut
  pass

def read_all_files_under():
  import os
  s = os.sep # '/' or '\'
  root = s+"disk200g"+s+"hn"+s+"laorenshouji"+s+"data"+s+"input"+s+"taobao_reviews"+s 
  for rt, dirs, files in os.walk(root):
      for f in files:
          fname = os.path.splitext(f)
        #  print(fname)
          new = fname[0] + 'b' + fname[1]
         # print(new)
#          os.rename(os.path.join(rt,f),os.path.join(rt,new))

def detect(string):
  print(type(string))
  print(chardet.detect(string))


def scan_dicts(src_dict,target_key):
#  get 'rateContent' values from json
  strs_rate_content=[]
  for key in src_dict.keys():
      src_dict=(src_dict[key])
      for key in src_dict.keys():
        for li in src_dict['rateList']:
          for key in li.keys():
            if key == 'rateContent':
              string = re.sub(r"<b></b>", '', li[key])
              string = re.sub(r"\\\\", r"\\", string)
              string = re.sub(r"!", r"", string)
              string = re.sub(r"\\x", r"", string)
              string = re.sub(r",", r"", string)
              #string = re.sub(r"?", r"", string)
#              string = string.strip(" ")
#              print(string)
              try:
                b=bytes.fromhex(string)
#              print(type(b))
#              print(b)
#              print(chardet.detect(b))
                b=b.decode('gb2312')
#              print(type(b))
#              print(b)
                strs_rate_content.append(b+'\r\n')
              except:
                pass
  return strs_rate_content                   

def read_all_files_under_2():
  g=codecs.open('./data/input/sample0001.txt','a+',encoding='utf8')
  import os
  count=0
  s = os.sep # '/' or '\'
  root = s+"disk200g"+s+"hn"+s+"laorenshouji"+s+"data"+s+"input"+s+"taobao_reviews"+s 
  for i in os.listdir(root):
      if os.path.isfile(os.path.join(root,i)):
          print(os.path.join(root,i))
          #f=open(os.path.join(root,i))
          with open(os.path.join(root,i), 'r') as f:
            line=f.readline()[21:-2]
#            print(line)
            line=data_helpers.clean_str_4_json(line)
            if line != "":
                data=json.loads((line))#, encoding='gb2312')
#                print(type(data))
                tt=scan_dicts(data,'rateContent')
                for t in tt:
                    print(type(t))
                    print((t))
                    g.write(t)
#                break
  g.flush()
  g.close()

                
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
      if isinstance(line, str):
        result.write('===' + line + '\r\n')
        print(line)
        continue
      line=line.decode("utf-8")
      line = data_helpers.clean_str(line)
      seglist = jieba.cut(line,cut_all=False)  #精确模式  
      output = ' '.join(list(seglist))         #空格拼接  
      output = re.sub(r"  ", " ", output)
      output = re.sub(r"   ", " ", output)
      result.write(output + '\r\n')
   #   print(output)
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
           # print((type(line)))
#            line = unicode(line, "utf-8")
            line = data_helpers.clean_str(line)
            line=line.decode("utf-8")
           # print(line)
            seglist = jieba.cut(line,cut_all=False)  #精确模式  
            #print(line)
            output = ' '.join(list(seglist))         #空格拼接  
          #  print(output)  
            result.write(output + '\r\n')  
            line = source.readline()  
        else:  
           # print(('End file: ' + str(num)))  
            source.close()  
            result.close()  
        num = num + 1  
    else:  
       # print('End All')  
        pass
  
#Run function  
if __name__ == '__main__':  
    read_all_files_under_2()
    read_file_cut('sample0001')  

