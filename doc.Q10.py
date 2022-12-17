# n=int(input("enter the num"))
# f=0
# i=2
# while i<n:
#     if n%i==0:
#         f=f+1
#     i=i+1
#     if f==0:
#         print("prime num")
#     else:
#         print("not a prime num")

a=int(input("enter the num"))
count=0
i=1
while i<=a:
    if a%i==0:
        count =count+1
        i=i+1
    if count==2:
        print(a,"is a prime num")
    else:
        print("not a prime num")
    i=i+1