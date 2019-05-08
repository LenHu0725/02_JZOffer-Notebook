# -*- coding:utf-8 -*-
"""
名称：表示数值的字符串
题目：实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
     例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。 
     但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。
测试：功能测试：正数或者负数；
             包含或者不包含整数的数值；
             包含或者不包含小数部分的数值；
             包含或者不包含指数部分的数值；
             各种不能表达有效数值的字符串；
     特殊测试：输入字符串和模式字符串是null、空字符串；
"""

# 思路一：使用python的float强行转换


# 思路二：
# 1. 所有数值模式都可表示为 A[.[B]][e|EC] or .B[e|EC]；
# 2. B为小数 C为指数；
# 3. 没有整数部分时 必有小数部分；
# 4. A,C 前可有“+”与“-”；

class Solution:
    def isNumber(self, s):
        """  
        判断是否为数字
        输入：
        - s：输入的字符串
        输出：
        - True/False：是否为数值
        """
        # 异常处理
        if not s or len(s)<=0:
            return False
        alist = [i.lower() for i in s]

        # 假设存在 e 分为两部分分别判断是否为数字
        if 'e' in alist:
            eIndex  = alist.index('e')
            eBefore = alist[:eIndex]
            eAfter  = alist[eIndex+1:]

            if '.' in eAfter or len(eAfter)==0:
                return False

            isFront = self.isDigital(eBefore)
            isAfter = self.isDigital(eAfter)
            return isFront and isAfter

        else:
            return self.isDigital(alist)


    def isDigital(self, s):
        """
        判断是否为数字
        输入：
        - s：输入字符串
        输出：
        - True/False：是否为数字
        """
        dotNum = 0
        allowNum = ['0','1','2','3','4','5','6','7','8','9',
                    '+','-','.']

        for i in range(len(s)):
            # 非数字部分
            if s[i] not in allowNum:
                return False
            
            # 包含多个 '.'
            if s[i] == '.':
                dotNum += 1

            # +-位置不正确
            if s[i] in '+-' and i!=0:
                return False

        if dotNum > 1:
            return False

        return True

            
        