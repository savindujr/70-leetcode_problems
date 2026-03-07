#1st Method - 

def twoSum_bruteForce(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []  

# 2nd Method - using hashmaps

def twoSum_optimal(nums, target):
    num_map = {}  # value -> index
    
    for i, num in enumerate(nums):
        complement = target - num
        
        if complement in num_map:
            return [num_map[complement], i]
        
        num_map[num] = i
    
    return []  # No solution found

nums = [7,11,5,2]
target = 9

print(twoSum_bruteForce(nums,target))
print(twoSum_optimal(nums,target))