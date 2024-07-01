#1
# Complete the solve function below.
def solve(s):
    s_1=""
    for i in range(len(s)):
        if i == 0:
            s_1 += s[i].upper()

        elif s[i - 1] == " ":
            s_1 += s[i].upper()
        else:
            s_1 += s[i]
    
    return s_1


#2
def average(array):
    # your code goes here
    setCollection = set()
    for x in array:
        setCollection.add(x)
        sum = 0
        i = 0
    for val in setCollection:
        sum = sum + val
        i = i + 1
        total = sum/i

    return total


#3
def wrap(string, max_width):
    result=""
    for i in range(len(string)):
        result+=string[i]
        if ((i+1) % max_width == 0):
            result+='\n'
    return result


#4
def print_rangoli(size):
    # your code goes here
    letters = [chr(a) for a in range(97, 97 + n)][::-1]
    
    # determine width of output 
    width = 4 * size - 3
    
    # initialise pattern
    pattern = []
    
    # output top and middle of pattern
    for i in range(size):
        pattern.append(letters[i])
        pattern_line = [*pattern, *pattern[::-1][1:]]
        print('-'.join(pattern_line).center(width, "-"))
      
    # output bottom of pattern
    for i in range(size - 1):
        pattern.pop()
        pattern_line = [*pattern, *pattern[::-1][1:]]
        print('-'.join(pattern_line).center(width, "-"))
    
    return


#5

def merge_the_tools(string, k):
    # your code goes here
    for t in range(0, len(string), k):
        u = set() 
        for i in range(t, t+k):
            if string[i] not in u:
                u.add(string[i])
                print(string[i], end="")
        print()
                
#6
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
n = int(input())
c = Counter(list(map(int, input().split())))
m = int(input())
total=0
for i in range(m):
    size, price = map(int, input().split())
    
    if (c[size] > 0):
        total += price
        
    if size in c:
        c[size] -= 1
print(total)
        
#7
# Enter your code here. Read input from STDIN. Print output to STDOUT
for i in range(int(input())):
    try:
        a, b = map(int, input().split())
        print(a//b)
    except ZeroDivisionError as e:
        print('Error Code:', e)
    except ValueError as e:
        print('Error Code:', e)

#8
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
T = int(input().strip())
for _ in range(T):
    try:
        S = input().strip()
        r = re.compile(S)
        print(True)
    except re.error:
        print(False)

#9
n = int(input())
s = set(map(int, input().split()))
N = int(input())

for i in range(N):
    i = input().split()
    if i[0] == 'pop':
        if s:
            s.pop()
    elif i[0] == 'remove':
        s.remove(int(i[1]))
    elif i[0] == 'discard':
        s.discard(int(i[1]))
        
print(sum(s))
