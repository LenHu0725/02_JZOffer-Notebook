# -*- coding:utf-8 -*-
"""
名称：二叉树中和为某一值的路径
题目：输入一颗二叉树和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
     路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
测试：功能测试：二叉树没有符合要求的路径，二叉树有一条或多条符合的路径；
     特殊测试：二叉树指针为Null；
"""

# 解题思路：
#   树的结构利用递归，依次遍历到每个叶节点；
#   通过栈的方式对加和过程建模；


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = x
        self.right = x


class Solution:
    def FindPath(self, root, expectNumber):
        """
        返回二维列表 内部每个列表表示找到路径
        Input：
        - root：根节点
        - expectNumber：期望加和结果
        """
        if not root:
            return []

        result = []


        def FindPathCore(self, root, path, currentNum):
            """
            寻找路径
            Input：
            - path：
            - currentNum：
            """
            # 求和 将当前数字加入队列
            currentNum += root.val
            path.append(currentNum)

            # 判断是否到达叶子节点
            flag = (root.left==None and root.right==None)
            
            # 达到叶子节点且为期望值
            if currentNum==expectNumber and flag:
                onepath = []

                for node in path:
                    onepath.append(node.val)

                result.append(onepath)

            # 如果没有达到叶子节点
            if currentNum < expectNumber:

                if root.left:
                    self.FindPathCore(root.left, path, currentNum)
                if root.right:
                    self.FindPathCore(root.right, path, currentNum)

            path.pop()

        FindPathCore(root, [], 0)
        return result
