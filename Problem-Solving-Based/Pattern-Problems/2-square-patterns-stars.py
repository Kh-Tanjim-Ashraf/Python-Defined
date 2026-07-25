"""

When n=3
***
***
***

When n=4
****
****
****
****

"""


n = int(input("Please enter the value of \"n\": "))

for i in range(0, n):

    for j in range(0, n):
        print("*", end="")

    print()