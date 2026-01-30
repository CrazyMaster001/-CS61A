#1.2阅读笔记#
a = 1
b = 2
a = b
a = 3
# 变量a最初指向整数1，变量b指向整数2。执行a = b后，a开始指向整数2。随后执行a = 3时，a又开始指向整数3，而b仍然指向整数2。这说明变量是名称的绑定，可以重新绑定到不同的对象上。

#纯函数与非纯函数
abs(-1) #打印出1
print(-1) #打印出-1 但非纯函数print会产生副作用，自动return None,所以print(-1)的返回值是None，不过这里没有打印出来
print(print(1), print(2)) #先打印1和2，然后打印None None
# print() 的工作：
# 1. 把参数显示到屏幕上（副作用）  print() 的主要目的是产生副作用（在屏幕上显示内容），而不是返回值
# 2. 返回 None（返回值）

result = print("Hello")  
# 屏幕上显示: Hello
# result = None


#1.3阅读笔记#
#传参外到内，设参内到外

#1.4阅读笔记#
from operator import mul
def square(x):
    mul(x, x) # Watch out! This call doesn't return a value.没有return语句，默认返回None

def square(x):
    return mul(x, x)
#加了return语句后，函数square才会返回计算结果
#或者使用赋值语句
def square(x):
    result = mul(x, x)
    return result

def print_square(x):
    print(square(x))

# ❌ 错误：应该返回结果却只打印
def calculate_discount(price, discount_rate):
    final_price = price * (1 - discount_rate)
    print(f"折后价: {final_price}")  # ❌ 只是打印，调用者拿不到结果

# ✅ 正确：返回结果
def calculate_discount(price, discount_rate):
    final_price = price * (1 - discount_rate)
    return final_price  # ✅ 返回给调用者

# 使用
price = calculate_discount(100, 0.2)  # 现在能拿到结果
print(f"您需要支付: {price}")

#短路
True and False
#False
True or False
#True
not False
#True

#迭代
def fib(n):
    """Compute the nth Fibonacci number, for n >= 2."""
    pred, curr = 0, 1   # Fibonacci numbers
    k = 2               # Position of curr in the sequence
    while k < n:        # Loop until we reach position n 循环语句
            pred, curr = curr, pred + curr  # Re-bind pred and curr
            k = k + 1                       # Re-bind k
            return curr
fib(8)
#13

#1.6阅读笔记#
def sum_naturals(n):
     total,k = 0,1
     while k <= n:
          total,k = total + k,k + 1
     return total   #把当前 total 的值返回给调用者  #若不与while对齐，则第一次之后就返回了
     
x = 5  # 把 5 赋给 x（从右到左）

def summation(n,term,next):
     total,k = 0,1
     while k <= n:
          total,k = total + term(k),next(k)
     return total
     
def cube(x):
     return pow(x,3)
def successor(x):
     return x + 1
def sum_cubes(n):
     return summation(n,cube,successor)

def iter_improve(update,test,guess = 1):
     while not test(guess):
          guess = update(guess)
     return guess
def approx_eq(x,y,tolerance = 1e-10):
     return abs(x - y) < tolerance
def near(x,f,g):
     return approx_eq(f(x),g(x))

def golden_update(guess):
     return (1 + 1/guess)
def golden_test(guess):
     return near(guess,square,successor)

from math import sqrt
phi = 1/2 + sqrt(5)/2
def improve_test():
     approx_phi = improve(golden_update, square_close_to_successor)
     assert approx_eq(phi, approx_phi), 'phi differs from its approximation'   #True则不会显示引号内的话
improve_test()



def h(x):
     h(x) = f(g(x))   #错误，函数不可以被赋值，可以写成result = f(g(x))
                      #函数只能调用
     return h         #错误，返回了函数本身

# ❌ 错误
def h(x):
    h = f(g(x))  # 这会覆盖 h 函数本身！
    return h

# 第一次调用后，h 就不再是函数了

def compose1(f,g):
     def h(x):
          return f(g(x))
     return h

#柯里化
def curried_pow(x):
     def h(y):
          return pow(x,y)
     return h

curried_pow(2)(3)


#1.7阅读笔记#
def sum_digits(n):
     if n < 10:
          return n
     else:
          all_but_last,last = n // 10, n % 10
          return sum_digits(all_but_last) + last

def iter_fact(n):
     total,k = 1,1
     while k < n:
          total , k = total * k,k + 1
     return total

def fact(n):
     if n == 1:
          return 1
     else:
          return n * fact(n - 1)
     
def is_even(n):
     if n == 0:
          return True
     else:
          return is_odd(n-1)
def is_odd(n):
     if n == 1:
          return True
     else:
          return is_odd(n-1)
     
def cascade(n):
     if n <10:
          print(n)
     else:
          print(n)
          cascade(n // 10)
          print(n)
#真的会用到吗
#互递归，可能类似于概率里面马尔科夫链（其实也不是，就是高中数学概率里要多设几个P，P1,P2之类的，并且先分几个初始场景讨论）

#双人游戏：桌子上最初有 n 个石子，玩家轮流从桌面上拿走一个或两个石子，拿走最后一个石子的玩家获胜。假设 Alice 和 Bob 在玩这个游戏，两个人都使用一个简单的策略：

#Alice 总是拿走一个石子
#如果桌子上有偶数个石子，Bob 就拿走两个；否则拿走一个
#给定 n 个初始石子且 Alice 先手，谁会赢得游戏？

def play_Alice(n):
     if n == 1:
          print("Alice wins")
     else:
          return play_Bob(n-1)
def play_Bob(n):
     if n % 2 == 0:
          return play_Alice(n - 2)
     else:
          return play_Alice(n-1)
     

def fib(n):
     if n == 1:
          return 0
     elif n == 2:
          return 1
     else:
          return fib(n-2) + fib(n-1)
     
def count_partitions(n,m):
     if n == 0:
          return 1
     elif n < 0 :
          return 0
     elif m == 0:
          return 0
     else:
          return count_partitions(n,m-1) + count_partitions(n-m,m)
