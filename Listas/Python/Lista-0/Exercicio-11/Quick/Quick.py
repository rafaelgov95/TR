# -*- coding: UTF-8 -*-

def partition(list, start, end):
    pivot = list[end]
    bottom = start-1
    top = end

    done = 0
    while not done:

        while not done:
            bottom = bottom + 1

            if bottom == top:
                done = 1
                break

            if list[bottom] > pivot:
                list[top] = list[bottom]
                break

        while not done:
            top = top-1

            if top == bottom:
                done = 1
                break

            if list[top] < pivot:
                list[bottom] = list[top]
                break

    list[top] = pivot
    return top

def quicksort(list, start, end):
   if start < end:
        split = partition(list, start, end)
        quicksort(list, start, split-1)
        quicksort(list, split+1, end)
   else:
        return
