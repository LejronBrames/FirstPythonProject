from datetime import datetime
now = datetime.now()

x = str(input("Please input your timezone: "))

if x == str("EU"):
	print("Todays Date is: %s / %s / %s " % (now.day, now.month, now.year))

if x == str("US"):
	print("Todays Date is: %s / %s / %s " % (now.month, now.day, now.year))
