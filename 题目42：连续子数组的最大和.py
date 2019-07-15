# -*- coding: utf-8 -*-
"""
名称：连续子数组的最大和
题目：输入一个整形数组，数组里有正数也有负数。
     数组中的一个或连续多个整数组成一个子数组。
     所有子数组的和的最大值。要求时间复杂度为O（n）
测试：功能测试：输入的数组中有正数也有负数；
             输入的数组中全是 正数/负数；
     边界测试：输入数组的指针为null；
     负面测试：
"""

# 解题思路： 动态规划
class Solution:
    g_InvalidInput=False

    def FindGreatestSumOfSubArray(self, array):
        # write code here
        if not array or len(array)<=0:
            g_InvalidInput=True
            return 0
        
        g_InvalidInput=False
        curSum=0
        greatSum=float('-inf')

        for i in array:
            if curSum<=0:
                curSum=i
            else:
                curSum+=i
            if curSum>greatSum:
                greatSum=curSum

        return greatSum