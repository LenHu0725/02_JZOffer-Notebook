# -*- coding: utf-8 -*-
"""
名称：字符串的排列
题目：输入一个字符串,按字典序打印出该字符串中字符的所有排列。
     例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
测试：功能测试：输入的字符串有一个或多个字符；
     特殊测试：输入的字符串内容为空或Null；
"""

# 解题思路：将字符串看成两部分，第一部分是它的第一个字符；
#         第二部分是后面的所有字符。递归

class Solution:
    def Permutation(self, ss):
        
        if not ss:
            return []

        if len(ss)==1:
            return list(ss)

        pStr = []
        charlist = list(ss)
        charlist.sort()

        for i in range(len(charlist)):
            if i>0 and charlist[i]==charlist[i-1]:
                continue

            temp = self.Permutation(''.join(charlist[:i])+''.join(charlist[i+1:]))

            for j in temp:
                pStr.append(charlist[i]+j)

        return pStr