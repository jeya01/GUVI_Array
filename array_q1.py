"""
You are given with an array. For each element present in the array your task is to print the next smallest than that number. If it is not smallest print -1

Input Description:
You are given a number ānā representing size of array. And n space separated numbers.

Output Description:
Print the next smallest number present in array and -1 if no smallest is present

Sample Input :
7
10 7 9 3 2 1 15
Sample Output :
7 3 3 2 1 -1 -1
"""

n = int(input()) # You are given a number ānā representing size of array
l = list(map(int,input().split()))

def printNSE(arr):
    for i in range(0,len(l)):
        next = -1
        for j in range(i+1, len(l)):
            if l[i] > l[j]:
                next = l[j]
                break;
        
        print(next , end = " ")
    

 

printNSE(l)
