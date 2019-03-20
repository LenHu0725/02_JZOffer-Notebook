# -*- coding: utf-8 -*-
"""
名称:   替换空格
题目:   请实现一个函数，将一个字符串中的空格替换成“%20”。
        例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
测试:   输入包括空格（空格在最前 在最后 在中间 多个连续空格）
        输入字符串没有空格
        特殊输入（空指针 空字符串 只有一个空格 多个连续空格）
"""

class Solution_1:
    def __init__(self):
        pass
    
    def replaceSpace(self, s):
        return '%20'.join(s.split(' '))


class Solution_2:
    def __init__(self):
        pass

    def replaceSpace(self, s):
        return s.replace(' ', '%20')


class Solution_3:
    def __init__(self):
        pass
    
    def replaceSpace(self, s):
        """
        遍历一次字符 从后到前排序 【重点掌握从后向前赋值 保护内存】
        时间复杂度N(n) 空间复杂度(n)
        输入
        - s: 一段字符串

        输出
        - s: 替换空格的字符串
        """
        # S1: 获得字符串长度 与空格数量
        s = list(s)
        spaceCount = 0
        for e in s:
            if e==' ':
                spaceCount+=1
        p1 = len(s)-1

        # S2: 倒序赋值list
        s += [None]*2*spaceCount 
        p2 = len(s)-1

        while (p1 >= 0):
            if s[p1]!=' ':
                s[p2] = s[p1]
                p2 -= 1
            else:
                s[p2-2] = '%'
                s[p2-1] = '2'
                s[p2]   = '0'
                p2 -= 3
            p1 -= 1
        
        return ''.join(s)

