country = input("Please Enter your country: ")

if country.lower() == "canada":
    province = input("What province do you live in: ")
    if province in ("Alberta","Nanvaut", "Yukon"):
        tax = 0.05
    elif province == "Ontario":
        tax = 0.13
    else:
        tax = 0.15
else:
    tax = 0

print(tax)