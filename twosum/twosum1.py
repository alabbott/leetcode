class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index1 = 0

        for num1 in nums:
            index2 = 0
            for num2 in nums:
                if index1 == index2:
                    index2 += 1
                    continue
                if num1 + num2 == target:
                    return [index1, index2]

                index2 += 1
            index1 += 1
