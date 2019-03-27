# -*- coding:utf-8 -*-
"""
名称:   重建二叉树
题目:   输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
        假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
        例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
测试：  普通二叉树（完全二叉树 不完全二叉树）
        特殊二叉树（所有节点都没有右子节点的二叉树、只有一个节点的二叉树）
        特殊输入测试（二叉树的根结点指针为nullptr，输入的前序遍历序列和中序遍历序列不匹配）
"""


class TreeNode:
    """ 定义树 """
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def reConstructTree(self, pre, tin):
        """
        递归 重建二叉树
        输入：
        - pre: 前序遍历序列
        - tin: 中序遍历序列
        输出：
        - result: 输出结果
        """
        
        # 递归到头
        if not pre or not tin:
            return None

        tree = TreeNode(pre[0])
        count = tin.index(pre[0])

        tree.left = self.reConstructTree(pre[1:count+1], tin[:count])    # 前序的前1:count+1 中序的前count 是左树
        tree.right = self.reConstructTree(pre[count+1:], tin[count+1:])  # 中序的后count+1 中序的后count+1 是右树

        return tree


# 测试 输出某层树
preTree = [1, 2, 4, 7, 3, 5, 6, 8,]
tinTree = [4, 7, 2, 1, 5, 3 ,8, 6,]

test = Solution()
newTree = test.reConstructTree(preTree, tinTree)

def printNodeLevel(tree, level):
    """
    输出树的某层
    输入：
    - tree:  输入的树
    - level: 输出层数
    输出：
    - 某层的数值
    """
    # S1: 异常和特殊处理
    if not tree or level<0 :
        return 0

    # S2: 树输出
    if level == 0:
        print(tree.val)
        return 1
    
    printNodeLevel(tree.left, level-1)
    printNodeLevel(tree.right, level-1)


def printTree(tree, depth):
    for i in range(depth):
        print("Depth {} is : ".format(i))
        printNodeLevel(tree, i)


printTree(newTree, 4)
# 最终输出为 1, 2 3, 4 5 6, 7 8
