# i=1
# while i<=100:
#     if i%7==0:
#         print(i)
#     i=i+1


"""given number is prime or not..."""
# a=int(input('enter any number:'))
# i=2
# fact=0
# while i<a:
#     if a%i==0:
#         fact+=1
#     i+=1
# if fact<1:
#     print("prime")
# else:
#     print("not a prime ")
"""1 to 100 primes and count...."""
# a=1
# c=0
# while a<=100:
#     i=2
#     fact=0
#     while i<a:
#         if a%i==0:
#             fact+=1
#         i+=1
     
#     if fact<1:
#         print("prime",a)
#         c+=1
#     else:
#         print("not prime",a)
#     a+=1
# print(c)
"""making prime numbers list of 1 to 100."""
# a=1
# c=[]
# while a<=100:
#     i=2
#     fact=0
#     while i<a:
#         if a%i==0:
#             fact+=1
#         i+=1
     
#     if fact<1:
#         # print("prime",a)
#         c.append(a)
#     # else:
#     #     print("not prime",a)
#     a+=1
# print(c)
# """given list find prime of the list..."""
# a=[1,2,97,4,11,7,12,9,5,32,21,23]
# b=[]
# i=0
# c=0
# while i<len(a):
#     j=2
#     fact=0
#     while j<a[i]:
#         if a[i]%j==0:
#             fact+=1
#         j+=1
#     if fact<1:
#         # print(a[i])"""checking prime r not"""
#         b.append(a[i])
#         c+=1
#     i+=1
# print(b,"\ncount of the primes in list:",c)
# # print(c)

# a=int(input('enter any number:'))
# def prime(a):
#     i=2
#     fact=0
#     while i<a:
#         if a%i==0:
#             fact+=1
#         i+=1
#     if fact<1:
#         return ("prime")
#     else:
#         return ("not a prime ")
# print(prime(a))
"""function arbitary........"""
# # a=int(input('enter any number:'))
# def prime(*a):
#     i=2
#     fact=0
#     while i<a[i]:
#         if a[i]%i==0:
#             fact+=1
#         i+=1
#     if fact<1:
#         return (a[i])
#     else:
#         return (a[i])
# print(prime(1,4,879,67,8,3))
"""if else....prime"""

# a=int(input("enter any number:"))
# if a==3 or a==2 or a==3 or a==5 or a==7 :
#     print("prime")
# elif a%2==0 or a%3==0 or a%5==0 or a%7==0:
#     print("not a prime")
# else:
#     print("prime num")


a=int(input("enter the num"))
i=0
while i<a:
    b=a%10
    c=a//10
    d=b*c
    i=i+1
print(d)