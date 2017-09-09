print("输出")
s="这是一个字符串"
#s[0]#第一个字符
s=s[0:2]#分割出前两个字符
#s[2:]#第三个字符以后的
print(s)

list=['abcd',123,2023,'john',70.2]
tinylist=[123,'john']
print(list)#可以使用[:]来分割数组

tuple=('abcd',123,2023,'john',70.2)#元组  一个不可二次赋值的数组

dict={}#字典 通过键值对来存储数据
dict['one']="this is one"
dict[2]="this is tow"

tinydict={'name':'john','code':6734}#字典的另一种声明形式

print (dict['one'])#输出字典 dict 中 one 键的值
print (dict)
