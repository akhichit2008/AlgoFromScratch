def Mergesort(array):
    n = len(array)
    if n == 1 or n == 0:
        return array
    arr1 = array[0:(n//2)]
    arr2 = array[(n//2):n]
    part_array1 = Mergesort(arr1)
    part_array2 = Mergesort(arr2)
    i = 0
    j = 0
    arr = []
    while i<len(part_array1) and j<len(part_array2):
        if part_array1[i] > part_array2[j]:
            arr.append(part_array2[j])
            j += 1
        elif part_array1[i] < part_array2[j]:
            arr.append(part_array1[i])
            i += 1
        else:
            arr.extend([part_array1[i],part_array2[j]])
            j += 1
            i += 1
    
    arr.extend(part_array1[i:])
    arr.extend(part_array2[j:])
    return arr

array = [8,5,2,0,4,4]

print(Mergesort(array))