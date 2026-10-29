from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # value -> index
        for i, n in enumerate(nums):
            if target - n in seen:
                return [seen[target - n], i]
            seen[n] = i
        return []


def test_basic():
    s = Solution()
    assert sorted(s.twoSum([2, 7, 11, 15], 9)) == [0, 1]
    assert sorted(s.twoSum([3, 3], 6)) == [0, 1]
