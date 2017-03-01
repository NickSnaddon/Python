import time

print("Restaurant Tip calculator")
time.sleep(3)
bill = float(input("How much is the bill?: "))
tipPercentage = float(input("How much will you be tipping?: "))
tipNum = (tipPercentage / 100) + 1
total = bill * tipNum
print("The total cost of the meal is £", total)
time.sleep(2)
peopleNum = int(input("How many people are dining?: "))
shares = total / peopleNum
time.sleep(2)
print("Each person must pay £", shares)



