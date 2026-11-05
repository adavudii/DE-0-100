# TODAY: Day 2 (Tuesday), User Input and type conversion

**Open:** `exercises/day02_input.py` (create it empty), and `reps.py` for the reps block.
**Time (3 hours, morning):** 45 min study, 75 min exercises, 30 min reps, 30 min notes and commit.

## 1. Study first (45 min): read, then retype it yourself

`input()` pauses the program, shows a message, and returns **whatever was typed, always as text (str)**, even if it looks like a number. Numbers must be converted with `int()` or `float()` before you can do arithmetic.

```python
name = input("What is your name? ")
print(f"Hello, {name}")

age_text = input("How old are you? ")      # age_text is a str, e.g. "25"
age = int(age_text)                         # now it is an int, 25
print(f"Next year you will be {age + 1}")

price = float(input("Price: "))             # convert in one step
print(type(price))                          # <class 'float'>
```

Check yourself before moving on: type `5` at an input prompt, then print `type(...)` of what you got. It is `str`, not `int`. That fact is the whole lesson.

## 2. Exercises (75 min), in `exercises/day02_input.py`

1. Ask for the user's name and print a greeting with an f-string.
2. Ask for their age, convert it, and print how old they will be in 5 years.
3. Ask for a price (float) and a quantity (int), then print the total.
4. Ask for two whole numbers and print their sum, difference and product.
5. **Predict first:** write on paper what `print(type(input("x ")))` prints when you type `7`. Then run it and compare.
6. **Break it on purpose:** run exercise 2 and type `abc` for the age. Read the error message and write down in one line what it says. (You will handle this properly in a later session. For now, just read it.)

Rules: no copy-paste from notes. Peek only after you've been stuck for 10 minutes, and write down which step you got stuck on.

## 3. Reps (30 min), in `reps.py`

Retype from a blank section: variables, str/int/float, `print()`, `type()`, f-strings and arithmetic from Day 1. Then add one new rep: an `input()` plus conversion line.

## 4. Close the day (30 min)

- Add 3 to 5 lines to `notes/` about what input() returns and why conversion matters.
- Write below what was confusing: ______
- Update `tracker.md` (Day 2 to done), then commit.

## Not finished today? Write it here

-

## Tomorrow (Wed): Day 3, Strings: indexing and slicing

Start with the 20-minute placement check (blank file, no notes): input and conversion, a decision and a loop, a function and a dictionary. It shows which later topics you already know.
