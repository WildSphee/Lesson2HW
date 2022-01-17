# Exercise 1
#
# userinput = input("Type a number")
#
# if userinput == "exit":
#     exit()
# try:
#     print(int(userinput))
# except:
#     print("Error, type a number")
#

#Exercise 2
#
# userinput = input("Type a series of numbers").split()
# try:
#     userinput = list(map(int, userinput))
#
#     factors = []
#     for i in range(1, min(userinput)+1):
#         assumption = True
#         for num in userinput:
#             if num % i != 0:
#                 assumption = False
#         if assumption:
#             factors.append(i)
#
#     print(factors)
#
# except:
#     print("please ensure all inputs are numbers")


# Exercise 2

userinput = input("Type a series of numbers").split()
try:
    userinput = list(map(int, userinput))

    factors = []
    for i in range(1, min(userinput)+1):
        # assumption = True
        for num in userinput:
            if num % i != 0:
                break
            factors.append(i)

    print(factors)

except:
    print("please ensure all inputs are numbers")