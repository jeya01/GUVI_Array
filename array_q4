"""

You are given with an array of numbers, Your task is to print the difference of indices of largest and smallest number.All number are unique.

Input Description:
First line contains a number ‘n’. Then next line contains n space separated numbers.

Output Description:
Print the difference of indices of largest and smallest array

Sample Input :
5
1 6 4 0 3
Sample Output :
-2

"""

n = int(input())
a = list(map(int,input().split()))
l = len(a)
max_value=max(a)
min_value = min(a)
for i in range(0,n):
    if a[i] == max_value:
        small = i
    elif a[i] == min_value:
        large = i
diff=small-large
print(diff)
    
