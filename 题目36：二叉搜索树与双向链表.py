# -*- coding:utf-8 -*-
"""
名称：二叉搜索树与双向链表
题目：输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
     要求不能创建任何新的结点，只能调整树中结点指针的指向。
测试：功能测试：输入的二叉树是完全二叉树；
     所有节点都没有左/右子树的二叉树；
     只有一个节点的二叉树；
     特殊输入测试：指向二叉树根节点的指针为nullptr指针；
"""

class TreeNode:
     def __init__(self, x):
          self.val = x
          self.left = None
          self.right = None


# 解题思路一：借助辅助空间
class Solution:
     def Convert(self, pRootOfTree):
          if not pRootOfTree:
               return None

          self.attr=[]
          self.inOrder(pRootOfTree)

          for i,v in enumerate(self.attr[-1]):
               self.attr[i].right = self.attr[i+1]
               self.attr[i+1].left = v

          return self.attr[0]

     def inOrder(self, root):
          if not root:
               return None

          self.inOrder(root.left)
          self.attr.append(root)
          self.inOrder(root.right)



# 解题思路二：递归
class Solution:
     def Convert(self, pRootOfTree):
          if not pRootOfTree:
               return None

          root = pHead = pRootOfTree

          while pHead.left:
               pHead = pHead.left

          self.Core(root)
          return pHead

     def Core(self, root):
          if not root.left and not root.right:
               return None

          if root.left:
               preRoot = root.left
               self.Core(root.left)
               
               while preRoot.right:
                    preRoot = preRoot.right
               
               preRoot.right = root
               root.left = preRoot

          if root.right:
               nextRoot = root.right
               self.Core(root.right)

               while nextRoot.left:
                    nextRoot = nextRoot.left

               nextRoot.left = root
               root.right = nextRoot
               
