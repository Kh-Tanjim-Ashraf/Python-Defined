"""

When n=3
123
123
123

When n=4
1234
1234
1234
1234

================
Mental Breakdown
================
1. "n" number of iterations are required to cover the rows. i.e. Signifies how many lines are required to be printed.
2. "n" number of iterations are required to cover the columns of each row. i.e. Signifies how many elemented are required to be printed in each line.

"""


n = int(input("Please enter the value of \"n\": "))

for i in range(1, n+1):     # Outer Loop

    for j in range(1, n+1): # Inner Loop
        print(j, end="") 

    print()