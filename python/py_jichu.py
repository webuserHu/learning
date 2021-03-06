#类型转换 start--------------------
#>>> int('123')
#123
#>>> int(12.34)
#12
#>>> float('12.34')
#12.34
#>>> str(1.23)
#'1.23'
#>>> str(100)
#'100'
#>>> bool(1)
#True
#>>> bool('')
#False
#类型转换 end----------------------

#字符串 start----------------------
#a = 'asd';
#a = a.replace("a","A")		#replace本质不是替换,而是创建新的字符串
#字符串 end------------------------

#list start------------------------
#a = ['4','2','3']
#print(len(a))
#print(a[3])	#list index out of range
#print(a[-1])	#倒数第一个值
#print(a[-2])	#倒数第二个值

#a.insert(2,'2.5')	#插入到某位置

#a.append('4')	#追加到最后

#a.pop()		#删除最后一个

#a.pop(1)		#删除指定位置的值

#a.sort()		#排序

#a[0]='-1'			#重新赋值

#b=[1,2,3,[11,22,33],4]
#print(b[3][1])
#list end------------------------------

#tuple (元组) start--------------------
#没有append()，insert()
#只有1个元素的tuple定义时必须加一个逗号','，来消除歧义.如:t = (1,)
#a=(1,2,3,4)
#print(a[1])

#a[0] = 111		#报错,不能修改
#tuple (元组) end----------------------

#条件判断 start------------------------
#num = 0
#if num>0:
#	print("大于")
#elif num==0:
#	print("0")
#else:
#	print("小于")
#条件判断 end------------------------

#循环 start--------------------------
#nums = [111,222,333,444,555,666,777]
#for num in nums:
#	print(num)

#numbers = list(range(101))
#n=0
#while n<101:
#	if n%2 == 0:
#		break
#		continue
#	print(numbers[n])
#	n=n+1
#循环 end----------------------------

#dict start--------------------------
#d = {'aaa':1,'bbb':2,'ccc':3}
#d['ddd'] = 4	#插入ddd

#print(d.get('aaa'))		#第一种取值方式
#print(d['aaa'])			#第二种取值方式
#print('aaa' in d)	#判断d中是否有aaa
#d.pop('ddd')		#删除
#dict end----------------------------

#set start---------------------------
#set 无序,无重复
#s1 = set(['111','111','222'])
#s1.add("222")	#追加
#s1.remove("222")		#删除

#s2 = set(['333','222'])
#print(s1 & s2)	#并集(两个set相同的值)
#print(s1 | s2)	#交集(两个set所有的值)
#set end-----------------------------

#切片 -------------------------------
#字符串,list都可以
#方法一:根据下标截取
L = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15"]
#print(L[0:2])       #取下标0-2 不包括2的\
#print(L[-2:])       #倒数前两个
#print(L[-2:-1])
#print(L[:2])       #前两个
#print(L[:10:2])     #前10,每两个取一个
#print(L[::3])       #所有,每3个取一个
#print(L[:])         #不变

#print('ABCDEFG'[:3])    #字符串测试
#print('ABCDEFG'[::2])

#方法二:放到另一个数组中
#r = []
#n = 3   #取前三
#for i in range(n):
#    r.append(L[i])
#print(r)'
