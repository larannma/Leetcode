from operator import index

# def twoSum(nums: list[int], target: int) -> list[int]:
#         map = {}
#         for i, j in enumerate(nums):
#             diff = target - j
#             if diff in map:
#                 return([map[diff], i])
#             map[j] = i
#         return

# print(twoSum([2,7,11,15], 9))

def twoSum(nums: list[int], target: int) -> list[int]:
        answer = list()
        for i in range(len(nums)):
            for j in range(len(nums)):
                if (i != j) and (nums[i] + nums[j] == target):
                    answer.append(j)
                    answer.append(i)
                    break
            if (i != j) and (nums[i] + nums[j] == target):
                    break    
        return(answer)

    

print(twoSum(l, t))