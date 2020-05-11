#!/bin/bash
#只读变量
#myUrl="http://www.google.com"
#readonly myUrl

#使用变量
#your_name="xxx"
#echo $your_name

#删除变量
#unset variable_name

#Shell 字符串
#单引号里的任何字符都会原样输出，单引号字符串中的变量是无效的；
#单引号字串中不能出现单引号（对单引号使用转义符后也不行）。
#双引号里可以有变量
#双引号里可以出现转义字符

# foreach
#for some in a b c d e; do
#	echo "read some ${some}Script"
#done

# append String
#your_name="shuaige"
#greeting="hello, "$your_name" !"
#greeting_1="hello, ${your_name} !"
#echo $greeting $greeting_1

# String length
#text="1234"
#echo ${#text}

# substring(index,size)
#text="1234567890"
#echo ${text:0:5}

#find string index(start index=1)
#text="string"
#echo `expr index "$text" r`

#Array
#array=(a b c d e f)
#echo ${array[0]}
#echo ${array[@]}

# Shell传递参数实例 ./text.sh x x x
#echo "执行的文件名：$0"
#echo "第一个参数为：$1"
#echo "第二个参数为：$2"
#echo "第三个参数为：$3"

#运算符(+-*/%)(=)(==)(!=)
#a=10
#b=2
#sumval=`expr $a + $b`
#echo "a+b=$sumval"

#(-eq -ne -gt -lt -ge -le)
#a=10
#b=2
#if [ $a -eq $b ]
#then
#	echo "eq"
#else
#	echo "ne"
#fi

#(!非 -o或 -a与 && ||)
#a=10
#b=20
#if [ $a -lt 100 -a $b -gt 15 ]
#then
#   echo "$a 小于 100 且 $b 大于 15 : 返回 true"
#else
#   echo "$a 小于 100 且 $b 大于 15 : 返回 false"
#fi

#字符串运算符
	#= 
	#!= 
	#-z检测字符串长度是否为0,为0返回true
	#-n检测字符串长度是否为0,不为0返回true
	#str检测字符串是否为空

#文件测试运算符
	#-b file 检测文件是否是块设备文件，如果是，则返回 true
	#-c file 检测文件是否是字符设备文件，如果是，则返回 true
	#-d file 检测文件是否是目录，如果是，则返回 true
	#-f file 检测文件是否是普通文件（既不是目录，也不是设备文件），如果是，则返回 true
	#-g file 检测文件是否设置了 SGID 位，如果是，则返回 true
	#-k file 检测文件是否设置了粘着位(Sticky Bit)，如果是，则返回 true
	#-p file 检测文件是否是有名管道，如果是，则返回 true
	#-u file 检测文件是否设置了 SUID 位，如果是，则返回 true
	#-r file 检测文件是否可读，如果是，则返回 true
	#-w file 检测文件是否可写，如果是，则返回 true
	#-x file 检测文件是否可执行，如果是，则返回 true
	#-s file 检测文件是否为空（文件大小是否大于0），不为空返回 true
	#-e file 检测文件（包括目录）是否存在，如果是，则返回 true

#read
#echo "please input name:"
#read str
#echo "$str is shuaige"

# -e 开启转义
#echo -e "OK! \n"
#echo "This is a test"

# Date
#echo `date`

# printf
printf "%-10s %-8s %-4s\n" 姓名 性别 体重kg  
printf "%-10s %-8s %-4.2f\n" 郭靖 男 66.1234 
printf "%-10s %-8s %-4.2f\n" 杨过 男 48.6543 
printf "%-10s %-8s %-4.2f\n" 郭芙 女 47.9876 
#%s %c %d %f都是格式替代符
#%-10s 指一个宽度为10个字符（-表示左对齐，没有则表示右对齐），任何字符都会被显示在10个字符宽的字符内，如果不足则自动以空格填充，超过也会将内容全部显示出来。
#%-4.2f 指格式化为小数，其中.2指保留2位小数。

#printf的转义序列
#\a	警告字符，通常为ASCII的BEL字符
#\b	后退
#\c	抑制（不显示）输出结果中任何结尾的换行字符（只在%b格式指示符控制下的参数字符串中有效），而且，任何留在参数里的字符、任何接下来的参数以及任何留在格式字符串中的字符，都被忽略
#\f	换页（formfeed）
#\n	换行
#\r	回车（Carriage return）
#\t	水平制表符
#\v	垂直制表符
#\\	一个字面上的反斜杠字符
#\ddd	表示1到3位数八进制值的字符。仅在格式字符串中有效
#\0ddd	表示1到3位的八进制值字符

# text
#num1="ru1noob"
#num2="runoob"
#if test $num1 = $num2
#then
#    echo '两个字符串相等!'
#else
#    echo '两个字符串不相等!'
#fi


