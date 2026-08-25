class Solution:
    def twoSum(self, numbers: list, target: int) -> list:
        n = len(numbers)
        i = 0
        j = n-1

        while True:            
            if numbers[i] + numbers[j] == target:
                break

            if target - numbers[i] > numbers[j] or i == j:
                j = n - 1
                i += 1
                continue

            if target - numbers[i] < numbers[j]:
                j -= 1
                continue

        return [i+1, j+1]