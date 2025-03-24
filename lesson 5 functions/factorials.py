def recur_f(n):
    if n == 1:
       return n
    else:
        return n*recur_f(n-1)
    
num = int(input("enter number:"))

if num < 0:
      print("sorry,factorials do not exist for negative numbers")
elif num ==0:
     print('the factorial of 0 is 1')
else:
    print("the factorial of", num,"is", recur_f(num))
