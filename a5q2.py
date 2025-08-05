# Christopher Lee
# ID: 10136117

# Allows user input lists, then turns it into a list of string numbers
getString = input("Please enter a list of numbers separated by spaces:")
stringList = getString.split()
# These variables are for turning the string list into an integer list
# They need to be global otherwise the counter gets lost during recursions
intList = []
x = 0


# This function turns the given string list into integers
def intifyList(intableList):
    global x
    if x == len(intableList):
        return
    else:
        intList.append(int(intableList[x]))
        x += 1
        intifyList(intableList)


# This function sums the values in the list
# It needs an input list that is integers
def sumRecursive(inputList):
    newList = inputList[:]
    x = len(inputList)
    # When we reach the end of the function, add 0
    if x == 0:
        return 0
    # This part should activate first and continue down the recursion chain.
    else:
        newList.pop()
        return inputList[x - 1] + sumRecursive(newList)


intifyList(stringList)
print(sumRecursive(intList))
