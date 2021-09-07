#Faulty calculator
#Design a calculator which  gives wrong input whebn user enters the following  calculation
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4

x1=input("Enter the opertions you want.+,-,/,%,* \n")
x2=int(input("Enter the 1st number"))
x3=int(input("Enter the 2nd number"))
if x2==45 and x3==3 and x1=='*':
    print("555")
elif x2==56 and x3==9 and x1=='+':
    print("77")
elif x2==56 and x3==6 and x1=='/':
    print("4")
elif x1=='*':
    mult=x2*x3
    print(mult)
elif x1=='+':
    add=x2+x3
    print(add)
elif x1=='-':
    sub=x2-x3
    print(sub)
elif x1=='/':
    div=x2/x3
    print(div)
elif x1=='%':
    perc=x2%x3
    print(perc)
else:
    print("Something went wrong")

