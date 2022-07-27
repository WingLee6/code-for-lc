from re import L
from typing import List, Optional

from matplotlib import pyplot as plt
from Tools.operations_node import ListNode
from Tools.operations_tree import operations_bi_tree


class Solution:
    def test(self, a: int):

        return False


class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.foods = foods
        self.cuisines = cuisines
        self.ratings = ratings

    def changeRating(self, food: str, newRating: int) -> None:
        self.ratings[self.foods.index(food)] = newRating

    def highestRated(self, cuisine: str) -> str:
        max_food_id = -1
        for i in range(len(self.foods)):
            if self.cuisines[i] == cuisine:
                if max_food_id == -1:
                    max_food_id = i
                elif self.ratings[i] > self.ratings[max_food_id]:
                    max_food_id = i
                elif self.ratings[i] == self.ratings[max_food_id]:
                    max_food_id = self.foods.index(
                        min(self.foods[i], self.foods[max_food_id]))

        return self.foods[max_food_id] if max_food_id != -1 else None

print("-----------------")

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class CBTInserter:

    def __init__(self, root: TreeNode):
        self.root = root  
        self.queue = []

        if root:
            p = root
            self.queue.append(p)
            while self.queue:
                p = self.queue[0]
                if p.left:
                    self.queue.append(p.left)
                if p.right:
                    self.queue.append(p.right)
                    self.queue.pop(0)
                if not (p.left and p.right):
                    break
                    
        
    def insert(self, val: int) -> int:
        q = TreeNode()
        q.val = val
        if not self.root:
            self.root = q
            self.queue.append(self.root)
            return None

        elif self.root:
            p = self.queue[0]
            if not p.left:
                p.left = q
                self.queue.append(p.left)
            elif not p.right:
                p.right = q
                self.queue.append(p.right)
                self.queue.pop(0)
        
            return p.val

    def get_root(self) -> TreeNode:
        return self.root


# Your CBTInserter object will be instantiated and called as such:

from Tools.operations_tree import operations_bi_tree
print("-----------------")
tree = operations_bi_tree()
tree.leetcode_level_build_tree([1, 2])

obj = CBTInserter(tree.tree_root)
param_1 = obj.insert(2)
print(param_1)
param_2 = obj.get_root()
print(param_2)



if __name__ == '__main__':

    # 周赛待整理
    # foods = ["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"]
    # cuisines = ["korean", "japanese", "japanese",
    #             "greek", "japanese", "korean"]
    # ratings = [9, 12, 8, 15, 14, 7]

    # obj = FoodRatings(foods, cuisines, ratings)
    # param_2 = obj.highestRated("korean")
    # print(param_2)
    # param_2 = obj.highestRated("japanese")
    # print(param_2)
    # obj.changeRating("sushi", 16)
    # obj.changeRating("ramen", 16)
    # param_2 = obj.highestRated("japanese")
    # print(param_2)

    # param = [2, 7, 11, 15]
    # tree = operations_bi_tree()
    # tree.leetcode_level_build_tree(tree_val=param)
    # print(tree.tree_root)

    # solution = Solution()
    # result = solution.test(a=param)
    # print(result)



    # 输入：
    # "abccbaacz"
    # 预期：
    # "c"
    # input = Solution()
    # input.test(a=param)
    nums = [1, 3, 4, 5, 6, 7, 8, 9]
    print(nums[len(nums):])




    