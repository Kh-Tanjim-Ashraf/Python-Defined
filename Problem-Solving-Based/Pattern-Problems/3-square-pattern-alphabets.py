"""

When n=3
ABC
ABC
ABC

When n=4
ABCD
ABCD
ABCD
ABCD

"""

n = int(input("Please enter the value of \"n\": "))

for i in range(0, n):

    char = 65   # ASCII code 65 is represents "A"; Always starts the new row with "A", thus it auto-resets the "char" variable

    for j in range(0, n):
        print(chr(char), end="")
        char += 1

    print()