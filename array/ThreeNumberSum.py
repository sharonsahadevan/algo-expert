

def threeNumberSum(array, targetSum):
    triplet = []
    result = []
    array.sort()
    for i in range(len(array)):
        l = i + 1
        r = len(array) - 1
        while (l < r):
            current_sum = array[i] + array[l] + array[r]
            if current_sum == targetSum:
                triplet = array[i], array[l], array[r]
                result.append(triplet)
                l += 1
                r -= 1
                triplet = []
            elif current_sum < targetSum:
                l += 1
            else:
                r -= 1

    return result
