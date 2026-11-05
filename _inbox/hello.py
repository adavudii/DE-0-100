trader_name = "Shafii"
exchange = "Bybit"
print(trader_name.upper())
print(trader_name.lower())
print(len(trader_name))
print(trader_name + " trades on " + exchange)

trader_name = "Shafii"
total_profit = 200
average_profit = 50.0

print(f"{trader_name} made a total of {total_profit} with an average of {average_profit} per trade")

trader_name = "Sage"
exchange = "Binance"
print(trader_name.upper())
print(trader_name.lower())
print(len(trader_name))
print(trader_name + " trades on " + exchange)
trader_name = "Sage"
total_profit = 800
average_profit = 85
print(f"{trader_name} made a total profit of {total_profit} with an average of {average_profit} per trade")

trades = [50, 80, 120, 200, 45]
print(trades)
print(trades[0])
print(trades[2])
print(len(trades))

trades = [50, 80, 120, 200, 45]

# Add a new trade
trades.append(300)
print(trades)

# Remove a trade
trades.remove(80)
print(trades)

# Sort trades from lowest to highest
trades.sort()
print(trades)

trades = ["BTC", "BNB", "ZIL", "ADA", "ETH", "AVAX"]

trades.append("SOL")
print(trades)
print(len(trades))

profit = 50

if profit > 100:
    print("Good trade!")
else:
    print("Bad trade!")

profit = -50

if profit > 200:
    print("Excellent trade!")
elif profit > 100:
    print("Good trade!")
elif profit > 0:
    print("Small win!")
else:
    print("Loss! Review this trade.")

# Loops

trades = [50, 80, 120, 200, 45]
for trade in trades:
    print(trade)

    trades = [50, 80, 120, 200, 45]
    for trade in trades:
        if trade > 100:
            print(f"{trade} was a good trade!")
        else:
            print(f"{trade} needs review")

trades = ["BTC", "BNB", "ZIL", "ADA", "SOL"]
for trade in trades:
    print(f"{trade} is in my portfolio")