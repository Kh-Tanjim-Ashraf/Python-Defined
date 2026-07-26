"""

When n=3
A
BB
CCC

When n=4
A
BB
CCC
DDDD

================
Mental Breakdown
================
1. "n" number of iterations are required to cover the rows. i.e. Signifies how many lines are required to be printed.
2. Elements in each line will have iterations equivalent to the line number. i.e. Signifies how many elemented are required to be printed in each line.
    2.1# Line-1 will iterate once, Line-2 will iterate twice & so on.
3. In each line, each iteration (element-level) will print the number of alpahbets. Starting from "A" in first line, the next line will initiate the next consecutive letter "B" & so on.

"""

n = int(input("Please enter the value of \"n\": "))
char = 65

for i in range(0, n):

    for j in range(0, i+1):
        print(chr(char), end="")

    char += 1

    print()