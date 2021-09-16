def ind(arr):
    max = 0
    for i in range(len(arr)):
        if arr[i] > max: max = i
    return max
array = [1,2,1,3,5,6,4]
print(ind(array))