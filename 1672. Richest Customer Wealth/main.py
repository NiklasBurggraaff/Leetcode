from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth = [sum(customerAccounts) for customerAccounts in accounts]
        return max(wealth)
