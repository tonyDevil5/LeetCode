# -*- coding: utf-8 -*-
"""
Created on Mon May 29 11:13:37 2017

@author: hongyangyu
"""
import pdb
import copy
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def pathSumHelper(root, curSum, resultList, totalPaths, sumT):
    curSum += root.val    
    if root.left is None and root.right is None:
        if curSum == sumT:
            resultListCopy = copy.deepcopy(resultList)
            resultListCopy.append(root.val)
            totalPaths.append(resultListCopy)
    else:
        pdb.set_trace()
        resultList.append(root.val)
        if root.left is not None:
            pathSumHelper(root.left, curSum, resultList, totalPaths, sumT)
        if root.right is not None:
            pathSumHelper(root.right, curSum, resultList, totalPaths, sumT)
        resultList.pop()
    
    
def pathSum(root, sumT):
    """
    :type root: TreeNode
    :type sum: int
    :rtype: List[List[int]]
    """
    if root is None:
        return []
    else:
        totalPaths = []
        pathSumHelper(root, 0, [], totalPaths, sumT)
        return totalPaths

def sortedArrayToBST(nums):
    """
    :type nums: List[int]
    :rtype: TreeNode
    """
    if len(nums) == 0:
        return None
    elif len(nums) == 1:
        leaf = TreeNode(nums[0])
        leaf.left = None
        leaf.right = None
        return leaf
    else:
        midNumInd = len(nums)/2
        midNum = nums[midNumInd]
        root = TreeNode(midNum)
        pdb.set_trace()
        if midNumInd == 0:
            root.left = None
            root.right = sortedArrayToBST(nums[midNumInd+1:len(nums)])
        elif midNumInd == len(nums)-1:
            root.right = None
            root.left = sortedArrayToBST(nums[0:midNumInd])
        else:
            root.left = sortedArrayToBST(nums[0:midNumInd])
            root.right = sortedArrayToBST(nums[midNumInd+1:len(nums)])
        return root
        
def helper(ele, itemList):
    for item in itemList:
        if item%ele != 0 and ele%item != 0:
            return False
    return True
    
def largestDivisibleSubset(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    if len(nums) == 0:
        return []
    prevList = []
    for i in range(len(nums)):
        if i == 0:
            prevList.append([nums[i]])
        else:
            curList = []
            #pdb.set_trace()
            for item in prevList:
                #pdb.set_trace()
                boo = helper(nums[i], item)
                if boo:
                    newItem = copy.deepcopy(item)
                    newItem.append(nums[i])
                    curList.append(newItem)
                    curList.append(item)
                else:
                    curList.append(item)
                    curList.append([nums[i]])
                prevList = curList
    maxInd = 0
    maxLen = 0
    for i in range(len(prevList)):
        if len(prevList[i]) > maxLen:
            maxLen = len(prevList[i])
            maxInd = i
    return prevList[maxInd]
        

if __name__ == '__main__':
    """
    a = TreeNode(5)
    a.left = TreeNode(4)
    a.right = TreeNode(8)
    a.left.left = TreeNode(11)
    a.left.left.left = TreeNode(7)
    a.left.left.right = TreeNode(2)
    a.right.left = TreeNode(13)
    a.right.right = TreeNode(4)
    a.right.right.left = TreeNode(5)
    a.right.right.right = TreeNode(1)
    b = pathSum(a, 22)
    """
    