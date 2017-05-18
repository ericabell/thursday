def sort_list(list1):
    """
    input: list1 consisting of integers
    output: list1 sorted from smallest to largest

    >>> sort_list([3,2,4,5,1])
    [1,2,3,4,5]
    """

    swapped = True
    while(swapped):
        swapped = False
        for i in range(len(list1)-1):
            if list1[i] > list1[i+1]:
                list1[i], list1[i+1] = list1[i+1], list1[i]
                swapped = True
    return list1




print( sort_list([3,2,4,5,1]) )
