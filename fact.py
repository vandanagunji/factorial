#factorial of a number using recursion
def fact(n):
	if n==1:
		return n
	else:
		return n*fact(n-1)
num=5
#check if num is negative
if num<0:
	print("factorial does not exist")
elif num==0:
	print("fatorial for 0 is 1")
else:
	print("factorial of",num,"is",fact(num))
