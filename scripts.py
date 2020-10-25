#Homework - 1

#PROBLEM 1

#INTRODUCTION

#1. Hello World
print("Hello, World!")

#2. Python If-Else
import math
import os
import random
import re
import sys
if __name__ == '__main__':
    n = int(input().strip())
if n//2 != n/2 :
    print ('Weird')
elif n<=5 :
    print ('Not Weird')
elif n<=20 :
    print ('Weird')
else:
    print ('Not Weird')

#3. Arithmetic Operators
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print (a+b)
    print (a-b)
    print (a*b)

#4. Python: Division
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print (a//b)
    print (a/b)

#5. Loops
if __name__ == '__main__':
    n = int(input())
    i = 0
    while i<n:
        print (i**2)
        i += 1

#6. Write a function
def is_leap(year):
    leap = False
    
    if year//4 == year/4 :
        leap = True
        if year//100 == year/100 :
            leap = False
            if year//400 == year/400: 
                leap = True
    
    return leap

year = int(input())
print(is_leap(year))

#7. Print function
if __name__ == '__main__':
    n = int(input())
    i = 1
    for i in range (1,n+1) :
        print (i, end = '')
        i += 1

#DATA TYPES

#1. List comprehensions
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    mylist = []
    i = 0
    j = 0 
    k = 0
    for i in range(x+1) :
        for j in range(y+1):
            for k in range(z+1):
                if i+j+k != n:
                    mylist.append([i,j,k])
    print(mylist)

#2. Find the runner up score!
if __name__ == '__main__':
    n = int(input()) #number of scores given
    arr = map(int, input().split()) #array of the scores
    #store the scores in a list
    mylist = list(arr)
    #then to find second place:
    #list in order
    ordlist = sorted(mylist)
    #find first place
    firstplace = max(ordlist)
    #remove first place
    ordlist.remove(firstplace)
    for i in range (n-1):
        if firstplace in ordlist:
            ordlist.remove(firstplace)
    #find second place and print it
    secondplace = max(ordlist)
    print(secondplace)

#3. Nested lists
records = []
scores = []
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        #create list of scores so you can sort cause no longer float
        records += [[name,score]]
        scores += [score]
    #select second lowest score
    score_sort = sorted(set(scores))[1]
    #names in alphabetical order and
    #find names of second lowest score
    for final_name,sec_score in sorted(records):
        if sec_score==score_sort:
            print(final_name)

#4. Finding the percentage
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
grades_query = student_marks[query_name]
query = sum(grades_query)/len(grades_query)
twodec_query = "{:.2f}".format(query)
print(twodec_query)

#5. Lists
all_commands = []
mylist = []
if __name__ == '__main__':
    N = int(input())
    for i in range(N):
        commands = input().split(" ")
        all_commands.append(commands)
    flat_comm = [t for sublist in all_commands for t in sublist]
    l = len(flat_comm)
    for i in range(l):
        comm = flat_comm[i]
        if comm=="insert":
            a = int(flat_comm[i+1])
            b = int(flat_comm[i+2])
            mylist.insert(a,b)
            i += 2
        if comm=="print":
            print(mylist)
        if comm=="remove":
            c = int(flat_comm[i+1])
            mylist.remove(c)
            i += 1
        if comm=="append":
            d = int(flat_comm[i+1])
            mylist.append(d)
            i += 1
        if comm=="sort":
            mylist.sort()
        if comm=="pop":
            mylist.pop()
        if comm=="reverse":
            mylist.reverse()
        i += 1

#6. Tuples
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(integer_list)
    print(hash(t))

#STRINGS

#1. Swap case
def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

#2. String split and join
def split_and_join(line):
    newlist = line.split(" ")
    finallist = "-".join(newlist)
    return finallist

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

#3. What's your name?
def print_full_name(a, b):
    print("Hello "+a+" "+b+"! You just delved into python.")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)

#4. Mutations
def mutate_string(string, position, character):
    mylist = list(string)
    mylist[position]=character
    string=''.join(mylist)
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

#5. Find a string
def count_substring(string, sub_string):
    count=0
    check=""
    lstring=len(string)
    lsub=len(sub_string)
    for i in range(lstring-lsub+1):
        for j in range(lsub):
            x = i+j
            check+=str(string[x])
            if check==sub_string:
                count+=1
        check=""
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

#6. String validators
if __name__ == '__main__':
    s = input()
s = list(s)
x = len(s)
check0=0
check1=0
check2=0
check3=0
check4=0
af=0
bf=0
cf=0
df=0
ef=0
for i in range(x):
    check = str(s[i])
    a = str(check.isalnum())
    b = str(check.isalpha())
    c = str(check.isdigit())
    d = str(check.islower())
    e = str(check.isupper())
    if a=="True":
        if check0 == 0:
            af+=1
        check0 += 1
    if b=="True":
        if check1==0:
            bf+=1
        check1 += 1
    if c=="True":
        if check2==0:
            cf+=1
        check2 += 1
    if d=="True":
        if check3==0:
            df+=1
        check3 += 1
    if e=="True":
        if check4==0:
            ef+=1
        check4 += 1
if af==1:
    print("True")
elif af==0:
    print("False")
if bf==1:
    print("True")
elif bf==0:
    print("False")
if cf==1:
    print("True")
elif cf==0:
    print("False")
if df==1:
    print("True")
elif df==0:
    print("False")
if ef==1:
    print("True")
elif ef==0:
    print("False")

#7. Text alignment
#Replace all ______ with rjust, ljust or center. 
thickness = int(input()) #This must be an odd number
c = 'H'
#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))
#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    
#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    
#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

#8. Text wrap
import textwrap
def wrap(string, max_width):
    m = max_width
    x = 0
    mystring = list(string)
    for i in range(len(string)):
        x = i+m
        if x//m==x/m:
            riga = list(mystring[i:i+max_width])
            if len(riga)==m:
                print(''.join(riga))
    return ''.join(riga)
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

#9. Designer doormat
N,M=map(int,input().split())
i=1
p=".|."
size=3
space=(M-3)//2
left_space=space
cols = (N-1)//2
#top part
for x in range(cols):
    if left_space >= size:
        print((p*i).center(M,"-"))
        i+=2
        left_space-=3
#middle
print("WELCOME".center(M,"-"))
#bottom part
i-=2
left_space+=3
for x in range(cols):
    if left_space <= space:
        print((p*i).center(M,"-"))
        i-=2
        left_space+=3

#10. String Formatting
def print_formatted(number):
    maxl=len("{0:b}".format(number))
    for n in range(1,number+1):
        numbers=("{0:{l}d} {0:{l}o} {0:{l}X} {0:{l}b}".format(n,l=maxl))
        print(numbers)
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

#11. Alphabet rangoli
def print_rangoli(size):
    alphabet=[chr(i) for i in range(ord('a'),ord('z')+1)]
    diameter=(size*2)-1
    dashes=diameter-1
    diameter+=dashes
    dashes=(diameter-1)//2
    x=size
    #top part
    for j in range(size):
        x-=1
        #left dashes
        for k in range(dashes):
            print("-",end="")
        #left part
        if j>0:
            for m in range(j):
                print(alphabet[size-m-1],end="-")
        #middle
        print(alphabet[size-j-1], end="")
        #right part
        if j>0:
            for a in range(j):
                b=j-a
                print("-",end="")
                print(alphabet[size-b],end="")
        #right dashes
        for l in range(dashes-1):
            print("-",end="")
        if j!=(size-1):
            print("-",end="")
        #next line
        print("")
        dashes-=2
    #bottom part
    dash=2
    odash=dashes-dash+4
    for lett in range(1,size):
        #left dashes
        for d in range(dash):
            print("",end="-")
        #left part
        letter=size-lett
        p=lett
        for l in range(letter):
            p-=1
            print(alphabet[letter+p],end="-")
        #right part
        p=lett
        for v in range(letter-1):
            p=letter-v
            print(alphabet[size-p+1],end="-")
        #right dashes
        print("-",end="")
        if odash!=0:
            for o in range(odash):
                print("-",end="")
        odash+=2
        dash+=2
        #next line
        print("")     
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

#12. Capitalize!
def solve(s):
    namesur=s.split(" ")
    l=len(namesur)
    sol=[]
    for i in range(l):
        name=namesur[i]
        capname=name.capitalize()
        if capname!=name:
            name=capname
        sol.append(name)
    separator=" "
    passport=separator.join(sol)
    return passport
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = solve(s)
    fptr.write(result + '\n')
    fptr.close()

#13. The minion game
def minion_game(string):
    #initial set up
    l=len(string)
    letters=list(string)
    vowels='AEIOU'
    consonants='BCDFGHJKLMNPQRSTVWXYZ'
    ps=0
    pk=0
    #count points
    #i had to check the editorial for this
    #what confused me was the possibility of a word being different than the simple alternating of vowel 
    # and consonant like what would happen for a word like "what"
    for i in range(l):
        if letters[i] in vowels:
            pk+=(l-i)
        else:
            ps+=(l-i)
    #compare scores
    if ps>pk:
        print("Stuart",end=" ")
        print(ps)
    elif pk>ps:
        print("Kevin",end=" ")
        print(pk)
    else:
        print("Draw")
if __name__ == '__main__':
    s = input()
    minion_game(s)

#14. Merge the tools
def merge_the_tools(s, k):
    n=len(s)
    #create a list t of nt substrings of equal length k
    t=[]
    for i in range(0,n,k):
        t.append(s[i:i+k])
    #create list u of subsequences with each character only once
    u=[]
    for substring in t:
        sub=substring
        for j in range(k):
            l=len(sub)
            if j<l:
                y=sub[j]
                c=sub.count(y)
                while c>1:
                    where=sub.rfind(y)
                    tlist=list(sub)
                    tlist.pop(where)
                    sub=''.join(tlist)
                    c=sub.count(y)
        print(sub)                
    return s
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

#SETS

#1. Introduction to sets
def average(array):
    N=len(set(array))
    tot=sum(set(array))
    u=tot/N
    return u
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

#2. No idea!
numbers=list(map(int,input().split()))
#number of integers in array
n=numbers[0]
#number of integers in each set
m=numbers[1]
#the integers in the array
elarray=list(map(int,input().split()))
#the disjoint sets
a=set(map(int,input().split()))
b=set(map(int,input().split()))
h=0
for i in elarray:
    if i in a:
        h+=1
    elif i in b:
        h-=1
print(h)

#3. Symmetric difference
M=int(input())
mint=set(map(int,input().split()))
N=int(input())
nint=set(map(int,input().split()))
mint.symmetric_difference_update(nint)
mint=sorted(mint)
for i in mint:
    print(i)

#4. Set .add()
N=int(input())
stamps=set()
for i in range(N):
    country=str(input())
    stamps.add(country)
print(len(stamps))

#5. Set .discard(), .remove() & .pop()
n = int(input())
s = set(map(int, input().split()))
ncomm = int(input())
noerror=[]
for i in range(ncomm):
    commands = input().split()
    check=bool(s)
    if check==True:
        if commands[0]=='pop':
            s.pop()
        if commands[0]=='remove':
            x=commands[1]
            x=int(x)
            if x in noerror:
                x=x
            else:
                s.remove(x)
                noerror.append(x)
        if commands[0]=='discard':
            x=commands[1]
            x=int(x)
            if x in noerror:
                x=x
            else:
                s.discard(x)
                noerror.append(x)
solution=list(s)
tsum=0
for i in range(len(solution)):
    num=int(solution[i])
    tsum+=num
print(tsum)

#6. Set .union() operation
#english newspaper
n=int(input())
rolln=list(input().split())
#french newspaper
b=int(input())
rollb=list(input().split())
#students who have at list one subscription
eng=set(rolln)
fre=set(rollb)
students=eng.union(fre)
#total n of students
sol=len(students)
print(sol)

#7. Set .intersection() operation
#english newspaper
n=int(input())
rolln=list(input().split())
#french newspaper
b=int(input())
rollb=list(input().split())
#both newspapers
eng=set(rolln)
fre=set(rollb)
both=eng.intersection(fre)
sol=len(both)
print(sol)

#8. Set .difference() operation
#english newspaper
n=int(input())
rolln=list(input().split())
#french newspaper
b=int(input())
rollb=list(input().split())
#students who only have eng
students=set(rolln)
rollb=set(rollb)
students.difference_update(rollb)
sol=len(students)
print(sol)

#9. Set .symmetric_difference() operation
#eng
n=int(input())
rolln=set(list(input().split()))
#fre
b=int(input())
rollb=set(list(input().split()))
#students who only have one subscription
students=rolln
students.symmetric_difference_update(rollb)
sol=len(students)
print(sol)

#10. Set mutations
na=int(input())
a=set(list(input().split()))
ns=int(input())
for i in range(ns):
    #the amount of other sets there are
    instructions=list(input().split())
    opname=instructions[0]
    nelements=int(instructions[1])
    otherset=list(input().split())
    otherset=set(otherset)
    if opname=="update":
        a.update(otherset)
    if opname=="intersection_update":
        a.intersection_update(otherset)
    if opname=="difference_update":
        a.difference_update(otherset)
    if opname=="symmetric_difference_update":
        a.symmetric_difference_update(otherset)
tot=0
l=len(a)
a=list(a)
for j in range(l):
    tot+=int(a[j])
print(tot)

#11. The captain's room
#size of each family
k=int(input())
roomlist=list(input().split())
totalrooms=set()
familyroom=set()
for i in roomlist:
    if i in totalrooms:
        familyroom.add(i)
    else:
        totalrooms.add(i)
caproom=totalrooms.difference(familyroom)
sol=list(caproom)
sol=sol[0]
print(sol)

#12. Check subset
t=int(input())
for i in range(t):
    nela=int(input())
    a=set(list(input().split()))
    nelb=int(input())
    b=set(list(input().split()))
    print(a.issubset(b))

#13. Check strict superset
a=set(input().split())
n=int(input())
count=0
for i in range(n):
    otherset=set(input().split())
    if a.issuperset(otherset):
        count+=1
print(count==n)

#COLLECTIONS

#1. Collections.counter()
#ragù
from collections import Counter
x=int(input())
shoesizes=list(map(int,input().split()))
inventory=list(Counter(shoesizes).keys())
available=list(Counter(shoesizes).values())
n=int(input())
money=0
for i in range(n):
    customer=list(input().split())
    desiredsize=int(customer[0])
    price=int(customer[1])
    if desiredsize in inventory:
        where=inventory.index(desiredsize)
        avw=int(available[where])
        if avw>0:
            avw-=1
            available.insert(where,avw)
            available.pop(where+1)
            money+=price
print(money)

#2. DefaultDict tutorial
from collections import defaultdict
n,m=map(int,input().split())
a=[]
b=[]
d=defaultdict(list)
for i in range(n):
    word=input()
    a.append(word)
    d['a'].append(word)
for j in range(m):
    word=input()
    b.append(word)
    d['b'].append(word)
for w in d['b']:
    if w in d['a']:
        for k in range(len(a)):
            if a[k]==w:
                k+=1
                print(k, end=" ")
            else:
                k+=1
    else:
        print(-1, end=" ")
    print()

#3. Collections.namedTuple()
from collections import namedtuple
n=int(input())
namecols=list(input().split())
ss=namedtuple('ss', namecols)
totmarks=0
for i in range(n):
    a,b,c,d=input().split()
    si=ss(a,b,c,d)
    totmarks+=int(si.MARKS)

print(totmarks/n)

#4. Collections.orderedDict()
from collections import OrderedDict
od=OrderedDict()
n=int(input())
for i in range(n):
    item=(input().split())
    item_name=' '.join(item[:-1])
    net_price=int(item[-1])
    if item_name in od:
        od[item_name]+=net_price
    else:
        od[item_name]=net_price
for a,b in od.items():
    print(a,b)
    
#5. Word order
from collections import OrderedDict
od=OrderedDict()
for i in range(int(input())):
    word=input().split()
    word=str(word)
    if word in od:
        od[word]+=1
    else:
        od[word]=1
count=0
for a in od.items():
    count+=1
print(count)
for b,c in od.items():
    print(c,end=" ")

#6. Collections.deque()
from collections import deque
d=deque()
for i in range(int(input())):
    mv=input().split()
    command=str(mv[0])
    if len(mv)>1:
        value=int(mv[1])
    if command=="append":
        d.append(value)
    if command=="pop":
        d.pop()
    if command=="popleft":
        d.popleft()
    if command=="appendleft":
        d.appendleft(value)
for j in range(len(d)):
    print(d[j],end=" ")

#7. Company logo
import math
import os
import random
import re
import sys
if __name__ == '__main__':
    s = sorted(input())
from collections import Counter
count=Counter(s).most_common(3)
for i,j in count:
    print(i,j)

#8. Piling up!
from collections import deque
t=int(input())
for i in range(t):
    d=deque()
    ncubes=int(input())
    sideLengths=input().split()
    for j in range(ncubes):
        d.append(int(sideLengths[j]))
    #now we have the first line
    l=2**31
    stack=0
    for j in range(ncubes):
        #so for all the cubes
        #we check if the leftmost is bigger than the rightmost
        if d[0]>=d[len(d)-1]:
            if d[0]<=l:
                stack+=1
                l=d[0]
                d.popleft()
        elif d[len(d)-1]>=d[0]:
            if d[len(d)-1]<=l:
                stack+=1
                l=d[len(d)-1]
                d.pop()
    if stack==ncubes:
        print("Yes")
    else:
        print("No")

#DATE AND TIME

#1. Calendar module
import calendar
l=input().split()
m=int(l[0])
d=int(l[1])
y=int(l[2])
day=calendar.weekday(y,m,d)
wdname=calendar.day_name[day]
print(wdname.upper())

#2. Time delta
import math
import os
import random
import re
import sys
from datetime import datetime
def time_delta(t1, t2):
    timeformat="%a %d %b %Y %H:%M:%S %z"
    t1=datetime.strptime(t1,timeformat)
    t2=datetime.strptime(t2,timeformat)
    diff=int(abs(t1-t2).total_seconds())
    diff=str(diff)
    return diff
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())
    for t_itr in range(t):
        t1 = input()
        t2 = input()
        delta = time_delta(t1, t2)
        fptr.write(delta + '\n')
    fptr.close()

#EXCEPTIONS

#1. Exceptions
t=int(input())
for i in range(t):
    n=input().split()
    a=(n[0])
    b=(n[1])
    try:
        print (int(int(a)//int(b)))
    except Exception as e:
        print ("Error Code:",e)

#BUILT-INS

#1. Zipped!
n,x=map(int,input().split())
studmarks=list()
for i in range(x):
    subjmarks=list(map(float,input().split()))
    studmarks.append(subjmarks)
marks=zip(*studmarks)
for j in marks:
    m=sum(j)/len(j)
    print(m)

#2. Athlete sort
import math
import os
import random
import re
import sys
if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    k = int(input())
arr=sorted(arr,key=lambda arr:arr[k])
for i in arr:
    print(*i)

#3. Ginorts
s=str(input())
slist=[]
for i in range(len(s)):
    slist.append(s[i])
slist=sorted(slist)
s=''.join(slist)
su=str(s.upper())
sl=str(s.lower())
se='02468'
so='13579'
d='0123456789'
l=[]
for i in range(len(s)):
    if s[i] == sl[i] and s[i] not in d:
        l.append(s[i])
for i in range(len(s)):
    if s[i]==su[i] and s[i] not in d:
        l.append(s[i])
for i in range(len(s)):
    if s[i] in so:
        l.append(s[i])
for i in range(len(s)):
    if s[i] in se:
        l.append(s[i])
sol=''.join(l)
print(sol)

#PYTHON FUNCTIONALS

#1. Map and lambda functions
cube = lambda x: x**3
def fibonacci(n):
    a=0
    b=1
    f=[]
    for i in range(n):
        if i<2:
            f+=[i]
        else:
            f+=[f[-1]+f[-2]]
    return f[0:n]
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))

#REGEX AND PARSING CHALLENGES

#1. Detect floating point number
import re
t=int(input())
for i in range(t):
    n=str(input())
    if re.match(r"^[+-]?\d*\.\d+$",n):
        print("True")
    else:
        print("False")

#2. Re.split()
regex_pattern = r"[,.]"	

import re
print("\n".join(re.split(regex_pattern, input())))

#3. Group(), Groups() & Groupdict()
import re
s=input()
x=re.search(r'([A-Za-z0-9])\1+',s)
if x:
    print(x.group(1))
else:
    print(-1)

#4. Re.findall() & Re.finditer()
import re
s=input()
vow='aeiou'
cons='bcdfghjklmnpqrstvwxyz'
x='(?<=['+cons+'])(['+vow+']{2,})['+cons+']'
m=re.findall(x,s,re.I)
if m:
    for i in m:
        print(i)
else:
    print(-1)

#5. Re.start() & re.end()
import re
s=input()
k=input()
x=re.search(k, s)
i=0
if x:
    while i+len(k)<len(s):
        y=re.search(k,s[i:])
        print('({0}, {1})'.format(i+y.start(), i+y.end()-1))
        i+=y.start()+1
else:
    print((-1,-1))

#6. Regex substitution
import re
n=int(input())
for _ in range(n):
    t=input()
    while ' && ' in t or ' || ' in t:
        t=t.replace(" && ", " and ").replace(" || ", " or ")
    print(t)

#7. Validating roman numerals
regex_pattern = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"
import re
print(str(bool(re.match(regex_pattern, input()))))

#8. Validating phone numbers
import re
n=int(input())
for _ in range(n):
    s=str(input())
    if len(s)==10:
        match=re.search(r'^[789]',s)
        if match:
            if s.isdecimal():
                print("YES")
            else:
                print("NO")
        else:
            print("NO")
    else:
        print("NO")

#9. Validating and parsing email addresses
import re
n=int(input())
for i in range(n):
    name,email=input().split()
    match=re.findall(r'<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>',email)
    if match:
        print(name,email)

#10. Hex color code
import re
for _ in range(int(input())):
    code=input()
    match=re.findall(r'[\s:](#[A-Fa-f0-9]{6}|#[A-Fa-f0-9]{3})',code)
    if match:
        print(*match,sep='\n')

#11. HTML parser - part 1
from html.parser import HTMLParser
class myhtmlparser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :",tag)
        for a in attrs:
            print("->"," > ".join(map(str,a)))
    def handle_endtag(self, tag):
        print("End   :",tag)
    def handle_startendtag(self, tag, attrs):
        print("Empty :",tag)
        for a in attrs:
            print("->"," > ".join(map(str,a)))
html=''
for _ in range(int(input())):
    html+=input()
p=myhtmlparser()
p.feed(html)
p.close()

#12. HTML parser - part 2
from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if data!="\n":
            if "\n" not in data:
                print(">>> Single-line Comment")
                print(data)
            else:
                print(">>> Multi-line Comment")
                print(data)
    def handle_data(self, data):
        if data!="\n":
            print(">>> Data")
            print(data)  
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
parser = MyHTMLParser()
parser.feed(html)
parser.close()

#13. Detect HTML Tags, Attributes and Attribute Values
from html.parser import HTMLParser
class myhtmlparser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for a in attrs:
            print("->"," > ".join(map(str,a)))
html=''
for _ in range(int(input())):
    html+=input()
p=myhtmlparser()
p.feed(html)
p.close()

#14. Validating UID
import re
for _ in range(int(input())):
    t=input()
    if len(t)==10:
        match=re.findall(r'^(?!.*([A-Za-z0-9]).*\1)(?=(?:.*[A-Z]){2,})(?=(?:.*[0-9]){3,})',t)
        if match:
            print("Valid")
        else:
            print("Invalid")
    else:
        print("Invalid")

#15. Validating Credit Card Numbers
import re
for _ in range(int(input())):
    l=input()
    match1=re.findall(r'[456][0-9]{3}(-?[0-9]{4}){3}$',l)
    match2=re.findall(r'(([0-9])-?(?!(-?\2){3})){16}',l)
    if match1 and match2:
        print("Valid")
    else:
        print("Invalid")

#16. Validating Postal Codes
regex_integer_in_range = r"^[1-9][0-9]{5}$"	
regex_alternating_repetitive_digit_pair = r"([0-9])(?=.\1)"	
import re
P = input()
print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)

#17. Matrix script
import math
import os
import random
import re
import sys
first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
matrix = []
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
matrix=list(zip(*matrix))
t=""
for i in matrix:
    t=t+"".join(i)
t=re.sub(r'\b[^A-Za-z0-9]+\b',r' ',t)
print(t)

#XML

#1. Find the score
import sys
import xml.etree.ElementTree as etree
def get_attr_number(node):
    l=len(node.attrib)
    s=sum((get_attr_number(feed) for feed in node))
    l+=s
    return l
if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))

#2. Find the maximum depth
import xml.etree.ElementTree as etree
maxdepth = 0
def depth(elem, level):
    global maxdepth
    if level==maxdepth:
        maxdepth+=1
    for i in elem:
        depth(i,level+1)    
if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)

#CLOSURES AND DECORATIONS

#1. Standardize Mobile Number Using Decorators
def wrapper(f):
    def fun(l):
        for i in range(len(l)):
            length=len(l[i])
            l[i]=int(l[i])
            if length>11:
                l[i]=l[i]-910000000000
            l[i]=str(l[i])
            l[i]=list(l[i])
            l[i].insert(0,'+91')
            l[i]=''.join(l[i])
        l=sorted(l)
        for j in range(len(l)):
            x=l[j]
            print(x[0:3],end=" ")
            print(x[3:8],end=" ")
            print(x[8:])
    return fun
@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')
if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 

#2. Decorators 2 - name directory
import operator
from operator import itemgetter
def person_lister(f):
    def inner(people):
        for i in people:
            i[2]=int(i[2])
        people.sort(key=itemgetter(2))
        x=map(f,people)
        return x
    return inner
@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]
if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')

#NUMPY

#1. Arrays
import numpy
def arrays(arr):
    arr.reverse()
    arr=numpy.array(arr,float)
    return arr
arr = input().strip().split(' ')
result = arrays(arr)
print(result)

#2. Shape and reshape
import numpy
l=numpy.array(input().split(),int)
l.shape=(3,3)
print(l)

#3. Transpose and flatten
import numpy
n,m=input().split()
n=int(n)
m=int(m)
x=numpy.empty((n,m),int)
for i in range(n):
    y=input().split()
    for j in range(m):
        x[i][j]=y[j]
print(x.transpose())
print(x.flatten())

#4. Concatenate
import numpy
n,m,p=map(int,input().split())
#got the next two lines from discussion, as i couldn't make them work on my own
a=numpy.array([input().split() for _ in range(n)],int)
b=numpy.array([input().split() for _ in range(m)],int)
print(numpy.concatenate((a,b),axis=0))

#5. Zeros and ones
import numpy
l=list(map(int,input().split()))
print(numpy.zeros((l),dtype=numpy.int))
print(numpy.ones((l),dtype=numpy.int))

#6. Eye and identity
import numpy
n,m=input().split()
n=int(n)
m=int(m)
numpy.set_printoptions(sign=' ')
print(numpy.eye(n,m,k=0))

#7. Array mathematics
import numpy
n,m=map(int,input().split())
a=numpy.array([input().split() for _ in range(n)],int)
b=numpy.array([input().split() for _ in range(n)],int)
#a+b
print(numpy.add(a,b))
#a-b
print(numpy.subtract(a,b))
#a*b
print(numpy.multiply(a,b))
#a/b
print(numpy.floor_divide(a,b))
#a%b
print(numpy.mod(a,b))
#a**b
print(numpy.power(a,b))

#8. Floor ceil and rint
import numpy
a=numpy.array(list(map(float,input().split())))
numpy.set_printoptions(sign=' ')
print(numpy.floor(a))
print(numpy.ceil(a))
print(numpy.rint(a))

#9. Sum and prod
import numpy
n,m=map(int,input().split())
a=numpy.array([input().split() for _ in range(n)],int)
s=numpy.sum(a,axis=0)
print(numpy.prod(s))

#10. Min and max
import numpy
n,m=map(int,input().split())
a=numpy.array([input().split() for _ in range(n)],int)
b=numpy.min(a,axis=1)
print(numpy.max(b))

#11. Mean var and std
import numpy
n,m=map(int,input().split())
a=numpy.array([input().split() for _ in range(n)],int)
numpy.set_printoptions(legacy='1.13')
#mean axis 1
print(numpy.mean(a,axis=1))
#var axis 0
print(numpy.var(a,axis=0))
#std axis none
print(numpy.std(a))

#12. Dot and cross
import numpy
n=int(input())
a=numpy.array([input().split() for _ in range(n)],int)
b=numpy.array([input().split() for _ in range(n)],int)
print(numpy.dot(a,b))

#13. Inner and outer
import numpy
a=numpy.array([input().split()],int)
b=numpy.array([input().split()],int)
print(int(numpy.inner(a,b)))
print(numpy.outer(a,b))

#14. Polynomials
import numpy
p=list(map(float,input().split()))
x=int(input())
print(numpy.polyval(p,x))

#15. Linear algebra
import numpy
n=int(input())
a=numpy.array([input().split() for _ in range(n)],float)
print(round(numpy.linalg.det(a),2))

#PROBLEM 2

#Birthday cake candles
import math
import os
import random
import re
import sys
#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#
def birthdayCakeCandles(candles):
    m=max(candles)
    count=0
    for i in candles:
        if i==m:
            count+=1
    return(count)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    candles_count = int(input().strip())
    candles = list(map(int, input().rstrip().split()))
    result = birthdayCakeCandles(candles)
    fptr.write(str(result) + '\n')
    fptr.close()

#2. Kangaroo
import math
import os
import random
import re
import sys
# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    check=0
    pos1=x1+v1
    pos2=x2+v2
    for _ in range(10000):
        if pos1==pos2:
            check=1
        pos1=pos1+v1
        pos2=pos2+v2
    if check==1:
        result="YES"
    else:
        result="NO"
    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    x1V1X2V2 = input().split()
    x1 = int(x1V1X2V2[0])
    v1 = int(x1V1X2V2[1])
    x2 = int(x1V1X2V2[2])
    v2 = int(x1V1X2V2[3])
    result = kangaroo(x1, v1, x2, v2)
    fptr.write(result + '\n')
    fptr.close()

#3. Viral advertising
import math
import os
import random
import re
import sys
# Complete the viralAdvertising function below.
def viralAdvertising(n):
    shared=5
    liked=shared//2
    totlikes=liked
    for i in range(1,n):
        shared=liked*3
        liked=shared//2
        totlikes+=liked
    return(totlikes)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    result = viralAdvertising(n)
    fptr.write(str(result) + '\n')
    fptr.close()

#4. Recursive digit sum
import math
import os
import random
import re
import sys
# Complete the superDigit function below.
def superDigit(n, k):
    n=str(n)
    while len(n)>1:
        count=0
        for i in range(len(n)):
            count+=int(n[i])
        n=str(count)
    p=n*k
    while len(p)>1:
        count=0
        for i in range(len(p)):
            count+=int(p[i])
        p=str(count)
    return count  
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nk = input().split()
    n = nk[0]
    k = int(nk[1])
    result = superDigit(n, k)
    fptr.write(str(result) + '\n')
    fptr.close()

#5. Insertion sort 1
import math
import os
import random
import re
import sys
# Complete the insertionSort1 function below.
def insertionSort1(n, arr):
    s=[]
    arr2=[]
    for x in arr:
        s.append(x)
        arr2.append(x)
    for i in range(n,0,-1):
        m=max(s)
        pos=i-1
        arr[pos]=m
        s.remove(m)
        if arr!=arr2:
            arr2=[]
            for k in arr:
                print(k,end=" ")
                arr2.append(k)
        print()
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    insertionSort1(n, arr)

#6. Insertion sort 2
import math
import os
import random
import re
import sys
# Complete the insertionSort2 function below.
def insertionSort2(n, arr):
    for i in range(1,n):
        k=arr[i]
        j=i-1
        while j>=0 and arr[j]>k:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=k
        for a in arr:
            print(a,end=" ")
        print()
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    insertionSort2(n, arr)