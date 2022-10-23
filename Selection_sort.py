def selection_sort(array):
    n=len(array)##length of the array
    for ind in range(n):
        min_index=ind##setting the minimum index
        for j in range(ind+1,n):
            if array[j]<array[min_index]:
                min_index=j  #setting the new minimum 
        print(array)
        (array[ind],array[min_index])=(array[min_index],array[ind])##swapping elements
array=[56789,45634,12243,-123,-657,72738]
print(selection_sort(array))##printing sorted elements