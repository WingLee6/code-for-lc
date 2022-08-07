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


if __name__ == '__main__':

    param = [2, 7, 11, 15]
    tree = operations_bi_tree()
    tree.leetcode_level_build_tree(tree_val=param)
    print(tree.tree_root.val)

    solution = Solution()
    result = solution.test(a=param)
    print(result)

    n = 7
    edges = [[0,1],[1,2],[3,1],[4,0],[0,5],[5,6]]
    restricted = [4,5]

    n = 7
    edges = [[0,1],[0,2],[0,5],[0,4],[3,2],[6,5]]
    restricted = [4,2,1]

    visit = 0
    queue = [0]
    visited = []
    while queue:
        
        v = queue[0]
        visited.append(v)
        print(v)
        visit += 1
        queue.pop(0)

    
                
        tmp = [p[1] for p in edges if p[0]==v and p[1] not in restricted and p[1] not in visited]
        tmp2 = [p[0] for p in edges if p[1]==v and p[0] not in restricted and p[0] not in visited]
        # print(tmp)
        # print(tmp2)
        queue += (tmp + tmp2)
        
        for p in edges:
            if p[0]==v or p[1]==v:
                edges.remove(p)
        

    
    print(visit)

    
        
        
    