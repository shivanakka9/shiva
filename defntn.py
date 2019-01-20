
#def avg(a,b,c,d,e):
 #   res = (a+b+c+d+e)/5
  #  print (res)
#avg(10,20,30,40,50)
#num1 = int(input( "enter  a number"))
#num2 = int(input( "enter  a number"))
#def addnums( num1,num2):
 ##   res = num1+num2
#    print(res)
#    return res
#num1 = int(input( "enter  a number"))

#num2 = int(input( "enter  a number"))
#stmt = input("choose an operation")
#addnums= (num1+num2)
#subnums = (num1-num2)
#print(addnums)
#print(subnums)


def supersum(num):
    ans = 0
    if len(str(num))== 1:
         return num
    else:
           for i in str(num):
                ans = ans+int(i)
           if len (str(ans))>1:
              return supersum(ans)
           else:
               return ans
#print (supersum(67899))

def factorial(num):
    if num == 1:
        return num
    else:
        return  num*factorial(num-1)
print(factorial(9))
    
