# SHAFII'S PYTHON FUNDAMENTALS — LEARNING NOTES
**Goal:** Data Engineering career + crypto trade pipeline portfolio project
**Phase:** 0 — Foundations (Restart)

---

## How to use this file
- One `##` section per Concept
- Drop your working code in the ```python``` blocks as you go
- Add a one-line "Key takeaway" at the end of each concept — this becomes your teaching content later

---

## Concept 1 — Variables

**Idea:** A variable is a labelled box that stores a value, so you can reuse it by name instead of retyping it.

```python
asset = "BTC"
entry_price = 61500
exit_price = 63200
trade_size = 0.5
```

**Rules:**
- No spaces in names → use `_` (e.g. `entry_price`)
- Can't start with a number
- Case-sensitive

**My practice code:**
```python
asset = "BTC"
entry_price = 62500
exit_price = 61000
trade_size = 0.5

print(asset)
print(entry_price)
print(exit_price)
print(trade_size)
```

**Key takeaway:**
>my key take aways are that variables are a box that holds information of a particular data and the equal to sign = means put this information into this box as opposed to what the equal sign would really mean in mathematical terms, i also used some commands in python to learn how to use the terminal to run codes, some things i learnt include;
- using find ~ -name "cryptotrades.py" to find where my cryptotrades file is located
- cd "Project DE 0-100" to move that folder into terminal
- cmd + s to save a file an unsaved with a dot at the front won't work with the terminal below it
- python3 cryptotrades.py to run the code after it was saved
- Cmd + Shift + V to open a notes file to record my lessons
- But before that i learned to open a new "pretty" terminal preview so my workflow and codes are easily translated for understanding.


---

## Concept 2 — Data Types

**Idea:** Python needs to know what kind of value something is, so it knows how to handle it.

**My practice code:**
```python
print("Entry price: " + str(entry_price))

print(f"Entry price: {entry_price}")
print(f"Asset: {asset}")
print(f"Exit price: {exit_price}")
print(f"Trade size: {trade_size}")
```

**Key takeaway:**
>Here i learnt the different data types and combining them in a single code as python needs special commands to add/make use of several data types and merging them together
The different types of data we have includes
- str - texts - "BTC"
- int - whole numbers - 62500
- float decimal numbers - 0.5
- bool - true/false - True 
* Note: Texts usually needs to be place in quotes for python to register it

The str(entry_price) temporarily turns the number 62500 into text "62500" for python to understand it, 
- f right before the opening quotes - tells  python "this string has variables in it"
- the variables go inside {} so it takes out the need for a + or str() , so python converts it automatically 

---

## Concept 3 — Basic Operations

**Idea:** Python can do maths directly on your variables using operators
Operator	Meaning	Example
+	addition	5 + 3 = 8
-	subtraction	5 - 3 = 2
*	multiplication	5 * 3 = 15
/	division	10 / 4 = 2.5 (always returns a float)
**	power	10 ** 2 = 100
%	modulus (remainder)	10 % 3 = 1

**My practice code:**
```python
For profit/loss on a trade we have; 

profit_loss = (exit_price - entry_price) * trade_size
print(f"Profit/Loss: {profit_loss}")

For rounding () we have;
average_check = round(profit_loss / 3, 2)
print(f"Example average (rounded): {average_check}")
```

**Key takeaway:**
>In f-strings you can make use operators (basically maths to run specific calculations and the big idea is that this set of calculative instructions only need to be given to the program once, after that is runs the same calculation on the variables given to it in the f-sting no matter what the variables are changed to)

i also used the round () which is used to average full list of trades 

---

## Concept 4 — Strings & F-Strings

**Idea:** Strings have built-in methods i.e actions you can perform on them:

F-strings let you drop variables straight into text:

**My practice code:**
```python
Strings:-

asset = "BTC"

print(asset.upper())     # BTC
print(asset.lower())     # btc
print(len(asset))        # 3 (counts characters)

F-strings:-

print(f"{asset} trade resulted in a profit/loss of {profit_loss}")
```


**Key takeaway:**
>Strings have built in methods like .upper(), .lower(), and len(), they generally let me transform or measure texts.
---

## Concept 5 — Lists

**Idea:** Right now, we have only handles one trade at a time. In reality, you'll have hundreds or thousands of trades — you can't make a new variable for every single one.
A list solves this — it's a single container holding multiple values together.

**My practice code:**
```python
For Lists we have:-

trade_profits = [-750, 320, 150, -80, 500]

To interatact with values in list we have:-

print(trade_profits[0])   # -750  (the first item)
print(trade_profits[2])   # 150   (the third item)
print(len(trade_profits)) # 5     (how many items total)

To add or remove things in lists we have:-
trade_profits.append(200)      # adds 200 to the end
trade_profits.remove(-80)      # removes -80 from the list
trade_profits.sort()           # sorts lowest to highest

**Key takeaway:**
> "A list is a data structure that groups multiple values together under one variable name. You can access, add, or remove individual items in it, modification methods includes .append(), .remove(), and .sort()
NOTE: Python counts from 0, so the first item in a list is at position 0, not 1, like most people would assume."

---

## Concept 6 — Conditionals (if/elif/else)

**Idea:**
This is where your code starts making decisions instead of just running top to bottom.
profit_loss = -750
Operator	Meaning
>	greater than
<	less than
==	equal to (note: two equals signs — one = means "store," two means "compare")
!=	not equal to
>= / <=	greater/less than or equal to


**My practice code:**
```python
if profit_loss > 200:
    print("Excellent trade!")
elif profit_loss > 0:
    print("Good trade!")
elif profit_loss == 0:
    print("Break-even trade.")
else:
    print("Loss — review this trade.")
```

**Key takeaway:**
>Conditionals let code make decisions by checking conditions top to bottom, running only the first one that's true; indentation tells Python what belongs to each condition

---

## Concept 7 — Loops
A loop lets you run the same block of code automatically for every item in a list, without repeating yourself.
**Idea:**

**My practice code:**
```python
for trade in trade_profits:
    print(trade)

How to read this: "For each item in trade_profits, temporarily call it trade, and run the indented code below using that value." It repeats once per item — 5 items, 5 runs — automatically.

for trade in trade_profits:
    if trade > 200:
        print(f"{trade} — Excellent trade!")
    elif trade > 0:
        print(f"{trade} — Good trade!")
    else:
        print(f"{trade} — Loss, review this.")
```

**Key takeaway:**
>A for loop repeats a block of code once per item in a list, so combining it with conditionals lets me automatically judge every trade without writing the same check multiple times, so basically instead of having to run conditions over every single block of code per item list, i can just use a for loop to run everything once and get the result i need

---

## Concept 8 — Functions

**Idea:** A function is a reusable block of code you define once and can run (call) as many times as you want, with different inputs each time

**My practice code:**
```python
def judge_trade(profit_loss):
    if profit_loss > 200:
        return "Excellent trade!"
    elif profit_loss > 0:
        return "Good trade!"
    else:
        return "Loss, review this."

Breaking that down:
def — tells Python "I'm defining a function"
judge_trade — the name you're giving it (your choice, should describe what it does)
(profit_loss) — a parameter: a placeholder variable that will hold whatever value you feed the function when you call it
return — sends a result back out of the function, instead of just printing it

return vs print — the key distinction
print() just displays something on screen — it's a dead end, nothing is saved
return hands a value back out of the function, so you can store it in a variable and use it again later (in another calculation, another function, saved to a file, etc.)
```
**My practice code 2:**
```python
def total_and_average(trades):
    total = sum(trades)
    average = round(total / len(trades), 2)
    return total, average

    * sum(trades) — built-in function that adds up every number in a list
total / 
* len(trades) — total divided by how many trades, i.e. the average
* return total, average — sends both values back at once
```

**Key takeaway:**
>Functions let me define reusable logic once (with def) and reuse it on different inputs; return sends a value back out so it can be stored and used later, unlike print() which just displays it. A function can return multiple values at once, separated by commas.

---

## Debugging Tips Log
1. print(entry) → print(entry_price) in Concept 1
My initial practice code has print(entry) instead of print(entry_price). "entry" isn't a variable i defined so this would actually throw a NameError if not caught, i fixed that by putting in the correct entry.
2. Fix practice code for concept 3 as well, fix the line that actually creates " profit_loss: " instead of jumping straight to print(f"Profit/Loss:  {profit_loss})

| Error | What caused it | Fix |
|---|---|---|
| | | |

---

## Next Up
- Dictionaries
- File I/O
- Basic OOP
- SQL basics
- Milestone: CSV → SQLite mini pipeline
