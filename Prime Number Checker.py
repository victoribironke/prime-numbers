import time

def checker(num):
	lists = [x for x in range(num + 1)]
	lists.remove(1)
	lists.remove(num)
	lists.remove(0)
	if num == 1:
		print("1 is not a prime number.")
	else:
		for i in lists:
			if num % i == 0:
				print(f"{num} is not a prime number.")
				break
		else:
			print(f"{num} is a prime number.")	

number = int(input("Enter Number = "))
time.sleep(0.5)
checker(number)
