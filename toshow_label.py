#!/usr/bin/env python
# coding=utf-8

#//192.168.0.102/home/zean/lao_ren_shou_ji/toshow_label.py

from flags import FLAGS
import os    
import sys  
import codecs  
import time
  
''''' 
@2016-01-07 By Eastmount 
功能:合并实体名称和聚类结果 共类簇90类 
输入:BH_EntityName.txt Cluster_Result.txt 
输出:ZBH_Cluster_Merge.txt ZBH_Cluster_Result.txt 
'''  
flags=FLAGS(90, False, False)
flags.set_flag_debug(True)
  
source1 = open("./data/output/sample0001.txt",'r')  
source2 = open("./data/output/kmeans.txt",'r')  
result1 = codecs.open("./data/output/kmeans_toshow.txt", 'w','utf-8')  
  
#########################################################################  
#                        第一部分 合并实体名称和类簇  
  
lable = []       #存储408个类标 20个类  
content = []     #存储408个实体名称  
names = source1.readlines()  
#总是多输出空格 故设置0 1使其输出一致  
res = source2.readline()  
for name in names:  
    name = unicode(name.strip('\r\n'), "utf-8")  
#    print '===='
#    print name
    res = source2.readline()  
    no = int(res)            #行号  
    res = source2.readline()  
    va = int(res)            #值  
    lable.append(va)  
    content.append(name+" "+str(no)+" \r\n")
    name+" "+str(no)+" \r\n"
#    time.sleep(1)
    result1.write(name + ' ' + str(va) + ' ' + str(no) + ' '  + '\r\n')  
source1.close()  
source2.close()  
result1.close()  
  
#测试输出 其中实体名称和类标一一对应  
i = 0  
while i < len(lable):  
  #  print content[i], (i+1), lable[i]  
    i = i + 1  
  
# 第二部分 合并类簇 类1 ..... 类2 .....  
  
#定义定长20字符串数组 对应20个类簇  
output = ['']*flags.CLUSTER_NUM
result2 = codecs.open("./data/output/kmeans_toshow_2.txt", 'w', 'utf-8')  
  
#统计类标对应的实体名称  
i = 0
while i < len(lable):
  if flags.DEBUG:
    output[lable[i]] += ' \r\n----' + content[i] + str(lable[i]) + ' \r\n----'
    print output[lable[i]]
    i = i + 1

    
#输出  
i = 0  
while i < flags.CLUSTER_NUM:  
#    print '#######'  
    result2.write('#######\r\n')  
#    print 'Label: ' + str(i)  
    result2.write('Label: ' + str(i) + '\r\n')  
    result2.write('---\r\n')  
 #   print output[i]  
    result2.write(output[i] + '\r\n')  
    print('====')
    print(output[i])
    result2.write('---\r\n')  
    i = i + 1  
result2.close()  