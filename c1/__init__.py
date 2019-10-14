# 1.输出控制台打印语法
print("你好世界")  # 直接打印字符串
print("你", "好", "世界")  # 用逗号分隔多个字符串 但会但打印空格
print(100)  # 打印数字
print(100+100)  # 打印运算
print("100 + 100 =", 100+100)  # 能够和字符串组合

# 2.输入控制台语法
# name=input() # 使用变量接收输入 这个方法会线程阻塞
# print(name)

# 3.数据类型
# ==整数
# ==浮点数 比较大的数呢 要这样写 例如1200的20次方
n = 1200e20
# ==字符串
name = '你好世界'  # 单引号
print(name)
name = "你好世界"  # 双引号
print(name)
name = "你好 \n \t 世界"  # 换行，空格
print(name)
name = "你\'你好\"世界"  # 转义
print(name)
name = r'神奇\' '  # r'' 语法中的字符串都不会转义
print(name)
name ='''你
好 
世
界    
'''  # 换行语法糖
print(name)

len(name)

# ==布尔值
i1 = True  # 是
i2 = False  # 否
i = i1 and i2  # 布尔值运算 与
i = i1 or i2  # 或
i = not i  # 非

# ==空值
name = None

# 4.变量 常量 python中没有常量的概念 一般用大写代替常量的习惯 实际他还是变量 所以还是可以修改的
name = " 我是变量"
NAME = "我是常量"

# 5.运算比java多了点花里胡哨的玩意
a = 10
b = 10.1
c = b/a  # 计算结果是浮点数 即使两个数都是整数 结果也是浮点数
d = b//a  # 计算结果是真那个整数 这个才相当于java的除法
e = b % a  # 这就是和java一样的取余了

# 6.字符串编码 Unicode编码
q = ord("中")  # 查看单字符的Unicode编码
w = chr(25991)  # 把数字转化成单字符
print(q, w)

e = '\u4e2d\u6587'  # 字符串还用16进制表示 等价于直接写中文
print(e)

r = b"aa123"  # 虽然看起来一样 但是用b"" 是ascii码 每个字符都只占用一个字节所以不能用来表示中文 其实就是java中的byte数组
print(r)

print("123qwe".encode("ascii"))  # 将Unicode 转化成ascii
print("你好世界".encode("utf-8"))  # 转化成utf-8

print(b"\xe4\xb8\xad\xe6\x96\x87".decode("utf8"))  # 在转回来


# 循环语法
# ==循环字符串
for char in "你好世界":
    print("当前字符："+char)
