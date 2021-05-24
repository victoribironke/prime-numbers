import time

def finder(a, b):
	ans1 = []
	ans2 = []
	for i in range(a, b + 1):
		for j in range(2, i + 1):
			if i % j == 0:
				ans1.append(j)
		if len(ans1) == 1:
			ans2.append(i)
			ans1.clear()
		else:
			ans1.clear()
	print(f"Prime numbers between {a} and {b} are {ans2}")

start = int(input("Enter Lower Number = "))
end = int(input("Enter Higher Number = "))
time.sleep(0.5)
finder(start, end)
