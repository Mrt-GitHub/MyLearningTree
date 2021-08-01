'''n = made only the first 10 fibonacci'''
n = 10
s1,s2 = 0,1
k = []
for i in range(0,n):
    t = s1 + s2
    s1 = s2
    k.append(s1)
    s2 = t    
print(k)

'''n = created Fibonacci list up to desired length'''
# n = int(input("Please enter a number : "))
# fib_list = [0, 1]
# i = 2
# while len(fib_list)<=n:
#     fib_list.append(fib_list[i-1]+fib_list[i-2])
#     i+=1
# del (fib_list[0],fib_list[-1])
# print(fib_list)