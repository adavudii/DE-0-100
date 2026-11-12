## Python Practice Session — Variables and Data Types

**Date:** October 19, 2026

### What I studied
- Creating variables and assigning values.
- Understanding strings (`str`), integers (`int`), and floating-point numbers (`float`).
- Using `print()` to display values.
- Using `type()` to check data types.
- Using f-strings to combine variables into a sentence.

### What I practiced
I used my `reps tab.py` file in VS Code to create variables for my name, age, and height. I printed their values, checked their data types, and formatted them into a sentence using an f-string.

### What I learned
- `"2500"` is a string because it is enclosed in quotation marks.
- `28` is an integer.
- `178.5` is a float.
- `type()` tells me the data type of a value.
- F-strings let me insert variables into text.

### Challenges
I needed help opening the integrated terminal in VS Code and running my Python script. I successfully ran the script and got the expected output.

### Next session
Practice Python arithmetic and operators, then continue with the fundamentals.

## Day 2 — Python Input and Type Conversion

**Status:** Completed

### What I learned

Today I learned how to receive user input in Python and convert that input into different data types.

1. **`input()`** — collects information from the user. Everything received through `input()` is initially a string (`str`), even when the user enters a number.
2. **`int()`** — converts suitable values into integers (whole numbers).
3. **`float()`** — converts suitable values into floating-point numbers (decimal numbers).
4. **`str()`** — converts values into strings, allowing numbers to be handled as text.
5. **`type()`** — checks the data type of a value.
6. **f-strings** — allow variables to be inserted into formatted text.

### Practical work

Built a Python program that:
- Asks for the user's name.
- Collects their age and converts it to an integer.
- Collects their height and converts it to a float.
- Displays the information using f-strings.
- Checks the resulting data types using `type()`.

### What I understood

Python does not automatically interpret information entered through `input()` as numbers. It initially treats everything as text.

When we need to perform numerical operations, we must convert the input into the appropriate data type.

I also learned that converting a number into a string is useful when we need to combine numerical values with text.

### Assessment

- Practical exercise: Passed.
- Integer conversion: Understood.
- Float conversion: Understood.
- String conversion: Practised; purpose needs a little more reinforcement.

### Key takeaway

Getting the correct output isn't enough. Understanding the data type you're working with is equally important.

**Next:** Day 3 — continue Python foundations.
Day 3 — Strings: Indexing, Slicing, Immutability and Concatenation

What I learned

Today I learned how Python handles strings and how to manipulate them.

1. String indexing

* Positive indexing starts at 0.
* Negative indexing starts at -1 from the last character.
* Example: name[0] returns the first character, while name[-1] returns the last.

2. String slicing

Slicing allows me to extract sections of a string.

Syntax: text[start:end:step]

* The starting position is included.
* The ending position is excluded.
* The step determines how Python moves through the string.
* name[::-1] reverses an entire string.

3. String immutability

Strings are immutable, meaning individual characters cannot be changed directly after a string is created.

However, I can create a new string and reassign it to an existing variable.

4. String concatenation

Concatenation joins strings using the + operator.

I also learned that Python does not automatically insert spaces between concatenated strings.

5. F-strings

F-strings allow variables and expressions to be inserted directly into strings using curly brackets {}.

They are particularly useful when formatting text containing different data types.

Practical application

I built a simple customer record processor using:

* Customer name extraction through slicing.
* Customer ID extraction while preserving leading zeros.
* Age and customer information formatting using f-strings.
* Creation of an updated customer name without modifying the original string.

Mistakes and discoveries

* Python does not allow ordinary decimal integers to begin with leading zeros. Customer IDs should be treated as strings when their exact characters matter.
* F-strings require curly brackets, not parentheses, to evaluate variables and expressions.
* name[-3] returns one character, while name[-3:] returns the last three characters.
* name[::-1] reverses the entire string.

Key takeaway

Today helped me understand not just how to manipulate strings, but why these operations matter when processing structured text such as customer records and identification numbers.

Day 4 — Python String Methods

Topic: String manipulation and data cleaning.

Concepts learned

Today I learned how to manipulate and standardise strings using Python’s built-in string methods.

* .lower() — converts a string to lowercase.
* .upper() — converts a string to uppercase.
* .strip() — removes whitespace from the beginning and end of a string.
* .replace() — replaces specified characters or text with something else.
* .split() — separates a string into a list.
* .join() — combines list elements into a single string.
* .title() — capitalises the first letter of each word.

Important discoveries

1. String methods return new strings; they do not modify the original string.
2. String methods can be chained, for example: customer_email.strip().lower().
3. .split() and .join() perform opposite operations.
4. Cleaning data and correcting inaccurate data are two different things. We should not change customer information without evidence.

Practical exercise: Customer data cleaning

customer_name = " DANIEL JOHNSON "
customer_email = " DANIEL.JOHNSON@GMAIL.COM"
phone_parts = ["080", "123", "4567"]
cleaned_name = customer_name.strip().title()
cleaned_email = customer_email.strip().lower()
cleaned_phone = "-".join(phone_parts)
print(cleaned_name)
print(cleaned_email)
print(cleaned_phone)

Output:

Daniel Johnson
daniel.johnson@gmail.com
080-123-4567

Real-world application

These techniques are useful when cleaning customer records, standardising imported data, preparing information for comparison, and processing text from files or databases.

Status: Day 4 completed.