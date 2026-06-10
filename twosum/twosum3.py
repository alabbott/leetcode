class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        index = 0
        for num in nums:
            if num in hash_map.keys():
                return [index, hash_map[num]]
            complement = target - num
            hash_map[complement] = index
            index += 1
        
        return []
