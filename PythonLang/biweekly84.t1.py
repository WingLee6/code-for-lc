from typing import List, Optional
from Tools.operations_tree import operations_bi_tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def test(self, a: int):
        print("Testing Solution")
        return False

from collections import defaultdict

if __name__ == '__main__':

    param = [2, 7, 11, 15]
    tree = operations_bi_tree()
    tree.leetcode_level_build_tree(tree_val=param)
    print(tree.tree_root.val)

    solution = Solution()
    result = solution.test(a=param)
    print(result)

    
    # cases=[
    # [1,'用例1','www,baidu.com','001','ok'],
    # [4,'用例4','www,baidu.com','002','ok'],
    # [2,'用例2','www,baidu.com','002','ok'],
    # [3,'用例3','www,baidu.com','002','ok'],
    # [5,'用例5','www,baidu.com','002','ok'],
    # ]
    # list1=[]
    # for i in range(1,5):
    #     list1.append(dict(zip(cases[0],cases[i])))
    # print(list1)


    items1 = [[1,1],[4,5],[3,8]]
    items2 = [[3,1],[1,5]]
    items1 = dict(items1)
    items2 = dict(items2)
   
    for key in items1.keys():
        
        if key in items2:
            items1[key] += items2[key]
            del items2[key]
    print(items1)
    if items2:
        items1.update(items2)  
    
    print(items1)
    print(items2) 


    dictlist=[]
    for keys, value in sorted(items1.items()):
        temp = [keys,value]
        dictlist.append(temp)
    


    
