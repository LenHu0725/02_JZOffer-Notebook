# -*- coding:utf-8 -*-
"""
名称：二叉搜索树的后序遍历序列
题目：输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
     如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
测试：功能测试：输入后序遍历序列对应一棵二叉树，包括完全二叉树，所有节点都没有左/右子树的二叉树、只有一个节点的二叉树；
     输入的后序遍历序列没有对应一棵二叉树。
     特殊测试：指向后序遍历序列的指针为nullptr指针。
"""

# 解题思路：递归，数组最后必为根节点，左子树根节点值<根节点值<右子树根节点值

class Solution:
    def VerifySequenceOfBST(self, sequence):
        # 异常处理
        if not sequence or len(sequence)<=0:
            return False


        # 找出左右分界点
        idx = 0
        while sequence[idx]<sequence[-1]:
            idx += 1
            

        # 验证右子树是否存在小于根节点值
        for i in sequence[idx:-1]:
            if i < sequence[-1]:
                return False


        # 左子树是否为搜索二叉树
        left = True
        if idx>0:
            left = self.VerifySequenceOfBST(sequence[:idx])

        # 右子树是否为搜索二叉树
        right = True
        if len(sequence)-1>idx:
            right = self.VerifySequenceOfBST(sequence[idx:-1])


        return left&right


# 测试：
seq1 = [5, 7, 6, 9, 11, 10, 8]
seq2 = [7, 4, 6, 5]
solu = Solution()
print(solu.VerifySequenceOfBST(seq1))
print(solu.VerifySequenceOfBST(seq2))