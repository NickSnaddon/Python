import time

print("Restaurant Tip calculator")
time.sleep(3)
bill = float(input("How much is the bill?: "))
tipPercentage = float(input("How much will you be tipping?: "))
tip = (bill / 100) * tipPercentage
total = bill + tip
print("The total cost of the meal is £", total)
time.sleep(1)
peopleNum = int(input("How many people are dining?: "))
shares = total / peopleNum
time.sleep(1)
print("Each person must pay £", shares)
time.sleep(1)
distance = float(input("How long is the journey home, in miles?: "))
distCost = distance * 0.45
time.sleep(1)
print("The cost of the Taxi journey home is £", distCost)
totalEvening = total + distCost
time.sleep(1)
print("The total cost for the whole evening is £", totalEvening)
totalShares = totalEvening / peopleNum
time.sleep(1)
print("Assuming that everyone is taking the same taxi home, each person must pay £", totalShares,"to cover the entire evening.")

