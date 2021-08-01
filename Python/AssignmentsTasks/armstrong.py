x=input("Write a positive number : ")
if x.isdigit():
    t=sum([int(x[i])**len(x) for i in range(len(x))])
    print(f"{t} is an Armstrong number" if t==int(x) else f"{int(x)} is not an Armstrong number")
else:
    print(f"It is an invalid entry. Don't use non-numeric, float or negative values")

# x=input("Write a positive number : ")
# if x.isdigit():
#     t=sum([int(x[i])**len(x) for i in range(len(x))])
#     if t==int(x):
#         print(f"{t} is an Armstrong number")
#     else:
#         print(f"{int(x)} is not an Armstrong number")
# else:
#     print(f"It is an invalid entry. Don't use non-numeric, float or negative values")