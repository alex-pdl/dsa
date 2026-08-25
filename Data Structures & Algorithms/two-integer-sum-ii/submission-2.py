class Solution:
    def twoSum(self, numbers: list, target: int) -> list:
        n = len(numbers)

        remainder = target
        i = 0
        j = n-1

        while True:
            if remainder == target:
                remainder -= numbers[i]
            if remainder - numbers[j] == 0:
                break
            #print("i:", i, "j:", j, "rem:", remainder)
            #print(f"{remainder} - {numbers[j]} == {remainder - numbers[j]}")

            if remainder > numbers[j]:
                j = n - 1
                i += 1
                remainder = target
                continue

            if remainder < numbers[j]:
                j -= 1
                continue

            if i == j:
                remainder = target
                i += 1
                j = n-1
                continue

            if i == n-1:
                break

        #print("i:", i, "j:", j, "rem:", remainder)
        #print(f"{remainder} - {numbers[j]} == {remainder - numbers[j]}")

        return [i+1, j+1]