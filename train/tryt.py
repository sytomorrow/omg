'''
#print("%s is number top %d"%("python",5))
myString="Hello,Word!"
print(myString[3:-1])#打印第三位到倒数第二位
print(myString[3:])#打印第三位到最后一位
print(myString[2:5])#打印第三位到第五位
print(myString[:5])#打印前五位
print(myString[-1])#打印最后一位
print(myString[-3:])#打印最后三位
print(myString[-5:-1])#打印倒数第五位至倒数第二位
myStr2=myString*2   #相同字符串的拼接
myStr3=myString+"very well" #不同字符串的拼接
print(myStr2,myStr3)

aList=[1,2,3,4,5,6]     #列表
aTuple=("hello","word","python","is","great","!")    #元组
aDict={"host":"earth","port":"8080"}    #字典
print(aList,aTuple,aDict.keys())
'''
#使用for循环把所有值放入一个列表中
# sqd=[x**2 for x in range(8) if not x % 2]
# for i in sqd:
#     print(i)
# a=0
# while a<=10:
#     print(a)
#     a += 1
# for i in range(3):
#     print(i)
'''
import cmath
print(abs(-5))  #取绝对值
print(cmath.sqrt(5))    #取平均数
print(float(3))      #转化浮点型
a = [1,2,2,4,3,4,]
a.append(5) #列表尾部增加一条数据
c = a.count(3)  #统计列表中一个元素的数量
print(a)
print(c)
b = [6,5,4,9]
a.extend(b)     #列表尾部增加列表
print(a)
print(a.index(6))   #找出一个元素所在的索引值
a.insert(3,"hello") #在指定位置插入一个元素
print(a)
'''
#assert -1>2,print("gaocuole")   #断言

# def fibs(num):
#     fibs=[0,1]
#     for i in range(num-2):
#         fibs.append(fibs[-1]+fibs[-2])
#     return fibs

# def asd(s="hello",d="word",a="!"):
#     print("%s,%s%s"%(s,d,a))
# def sim1(*sim):
#     print(sim)
# def sim2(**sim):
#     print(sim)
# sim1(1,2,3)
# sim2(a=1,b=2,c=3)
#
# def add(x,y):
#     return x+y
# bbb=(2,6)
# print(add(*bbb))

# print(type(2/1))
# print(type(2//1))#整除
# print(int(0o11))#转化为10进制
# print(bin(10))#转化为2进制
# print(hex(155))#转化为16进制
# print(oct(135))#转化为8进制
# #布尔类型属于数字类型的一个大类
# print(int(True))
# print('12\n123')
# print('13 \\n 1213 \\n 21313')
# print(r'13\n56\n54')#加r，原始字符串
# set()#空集合，无序，不重复
# set1={1,2,3,4,5,6}
# set2={1,2}
# set3={1,7}
# print(set1-set2)#差集
# print(set1&set2)#交集
# print(set1|set3)#并集
# dict1={1:"keyide",2:"没问题的",3:"hello",4:"word"}
# print(dict1[1])
# lista=[1,2,3,4]
# b=lista
# lista[1] = "hello"
# print(b)
print(1 and 2)
print(1 or 2)
a = {1,2,3}
b = {1,3,2}
print(a == b)
print(a is b)

isinstance(a,set)  # 判断数据类型
isinstance(a,(set,str))
