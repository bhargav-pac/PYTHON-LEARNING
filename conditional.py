'''name=input("Enter Name:")
cname=input('Enter company Name:')
if cname=='paccore':
    print(name,'Welcome To Paccore')
else:
    print("Invalid User")    '''

'''
n1=int(input("enter any number:"))
n2=int(input("enter any number:"))
n3=int(input("enter any number:"))
if n1>n2 and n1>n3:
    print(n1,'is Biggest Number')
elif n2>n1 and n2>n3 :
    print(n2,"is Biggest Number")
else:
    print(n3,"is Biggest Number")   '''
'''
n=int(input('enter any number:'))
if n%2!=0:
     print("Weird")
elif n%2==0 and 2<=n<=5:
     print("Not Weird")
elif n%2==0 and 6<=n<=20:
     print("Weird") 
elif n%2==0 and n>20:
     print("Not Weird")    '''
"""n=int(input())
for i in range(n):
    a=i**2
    print(a)"""
'''
n=int(input("Enter any Number:"))
if 1<=n<=100:
    print("Number is between 1 to 100")
else:
    print("Number is not between 1 to 100")    '''
"""
n=input("enter:")
r=0
for i in n:
    print(" index ",r,'is number of:',i)
    r=+1 """

'''for i in range(10):
    print('HAI')    '''


'''for i in range(20):
    if i%2!=0:
        print(i)'''
'''
a=eval(input("Enter any list:"))
s=0;
for i in a:
    s+=i;
print("Sum is :",s)'''
'''
n=int(input("Enter number:"))   
sum=0   
i=1   
while i<=n:   
   sum=sum+i   
   i=i+1   
print("The sum of first",n,"numbers is :",sum)  '''
'''
n = int(input()) 
for i in range(1, n + 1):
    print(i, end='') '''

'''n=''
while n!='ram':
    n=input(':')
print('thanks')'''

'''
h='hai'
del(h)
print(h)'''

'''
n = int(input("Enter a positive integer:")) 
for i in range(1, n):  
   print(str(i) * i)  '''

#a=2*("RAM")
#print(a)   

a="RAM"
b="ram"
print('a<b is',a<b)
print('a<=b is',a<=b)
print('a>b is',a>b)
print('a>=b is',a>=b)
