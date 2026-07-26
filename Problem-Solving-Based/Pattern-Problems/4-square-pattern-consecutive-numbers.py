"""

When n=3
123
456
789

When n=4
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16

================
Mental Breakdown
================
1. "n" number of iterations are required to cover the rows. i.e. Signifies how many lines are required to be printed.
2. "n" number of iterations are required to cover the columns of each row. i.e. Signifies how many elemented are required to be printed in each line.
3. Inside each row element, a consecutive number-series gets printed. So a number initiated from 1 will be incremented consecutively.

"""


n = int(input("Please enter the value of \"n\": "))
num = 1

for i in range(0, n):

    for j in range(0, n):
        print(num, end=" ")
        num += 1

    print()