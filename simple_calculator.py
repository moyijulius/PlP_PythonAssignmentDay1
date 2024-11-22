num1=float(input("Enter number one:"))
num2=float(input("Enter number two:"))
operator=input("Enter +,-,*,/:")
if operator=="+":
         print(f"{num1} +{num2} ={num1+num2}")
elif operator=="-":
         print(f"{num1} -{num2} ={num1-num2}")
elif operator=="*":
         print(f"{num1} *{num2} ={num1*num2}")
elif operator=="/":
         if num1 !=0:
                print(f"{num1}/{num2} ={num1/num2}")
         else:
                print("Error :division by zero not allowed")

else:
       print("Invalid input operator")
       