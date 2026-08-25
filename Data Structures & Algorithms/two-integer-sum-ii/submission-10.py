class Solution:
    def twoSum(self, numbers: list, target: int) -> list:
        i = 0
        j = len(numbers)-1

        while True:
            sums_to = numbers[j] + numbers[i]     
            if sums_to < target or i == j:
                j = len(numbers) - 1
                i += 1

            if sums_to > target:
                j -= 1
            
            if sums_to == target:
                break

        return [i+1, j+1]