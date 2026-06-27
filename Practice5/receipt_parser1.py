import re

with open("/Users/sanche/Desktop/pp2sum/Practice5/raw.txt", "r", encoding="utf-8") as file:
    text = file.read()
    
# Extract all prices
prices = re.findall(r"\d[\d ]*,\d{2}", text)

print("All found prices:")
for price in prices:
    print(price)

# Find product names
products = []

pattern = r"\d+\.\n(.*?)\n"

matches = re.finditer(pattern, text, re.MULTILINE)

for match in matches:
    products.append(match.group(1).strip())

print("\nName of Products:")
for p in products:
    print("-", p)

# Total amount
total = re.search(r"ИТОГО:\s*\n?([\d ]+,\d{2})", text)

if total:
    print("\nTotal:", total.group(1))

# Date and time
datetime = re.search(
    r"Время:\s*(\d{2}\.\d{2}\.\d{4})\s+(\d{2}:\d{2}:\d{2})",
    text
)

if datetime:
    print("\nDate:", datetime.group(1))
    print("Time:", datetime.group(2))

# Payment method
payment = re.search(r"(Банковская карта|Наличные)", text)

if payment:
    print("\nPayment:", payment.group(1))