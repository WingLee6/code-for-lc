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

    # grid = [[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]
    # grid = [[3, 2, 1], [1, 7, 6], [2, 7, 7]]
    # num = 0
    # t_grid = list(map(list, zip(*grid)))
    #
    # for cow in grid:
    #     num += t_grid.count(cow)
    #
    # print(num)



    print("-----------------------------------")

    

    