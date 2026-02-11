# import array as arr
# class twoSum:
#     at = arr.array(int,[2,33,54,64,98])
#     gl = "hello"
#     def twoSumSorted(ay):
#         # for s in range(ay):
#         print(ay[0])
#         # print(gl)

#     twoSumSorted(ay = arr.array(int, [2,33,54,64,98]))
class Solution:
    def twoSum(numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            currentSum = numbers[left] + numbers[right]
            
            if currentSum == target:
                # Return 1-indexed positions
                print(left, right)
                return [left + 1, right + 1]
            elif currentSum < target:
                left += 1
            else:
                right -= 1
        
        # As per problem constraints, a solution always exists
        print("value not matched")
        return []
    twoSum(numbers = [2,17,11,7,15], target = 19)
