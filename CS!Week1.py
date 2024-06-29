#2
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)

#3
from itertools import groupby
S=input()

for k, i in groupby(S):
    print((list(i).count(k), int(k)), end=" ") 

#4
def minion_game(string):
    # your code goes here
    vowels="AEIOU"
    kevin_score=0
    stuart_score=0
    length=len(string)
    for i in range(length):
        if (string[i] in vowels):
            kevin_score+=length-i
        else:
            stuart_score+=length-i
    if kevin_score > stuart_score:
        print('Kevin', kevin_score)
    elif stuart_score > kevin_score:
        print('Stuart', stuart_score)
    else:
        print('Draw')           

if __name__ == '__main__':
    s = input()
    minion_game(s)
    
#5
def is_leap(year):
    leap = False
    if (((year % 4 == 0) & (year % 100 != 0)) | (year % 400 == 0)):
        leap = True
    return leap

year = int(input())
print(is_leap(year))

#7
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
N=int(input())
S = input().split()
K= int(input())
total=list(combinations(S, K))
print(len([x for x in total if 'a' in x])/ len(total))

#8
n=int(input())
t=tuple(map(int, input().split()))
print(hash(t))

#9

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
        
    query_name = input()
    marks=list(student_marks[query_name])
    
    number=sum(marks)/float(len(marks))
    print(f"{number:.2f}")
        

#0
def print_formatted(number):
    # your code goes here
    width = len(format(number,'b'))

    for i in range(1, number+1):
        print(f"{i:>{width}d} {i:>{width}o} {i:>{width}X} {i:>{width}b}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
