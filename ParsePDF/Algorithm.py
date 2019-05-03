def bubblesort(list):

    for iter in range(len(list)-1,0,-1):
        for idx in range(iter):
            if list[idx] > list[idx+1]:
                temp = list[idx]
                list[idx] = list[idx+1]
                list[idx+1] = temp

def merge_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list

    middle = len(unsorted_list) // 2
    left_list = unsorted_list[:middle]
    right_list = unsorted_list[middle:]

    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)

    return list(merge(left_list, right_list))

def merge(left_half, right_half):
    res = []
    while len(left_half) != 0 and len(right_half) != 0:
        if left_half[0] < right_half[0]:
            res.append(left_half[0])
            left_half.remove(left_half[0])
        else:
            res.append(right_half[0])
            right_half.remove(right_half[0])
    if len(left_half) == 0:
        res = res + right_half
    else:
        res = res + left_half
    print("merge :") + str(res)
    return res

def QuickSort(unsorted_list):
    Split(unsorted_list, 0, len(unsorted_list)-1)

def Split(unsorted_list, first, last):
    if first < last:
        print "first : " + str(first)
        print "last : " + str(last)
        print "list : " + str(unsorted_list)
        split_point = partition(unsorted_list, first, last)
        print "split point : " + str(split_point)
        Split(unsorted_list, first, split_point-1)
        Split(unsorted_list, split_point+1, last)

def partition(unsorted_list, first, last):
    pivot_pointer = first
    left_pointer = first+1
    right_pointer = last
    stop = False

    while not stop:

        while left_pointer <= right_pointer and \
                        unsorted_list[left_pointer] <= unsorted_list[pivot_pointer]:
                left_pointer = left_pointer + 1
                print "left_pointer : " + str(left_pointer)

        while left_pointer <= right_pointer and \
                        unsorted_list[right_pointer] >= unsorted_list[pivot_pointer]:
                right_pointer = right_pointer - 1
                print "right_pointer : " + str(right_pointer)

        if left_pointer >= right_pointer:
            stop = True
        else:
            temp = unsorted_list[left_pointer]
            unsorted_list[left_pointer] = unsorted_list[right_pointer]
            unsorted_list[right_pointer] = temp

    temp = unsorted_list[pivot_pointer]
    unsorted_list[pivot_pointer] = unsorted_list[right_pointer]
    unsorted_list[right_pointer] = temp

    return right_pointer

unsorted_list = [64, 34, 25, 12, 22, 11, 90]
print QuickSort(unsorted_list)

def insertion_sort(InputList):
    for i in range(1, len(InputList)):
        j = i - 1
        nxt_element = InputList[i]
        # Compare the current element with next one

        while (InputList[j] > nxt_element) and (j >= 0):
            InputList[j + 1] = InputList[j]
            j = j - 1
        InputList[j + 1] = nxt_element
        print "J+1 : " + str(InputList[j + 1])
        print "next : " + str(nxt_element)



list = [19, 2, 31, 45, 30, 11, 121, 27]
insertion_sort(list)
print(list)