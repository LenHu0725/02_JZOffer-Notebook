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

        
        




