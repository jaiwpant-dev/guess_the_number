## No guessing game 

print("welcomee")
print("let's start the game")
print("are you ready")
input("")
print("Instructions to be noted ")
print("if your guessed no is smaller than actual no it will show higher which means to increase your guessed no and vise versa")

attempt=2
val=69
x=int(input("Entre your guess :"))

print(x)

if x >= 70:
	print("(low)")
if x <= 68:
	print("(high)")
if x == val:
	attempt+=1
	print("you got that")
	print("No of attempt :",attempt)


while val != x:
	x=int(input("guess again :"))
	print(x)
	if x >=70:
		print("(low)")
	if x <=68:
		print("(high)")
	if x ==69 :
		print("got it ")
	if x !=69:
		attempt+=1
	if x==69:
		print("attempt you took :",attempt)
		