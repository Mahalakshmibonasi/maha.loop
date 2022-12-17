# i=1
# while i<=100:
#     if i%2==0:
#         print(i*-1,end=" ")
#     else:
#         print(i,end=" ")
#     i=i+1  

      

# i=1
# while i<=5:
#     k=i
#     j=1
#     while j<=i:
#         print(k,end=" ")
#         k=k-1
#         j=j+1
#     print()
#     i=i+1    

# i=1
# while i<=5:
#     j=1
#     while j<=5:
#         print(i,end=" ")
#         j=j+1
#     print()
#     i=i+1    

# a=12
# i=1
# while i<=4:
#     j=1
#     while j<=i:
#         print(a,end=" ")
#         j=j+1
#         a=a+1
#     print()
#     i=i+1    

# i=1
# while i<=4:
#     j=0
#     while j<=i:
#         print(j*j,end="")
#         j=j+1
#     print()
#     i=i+1
    
# i=1
# while i<=5:
#     b=1
#     while b<=i-5:
#         print(" ",end=" ")
#         b=b+1
#     j=1
#     while j<=i:
#         print(j,end=" ")
#         j=j+1
#     print()
#     i=i+1    

# i=5
# while i>=1:
#     b=1
#     while b<=5-i:
#         print(" ",end="")
#         b=b+1
#     j=1
#     while j<=i:
#         print(j,end="")
#         j=j+1
#     print()
#     i=i-1

# i=0
# while i<=4:
#     j=0
#     while j<=i:
#         print(j*i,end=" ")
#         j=j+1
#     print()
#     i=i+1

# i=1
# str=input("enter the ")
# a=len(str)
# while i<=a:
#     j=1
#     while j<=i+1:
#         print(str[j],end=" ")
#         j=j+1
#     print()
#     i=i+1    



# i=1# while i<=5:
#     print(" "*(5-i),end=" ")
#     j=1
#     while j<=i:
#         print("*",end=" ")
#         j=j+1
#     print()
#     i=i+2
# i=3
# while i>=1:
#     print(" "*(5-i),end=" ")
#     j=1
#     while j<=i:
#         print("*",end=" ")
#         j=j+1
#     print()
#     i=i-2        


# a="python"
# l=len(a)
# i=0
# while i<l:
#     j=0
#     while j<=i :
#         print(a[i],end=" ")
#         j+=1
#     print()
#     i=i+1


# i=1
# k=ord("A")
# while i<=4:
#     j=1
#     while j<=i:
#         print(chr(k),end=" ")
#         k=k+1
#         j=j+1
#     print( )
#     i=i+1

# def a(a,b):
#     c=a+b
#     print(c)
# print("hello")
# a(5,6)

# def x(A):
#     print(A*2)
# x(2)

'''positinal argument'''


# def  fun(a,b=2,c=4):
#     print(a,b,c)
# fun(3,)

''''arbitary argument'''

# def fun(x,y):
#     print(y,x)
# fun(y=6,x=6)

'''arbitary keyward argument'''
# def fun(*a):
#     print(a)
# fun(2,3,4,5,6)b
# a=[2,3,4,5,6]


# year=int(input("enter a year"))
# month=int(input("enter a month"))
# date=int(input("enter the date"))
# if date >0 and date <=30:
#     date+=1
#     print("next date is",year,"/",month,"/",date)
# else:
#     print("next date",date)

# year=int(input("enter the year"))
# month=int(input("enter the month"))
# date=int(input("enter the date"))
# if date>0 and date<30:
#     date=date+1
#     print("next date is",year,"/",month,"/",date)
# else:
#     print("next date",date)

# i=10
# while i<10:
#     print(i)
#     i=i+1
# else:
#     while i>-5:
#         print(i)
#         i=i-1

# a=int(input("enter the num"))
# b=int(input("enter the num"))
# while a<=b:
#     i=1
#     while i<=b:
#         print(a,"*",i,"=",a*i)
#         i=i+1
#     print()
#     a=a+1

# a="ma5hal@aks6hmib"
# i=0
# b=" "
# while i<len(a):
#     if a[i]>="a" and a[i]<="z":
#         b=b+a[i]
#         i=i+1
# print(i)

a=[100,200,300,400]
b=[10,20,30,40]
c=[]
i=0
b.reverse()
while i<len(a):
    c.append(a[i],b[i])
    i=i+1
print(c)
