import random
list1 = [5,13,31,73,53,17,83,23,79,11,61,19,41,2,89,71,3,97,43,7,29,47,37,59,67]
#Sort the list using Insertion Sorting Algorithm
def InsertionSort(list):
    for i in range(1,len(list)):
        current = list[i]
        k = i - 1      #we look at the sorted sublist and compare
        while k>=0 and list[k] > current:
            list[k+1]=list[k]       #k+1=i which is the current will compare it with k-1th element
            k-=1
            #print(list)  #to see the progress
        list[k+1]=current #if the current element is greater than its predecessors
    return list


# Search for the element
def BinarySearch(key):
    print("We are searching for the index of the number",key)
    list2=InsertionSort(list1) #Sort the list using the insertion algorithm
    minIndex = 0
    maxIndex = len(list2)-1

    found = -1             #If value is not found it will display -1

    while minIndex<=maxIndex and found==-1:
        midVal = (maxIndex+minIndex)//2
        if midVal < list2.index(key):
            minIndex = minIndex+1
        elif midVal > list2.index(key):
            maxIndex = maxIndex - 1
        elif midVal == list2.index(key):
            found = midVal

    if found>=3 and found>=23:
        print("the number is the",found+1,"th element of the list")
    elif found==0 or found==20:
        print("The number is the",found+1,"st element in the list")
    elif found==1 or found==21:
        print("The number is the",found+1,"nd element in the list")
    elif found==2 or found==22:
        print("The number is the",found+1,"rd element in the list")

key2 =input("Please enter an integer to search for: ")
try:
    key3=int(key2)
    if key3 in list1:
        BinarySearch(key3)
    else:
        print("The number that you are looking for is not in the list")
except ValueError:
    print(key2,"is not an integer")
    exit()
