# -*- coding:utf-8 -*-
"""
名称：从上到下打印二叉树
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 题目：不分行从上到下打印二叉树
# 解题思路：用队列存储的方式，从上到下遍历；
# 测试：功能测试：完全二叉树，所有节点只有左子节点的二叉树，只有右子节点的二叉树；
#      边界测试：二叉树为空，只有一个根节点的二叉树；
class Solution:
    def PrintFromTopToBottom(self, root):
        """
        打印二叉树
        输入：
        - root：输入根节点
        """
        # 异常处理
        if not root:
            return []

        res = []
        res_val = []
        res.append(root)

        while( len(res)>0 ):
            node = res.pop(0)

            res_val.append(node.val)

            if not node.left:
                res.append(node.left)
            
            if not node.right:
                res.append(node.right)
        
        return res_val


# 题目：分行从上到下打印二叉树
# 解题思路：
# 测试：
class Solution2:
    def print(self, pRoot):
        """
        打印二叉树
        输入：
        - pRoot: 输入根节点
        """

        if not pRoot:
            return []

        res, nodes = [], [pRoot]

        while nodes:
            # 当前行与下一行Node
            cur_stack, next_stack = [], []
            
            # 添加下一行Node
            for node in nodes:
                if node.left:
                    next_stack.append(node.left)

                if node.right:
                    next_stack.append(node.right)
                
            # 更换下一行Node
            res.append(cur_stack)
            nodes = next_stack
        
        return res


# 解题思路：cur last 记录
class Solution3:
    def Print(self, pRoot):
        """ 
        打印二叉树
        输入：
        - pRoot: 输入根节点
        """
        # 异常处理
        if not pRoot:
            return []
        
        res, res_val = [pRoot], []
        cur = 0

        while cur<len(res):
            last = len(res)
            temp = []

            while (cur<last):
                temp.append(res[cur].val)

                if res[cur].left:
                    res.append(res[cur].left)

                if res[cur].right:
                    res.append(res[cur].right)

                cur += 1
            
            res.append(temp)

        return res
        

class Solution4:
    def Print(self, pRoot):
        """
        之字形打印
        输入：
        - pRoot: 根节点
        """
        # 异常处理
        if not pRoot:
            return []

        # 之字形打印
        res, nodes = [], [pRoot]
        treeReverse = False

        while nodes:
            curStack, nextStack = [], []

            for node in nodes:
                curStack.append(node.val)

                if node.left:
                    nextStack.append(node.left)

                if node.right:
                    nextStack.append(node.right)

            if treeReverse:
                curStack.reverse()

            res.append(curStack)
            treeReverse = not treeReverse
            nodes = nextStack
