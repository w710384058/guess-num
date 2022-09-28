import random 

r = random.randint(1,100)
count = 0
while True:
	num = input("請猜數字:")
	num = int(num)
	count = count + 1
	if num == r :
		print("終於猜對了!")
		print('你總共猜了',count,'次')
		break
	else:
		if num > r:
			print("比答案大")
		else:
			print("比答案小")
	print('你總共猜了',count,'次')		