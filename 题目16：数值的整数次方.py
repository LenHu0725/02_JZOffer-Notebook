# -*- coding:utf-8 -*-
"""
名称：数值的整数次方
题目：实现函数double Power(double base, int exponent)，
     求base的exponent次方、不得使用库函数，同时不需要考虑大数问题。
补充：底数和指数分别设为 正数、负数和零
"""

class Solution1:
    g_InvalidInput = False    # 返回全局变量用于判断是否为错
    def Power(self, base, exponent):
        """ 考虑底数为0.0 指数为负数
        输入：
        - base: [double] 底数
        - exponent: [int] 指数
        输出：
        - result: 输出结果
        """
        if base == 0.0 and exponent<0 :
            g_InvalidInput = True
            return 0.0    # 返回值为0表示错误

        if exponent>=0:
            return self.PowerWithUnsignedExponent(base, exponent)
        
        return 1 / self.PowerWithUnsignedExponent(base, -exponent)


    def PowerWithUnsignedExponent(self, base, exponent):
        """ 乘次方函数
        输入：
        - base: [double] 输入底数 
        - exponent: [int] 指数次方
        输出：
        - restult: 结果
        """
        result = 1.0
        for i in range(exponent):
            result *= base

        return result


num = Solution1()
print("Result number is: ", num.Power(4.0, 4))
print("Error is : ", num.g_InvalidInput)



class Solution2:
    def __init__(self):
        self.g_InvalidInput = False

    def Power(self, base, exponent):
        """ 使用平方的一半乘以平方的一半 递归的方法
        输入：
        - base: [double] 输入底数 
        - exponent: [int] 指数次方
        输出：
        - restult: 结果
        """
        if exponent == 0:
            return 1
        if base==0.0 and exponent<0:
            self.g_InvalidInput = True
            return 0.0

        if exponent>=0:
            return self.PowerWithUnsignedExponent(base, exponent)
        
        return 1.0/self.PowerWithUnsignedExponent(base, -exponent)

    
    def PowerWithUnsignedExponent(self, base, exponent):
        """ 使用迭代的方法完成幂指数相乘
        输入：
        - base: [double] 输入底数 
        - exponent: [int] 指数次方
        输出：
        - restult: 结果
        """
        if exponent==0:
            return 1
        if exponent==1:
            return base

        res = self.PowerWithUnsignedExponent(base, exponent>>1)
        res *= res
        if exponent & 0x1==1:
            res*=base
        return res


num2 = Solution2()
print(num2.Power(5.0, 4))
