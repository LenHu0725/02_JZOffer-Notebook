# -*- coding: utf-8 -*-
"""
名称：正则表达式匹配
题目：实现一个函数用来匹配包括'.'和'*'的正则表达式。
     模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（包含0次）。 
     在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配。
测试：功能测试（模式字符串里包含普通字符、‘.'、’*‘；模式字符串和输入字符串匹配/不匹配）
     特殊输入测试（输入字符串和模式字符串是nullptr、空字符串）
"""

# 解题思路：
# 利用递归的思想 将模式和字符串向后轮换对比

class Solution:
    def match(self, s, pattern):
        """
        匹配字符串
        输入：
        - s:字符串
        - pattern:模式
        输出：
        - True / False
        """
        # 异常处理
        if len(s)==0 and len(pattern)==0:
            return False
        
        if len(s)>0 and len(pattern)==0:
            return False

        # 模式中的第二个字符是“*”时
        if len(pattern)>1 and pattern[1]=='*':
            # 如果字符串第一个模式跟模式第一个字符匹配（相等或匹配到“.”），可以有3种匹配方式
            if len(s)>0 and (pattern[0]==s[0] or pattern[0]=='.'):
                # 1、模式后移2字符，相当于x*被忽略；
                # 2、字符串后移1字符，模式后移两字符；
                # 3、字符串后移1字符，模式不变，即继续匹配字符下一位，因为*可以匹配多位
                return self.match(s, pattern[2:]) or self.match(s[1:], pattern[2:]) or self.match(s[1:], pattern)
            else:
                return self.match(s[1:], pattern[2:])

        # 当模式中的第二个字符不是“*”时：
        if len(s)>0 and (s[0]==pattern[0] or pattern[0]=='.'):
            # 1、如果字符串第一个字符和模式中的第一个字符匹配（相等或匹配到“.”），那么字符串和模式都后移一个字符，然后匹配剩余的
            return self.match(s[1:], pattern[1:])
            # 2、如果字符串第一个字符和模拟中的第一个字符相不匹配，直接返回False
        return False
