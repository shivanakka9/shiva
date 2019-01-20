#stmt = input("enter a stmt ")
#lenwords=[ len(i) for i in stmt.split()]
#print(lenwords)

##char = "a","b","c"
#print(char)
#print (type(char))

emp=[]
l= int(input("enter length "))
for i in range (0,l+1):
    ele= input(" enter an element")
    if ele.isdigit():
        ele=int(ele)
        emp.append(ele)
    elif"." in ele:
        e= ele.split(".")
        for i in e:
            if i.i is digit():
                ele = float(ele)
                emp.append(ele)
                else:
                    emp.append(ele)
                else:
                    emp.append(ele)
                    emp=tuple(emp)
                    print (emp)

    


