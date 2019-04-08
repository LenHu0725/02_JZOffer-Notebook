# -*- coding:utf-8 -*-
"""
名称：  斐波那契数列
题目：  写一个函数，输入整数n，输出斐波那契数列第n项;
测试：
"""

class Solution_1:
    def Fibonacci(self, n):
        """
        循环计算
        输入：
        - n：   输出的斐波那契数列位数；
        输出：
        - nNum：斐波那契数列的第n个数；
        """
        if n<=0:
            return 0
        elif n==1 or n==2:
            return 1
        
        fn  = 0
        fn1 = 1
        fn2 = 1

        for _ in range(2, n+1):
            fn  = fn1+fn2
            fn2 = fn1
            fn1 = fn

        return fn 


class Solution_2:
    def Fibonacci(self, n):
        """
        递归计算
        时间复杂度：nlog(n)
        输入：
        - n：   输出的斐波那契数列位数；
        输出：
        - nNum：斐波那契数列的第n个数；
        """
        if n<=0:
            return 0
        elif n==1 or n==2:
            return 1
        else:
            return self.Fibonacci(n-1)+self.Fibonacci(n-2)


class Solution_3:
    def Fibonacci(self, n):
        """
        矩阵求解法
        输入：
        - n：   输出的斐波那契数列位数；
        输出：
        - nNum：斐波那契数列的第n个数；
        """
        import numpy as np

        w = np.array([[1, 1], [1, 0]])
        x = np.array([[1], [1]])

        if n<0:
            return 0
        elif n==1 or n==2:
            return 0

        for _ in range(2, n):
            x = np.dot(w, x)

        return x[1]


        
"""
名称：  青蛙跳台阶
题目：  一只青蛙一次可以跳上1级台阶，也可以跳上2级。
        求该青蛙跳上一个n级的台阶总共有多少种跳法。
测试：  
"""

class Solution_4:
    def JumpFloor(self, number):
        if number<0:
            return 0
        elif number==1:
            return 1
        elif number==2:
            return 2

        for _ in range(2, number+1):
            return self.JumpFloor(number-1)+self.JumpFloor(number-2)



"""
名称：  升级版青蛙跳台阶
题目：  一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。
        求该青蛙跳上一个n级的台阶总共有多少种跳法。
测试：  
"""
class Solution_5:
    def JumpFloor(self, number):
        """
        数学归纳法
        """
        return 2**(number-1)


"""
名称：  矩形覆盖
题目：  用2*1的小矩形 横着或竖着 覆盖更大矩形。
        用n个2*1的小矩形无重叠地覆盖2*n个大矩形 有多少种方法？
测试：
"""
class Solution_6:
    def rectCover(self, number):
        """
        还是可以看成 f(n) = f(n-2)+f(n-1) 的斐波那契数列问题
        输入:
        - number: 输入数据
        """
        if number<=0:
            return 0
        elif number==1:
            return 1
        elif number==2:
            return 2

        fn_1 = 1
        fn_2 = 2
        for i in range(3, number):
            s = fn_1 + fn_2
            fn_2 = fn_1
            fn_1 = s

        return s
        