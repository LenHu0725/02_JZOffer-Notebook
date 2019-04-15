# -*- coding: utf-8 -*-
"""
名称：剪绳子
题目：给一根长度为n的绳子，剪成m段（m,n都是整数，且n>1, m>1）
     每段绳子的长度为k[0],k[1],k[2]....,k[m]，所有K的最大乘积是多少？
测试：功能测试：绳子初始长度大于等于5；
     边界测试：绳子长度为 0，1，2，3，4；
"""

class Solution:
    def MaxProductAfterCut1(self, n):
        """
        动态规划
        时间复杂度：O(n^2)；空间复杂度：O(n)；
        输入：
        - n：绳子长度
        输出：
        - s：乘积
        """
        if n<2:
            return 0
        elif n==2:
            return 1
        elif n==3:
            return 2

        products = [0]*(n+1)
        # 为什么设置到3:可手动列出绳子长度与最大乘积的关系
        # 绳长->乘积： 1->1 2->1 3->2 4->4 5->6
        # 当绳长大于3时 最大乘积超过绳长
        products[0] = 0
        products[1] = 1
        products[2] = 2
        products[3] = 3

        for i in range(4, n+1):
            max = 0
            for j in range(1, i//2+1):
                product = products[j]*products[i-j]
                if product>max:
                    max = product
            products[i]=max

        return products[n]


    def MaxProductAfterCut2(self, n):
        """
        贪婪算法
        时间复杂度：O(1)；空间复杂度：O(1)；
        输入：
        - n：绳子长度
        输出：
        - n：乘积
        """
        if n<2:
            return 0
        elif n==2:
            return 1
        elif n==3:
            return 2

        timeOf3 = n//3
        if (n-3*timeOf3)==1:
            timeOf3 -= 1
        timeOf2 = (n-3*timeOf3)//2

        return (3**timeOf3)*(2**timeOf2)
