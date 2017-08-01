import sys
'''
Takes a raw_input of an int, and prints out the max number of consecutive
1's in the binary represenation of that number.
This short and simple function was a problem I did out of practice material,
but I thought was fun enough to hang onto.
Mostly I found it fun to cast an int into a bin into a string into a list.
There's probably a super pythonic way to turn that for loop into one line,
but maybe I'm not that much of an ace yet.
'''
n = int(raw_input().strip())
ans = 0
count = 0
n = list(str(bin(n)))
for i in n:
    if i == "1":
        count += 1
        if count > ans:
            ans = count
    else:
        count = 0
print ans