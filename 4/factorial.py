import sys
sys.setrecursionlimit(10**6)
def fac(n):
    if n == 0: 
        return 1
    else:
        #print(n)
        return n*fac(n-1)

number = int(input())
print(fac(number))
temp = list(str(fac(number)))
#flag = True
temp = temp[::-1]
count = 0
for i in range(len(temp)):
    #print(temp[i])
    if temp[i] == str(0): 
        count += 1 
    else: 
        break
print(count)