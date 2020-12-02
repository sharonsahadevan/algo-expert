def isMonotonic(array):
    IsNonDecreasing = True
    IsNonIncreasing = True

    if len(array) == 0 or len(array) == 1:
        IsNonDecreasing = True
        IsNonIncreasing = True

    for i in range(len(array) - 1):
        if array[i] > array[i+1]:
            IsNonIncreasing = False
        elif array[i] < array[i+1]:
            IsNonDecreasing = False

    return IsNonIncreasing or IsNonDecreasing
