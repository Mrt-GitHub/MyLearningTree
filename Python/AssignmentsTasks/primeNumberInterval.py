'''it will show how many prime numbers are there when typing a last interval'''        
num=int(input("Write last interval  :  "))
k=[2]
for i in range(3,num):
    for j in range(2,int((i**0.5)+1)):
        if i%j==0:
            break
    else:
        k.append(i)
print(k)

# num=int(input("Write a number  :  "))
# while num > 1:
#     for i in range(2,num):
#         if num%i==0:
#             print("Not Prime")
#             break
#     else:
#         print("Prime")