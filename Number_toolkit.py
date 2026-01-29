n1 = int(input("Enter a number: "))
do = input("Enter which task is done on it: ")


# prime func.
def prime(n1):
    if  n1 <= 0: 
        print("The entered number",n1,"is not a prime number!")
    else :
        for i in range(2, int(n1**0.5) + 1):
            if n1 % i == 0:
                print("The entered number",n1,"is not a prime number!")
            else:
                print("The entered number",n1,"is a prime number!")

                return 

# HCF func.
def hcf(n1,n2):
    if n2 == 0:
        return n1
    else:
        return hcf(n2,n1%n2)
    6
# LCM function
def lcm(n1,n2,current=1):
    if current % n1 ==0 and current % n2 == 0:
        return current
    else:
       return lcm(n1,n2,current + 1)
    
# fibbonachi fun.
def fibonachi(n1):
    if n1==1:
        return 0
    elif n1 == 2:
        return 1
    else:
        return (fibonachi(n1-1) + fibonachi(n1-2))
    
    
# checking that if user want to  do prime task
if do =="prime":
     prime(n1)

#checking that if user want to  do fibonachi task
elif do == "fibonachi":
   ans=fibonachi(n1)
   print("The",n1,"th fibbonachi number is:",ans)
   for i in range(1,n1+1):
       print(fibonachi(i))

#checking that if user want to  do hcf task
elif do =="hcf":
   n2 =int(input("Enter 2nd number: "))
   ans =hcf(n1,n2)
   print("The HCF of",n1,"and",n2,"is:",ans)
   
# checking that if user want to  do lcmtask
elif do == "lcm":
    n2 =int(input("Enter 2nd number: "))
    ans=lcm(n1,n2)
    print("The LCM of",n1,"and",n2,"is:",ans)
    
    

