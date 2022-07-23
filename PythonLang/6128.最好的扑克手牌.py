

from typing import List


class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        if suits.count(suits[0]) == 5:
            return "Flush"
        
        result = "High Card"
        for i in range(len(ranks)-1):
            if ranks.count(ranks[i]) >= 3:
                return "Three of a Kind"
            elif ranks.count(ranks[i]) == 2:
                result = "Pair"
        
        return result