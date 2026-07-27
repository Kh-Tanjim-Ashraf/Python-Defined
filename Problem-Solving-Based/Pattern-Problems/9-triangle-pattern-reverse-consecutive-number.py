"""

When n=3
1
21
321

When n=4
1
21
321
4321

================
Mental Breakdown
================
1. "n" number of iterations are required to cover the rows. i.e. Signifies how many lines are required to be printed.
2. Elements in each line will have iterations equivalent to the line number. i.e. Signifies how many elemented are required to be printed in each line.
    2.1# Line-1 will iterate once, Line-2 will iterate twice & so on.
3. In each line, each iteration (element-level) initiates with number 1 & prints the next consecutive number in reverse.

"""

n = int(input("Please enter the value of \"n\": "))

for i in range(0, n):

    for j in range(i+1, 0, -1):
        print(j, end="")

    print()