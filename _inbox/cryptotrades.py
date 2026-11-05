asset = "BTC"
entry_price = 62500
exit_price = 61000
trade_size = 0.5

print(asset)
print(entry_price)
print(exit_price)
print(trade_size)

print("Entry price: " + str(entry_price))

print(f"Entry price: {entry_price}")
print(f"Asset: {asset}")
print(f"Exit price: {exit_price}")
print(f"Trade size: {trade_size}")

profit_loss = (exit_price - entry_price) * trade_size
print(f"profit/loss: {profit_loss}")
average_check = round(profit_loss / 3, 2)
print(f'Example average (rounded): {average_check}')

print(asset.upper())
print(asset.lower())
print(len(asset))

trade_profits = [-750, 320, 150, -80, 500]

print(trade_profits)
print(trade_profits[0])
print(len(trade_profits))
trade_profits.append(200)
print(trade_profits)

trade_profits.remove(-80)
print(trade_profits)

trade_profits.sort()
print(trade_profits)

profit_loss = -750

if profit_loss > 200:
    print("Excellent trade!")
elif profit_loss > 0:
    print("Good trade!")
elif profit_loss == 0:
    print("Break-even trade.")
else:
    print("Loss - review this trade.")

first_trade = trade_profits[0]

if first_trade > 200:
    print("Excellent trade!")
elif first_trade > 0:
    print("Good trade!")
else:
    print("Loss - review this trade.")

second_trade = trade_profits[1]

if second_trade > 200:
    print("Excellent trade!")
elif second_trade > 0:
    print("Good trade!")
else:
    print("Loss - review this trade.")

for trade in trade_profits:
    if trade > 200:
        print(f"{trade} - Excellent trade!")
    elif trade > 0:
        print(f"{trade} - Good trade!")
    else:
        print(f"{trade} - Loss, review this.")

def judge_trade(profit_loss):
    if profit_loss > 200:
        return "Excellent trade!"
    elif profit_loss > 0:
        return "Good trade!"
    else:
        return "Loss, review this."

for trade in trade_profits:
    verdict = judge_trade(trade)
    print(f"{trade}: {verdict}")

def total_and_average(trades):
    total = sum(trades)
    average = round(total / len(trades), 2)
    return total, average

total, average = total_and_average(trade_profits)
print(f"Total: {total}")
print(f"Average: {average}")

trade = {
    "asset": "BTC",
    "entry_price": 62500,
    "exit_price": 61000,
    "trade_size": 0.5
}
trade["profit_loss"] = -750

print(trade)
print(trade["asset"])
for key, value in trade.items():
    print(f"{key}: {value}")