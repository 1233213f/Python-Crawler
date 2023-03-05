import os
import re
import time

string =''
a = input()
i=0
while i<2:
    string +=a
    a = input()
    if a:
        string += '\n'
    if a=='':
        string += '\n'
        i=i+1
# print(string.split('\n')or('，'))
# print(len(string.split('，'and'\n')))
# print(len(string.split('，')))
# print(len(string.split('\n')))
# print(string.split('\n')[8])
# print(string.split('\n')[7])
# print(string.replace('\n', '').replace('\r', ''))
# print(re.split('，|。',string))

string=string.replace('\n', '').replace('\r', '')
string=re.split('，|。',string)
cpuDetail = [i for i in string if i !='']
print(len(string))
print(string[1])






#
# cpuDetail = [i for i in re.split('。',string) if i !='']#方法一
# print(cpuDetail)

#  = string.split("\n")#方法二
# while '' in cpuDetail:
#     cpuDetail.remove('')
# print(cpuDetail)
# string=string.replace('\n', '').replace('\r', '')
# cpuDetail=string.split('\n')#方法三
# for i in cpuDetail:
#     print(i)
#     if i == '':
#         cpuDetail.remove(i)
# cpuDetail = [i for i in cpuDetail if i !='']
# print ("删除空值后的输出如下:\n",cpuDetail)

# string=string.replace('\n', '').replace('\r', '')
# string1=re.split('，|。',string))

# for i in cpuDetail[i]:
#     if i=="，"
# print(cpuDetail)
# print (li_list.split('\n'))
# print(len(li_list.split('\n')))