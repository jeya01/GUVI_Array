"""

You are given an array. Your task is to sort the array in given manner. Print the elements in increasing order of the frequency. If frequency is same print smaller one first.

Input Description:
You are given a number ‘n’. Then in next line n space separated numbers.

Output Description:
Print the array as mentioned

Sample Input :
4
1 1 3 2
Sample Output :
2 3 1

"""


n = int(input())
lst = list(map(int,input().split()))

a = sorted(lst,key = lambda i:lst.index(i), reverse = True)
print(a)

ans = []
for i in a:
    if i not in ans:
        ans.append(i)
print(*ans)
