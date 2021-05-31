#this is a program to find smallest element in the list
lst = [7,4,52,63,23,2,6]
#assume that the firs element is smallest
smallest=lst[0]
#compare the elements consecutively ad replace whenever you find a smaller element
for num in lst:
    if num<smallest:
        smallest=num
print(smallest)


#this is a program to find the largest element in the list
number = [1,7,4,52,63,23,2,6]
#assume that the firs element is largest
largest = lst[0]
#compare the elements consecutively ad replace whenever you find a larger element
for element in number:
    if element>largest:
        largest = element
print(largest)


#these are the short way to find min and max element in a list
print(min(lst))
print(max(lst))


