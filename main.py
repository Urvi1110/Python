import  calculator as c
import scientific as s

print("1.calculator" \
"2.scientific calculator" \
"3.exit")

ch =  int(input("enter the choice :"))

if ch == 1 :
    while True:
        print("1.add" \
        "2.subtract" \
        "3.multiply" \
        "4.divide" \
        "5.exit")

        n = int(input("enter the choice : "))

        if n == 1 :
            a = int(input("enter the digit-1 : "))
            b = int(input("enter the digit-2 : "))

            print(f"addition : {c.add(a,b)}")

        elif n == 2 :
            a = int(input("enter the digit-1 : "))
            b = int(input("enter the digit-2 : "))

            print(f"substraction : {c.subtract(a,b)}")

        elif n == 3 :
            a = int(input("enter the digit-1 : "))
            b = int(input("enter the digit-2 : "))
    
            print(f"multiplication : {c.multiply(a,b)}")

        elif n == 4 :
            a = int(input("enter the digit-1 : "))
            b = int(input("enter the digit-2 : "))
    
            print(f"division : {c.divide(a,b)}")

        elif n == 5 :
          break

        else :
          print("wrong choice")

elif ch == 2 :
    while True:
        print("1.sqrt" \
        "2.factorial" \
        "3.power" \
        "4.exit")

        n = int(input("enter the choice : "))

        if n == 1 :
            x = int(input("enter the number"))

            print(f"sqrt of {x} : {s.sqrt(x)}")

        elif  n == 2 :
            x = int(input("enter the number"))

            print(f"factorial of {x} : {s.factorial(x)}")

        elif n == 3 :
            x = int(input("enter the number"))
            y = int(input("enter the power"))

            print(f"{x} ^ {y} : {s.power(x,y)}")

        elif n == 4 :
            break

        else :
            print("wrong choice")

        
