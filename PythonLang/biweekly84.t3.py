from collections import defaultdict
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


if __name__ == '__main__':

    param = [2, 7, 11, 15]
    tree = operations_bi_tree()
    tree.leetcode_level_build_tree(tree_val=param)
    print(tree.tree_root.val)

    solution = Solution()
    result = solution.test(a=param)
    print(result)

    
    tasks = [1,2,1,2,3,1]
    space = 3


    days = 0
    i = 0
    while i < len(tasks):
        print(i)
        print(tasks[max(0,i-space):i])
        if days == 0:
            days += 1
            i += 1
        elif tasks[i] in tasks[max(0,i-space):i]:
            relax = space-tasks[:i][::-1].index(tasks[i])
            # print(relax)
            # print(tasks[:i][::-1].index(tasks[i]))
            days += relax+1
            tasks = tasks[:i] + [0]*relax + tasks[i:]
            i += relax+2
            print(tasks)
        else: 
            days += 1
            i += 1

        
    