# code to make a calculator
num1 = int(input("Enter First Number :"))
num2 = int(input("Enter Second Number :"))

operator = input("Enter Your Operator :")

match operator:
    case "+":
        print("Sum of two numbers", num1 ,"and" , num2,"is :", num1 + num2)
    case "-":
        print("Difference of two numbers", num1 ,"and",num2, "is :", num1 - num2)
    case "*":
        print("Product of two numbers", num1, "and", num2 , "is :", num1 * num2)   
    case "/":
        print("Division of two numbers" , num1,"/",num2,"is :", num1 / num2)  
    case "%":
        print("Remainder of two numbers", num1,"and", num2,"is :", num1 % num2)
    case "//":
        print("Quotient of two numbers", num1,"and", num2,"is :", num1 // num2)
    case "**":
        print("Value of",num1, "with power of",num2, "is :",num1 ** num2)      
    case _:
        print("Please enter valid operator")    