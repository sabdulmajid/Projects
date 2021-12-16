customer = {
    "name": "John Cuddy",
    "age": 30,
    "is_verified": True
}
customer["birthdate"] = "Dec 20 2000"
print((customer.get("birthdate")))

phone = input('Phone number:  ')
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine"
}
output = ""
for chr in phone:
    output += digits_mapping.get(chr, "Not valid!!") + ", "
print(output)

