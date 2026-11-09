name = "Shafii"

print(name[0])
print(name[2])
print(name[5])

name = "Shafii"

print(name[-1])
print(name[-2])
print(name[-3])

#indexing(string + slicing)

name = "Shafii"

print(name[0:3])
print(name[2:5])
print(name[:2])
print(name[3:])

#indexing(slicing in 3 values,[start:end:step])

name = "Shafii"

print(name[::2])
print(name[1::2])
print(name[::-1])

#String immutability

name = "Shafii"
name = "K" + name[1:]

print(name)

#Concatenation

#first_name = "Shafii"
#last_name = "Mohamed"

#full_name = first_name + " " + last_name

#print(full_name)

#Concatenation with variable and user input
#first_name = input("Enter your first name: ")
#last_name = input("Enter your last name: ")

#full_name = first_name + " " + last_name

#print("Welcome, " + full_name)

full_name = "Daniel Johnson"
customer_id = "CUS-2026-00845"
age = 32

print(full_name[0:6])
print(full_name[7:])
print(customer_id[-4:])

print(f"Welcome, {full_name}!")
print(f"You are {age} years old.")
print(f"Your customer ID ends in {customer_id[-4:]}")

updated_name = "David" + " " + full_name[7:]
print(updated_name)