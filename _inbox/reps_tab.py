customer_email = "DANIEL.JOHNSON@GMAIL.COM"
print(customer_email.lower())
print(customer_email.upper())

customer_name = "Daniel Johnson"
print(customer_name)
print(customer_name.strip())

customer_name = " Daniel Johnson"
cleaned_name = customer_name.strip()

print(customer_name)
print(cleaned_name)

customer_email = " DANIEL.JOHNSON@GMAIL.COM"
cleaned_email = customer_email.strip().lower()
print(cleaned_email)

phone_number = "080-123-4567"
cleaned_number = phone_number.replace("-", "")
print(cleaned_number)

customer_email = "daniel.johnson@gmail.com"
email_parts = customer_email.split("@")
print(email_parts)

phone_parts = ["080", "123", "4567"]
phone_number = "-".join(phone_parts)
print(phone_number)

customer_name = " DANIEL JOHNSON "
customer_email = " DANIEL.JOHNSON@GMAIL.COM"
phone_parts = ["080", "123", "4567"]

cleaned_name = customer_name.strip().title()
cleaned_email = customer_email.strip().lower()
cleaned_phone = "-".join(phone_parts)

print(cleaned_name)
print(cleaned_email)
print(cleaned_phone)
