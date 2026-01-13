import re
import json

data = [
    " Harish,25,Hyderabad ",
    "Anil, ,Bangalore",
    "Ravi,30, ",
    " ,22,Chennai",
    "Sita,28,Delhi"
]

name_pattern = re.compile(r'^[A-Za-z]+$')
age_pattern = re.compile(r'^\d+$')
city_pattern = re.compile(r'^[A-Za-z]+$')


cleaned_data = []

for record in data:
    if not record:
        continue

    record = record.strip()

    parts = [p.strip() for p in record.split(",")]

    if len(parts)!=3:
        continue

    name,age,city = parts

    if not name_pattern.fullmatch(name):
        continue
    if not age_pattern.fullmatch(age):
        continue
    if not city_pattern.fullmatch(city):
        continue

    cleaned_data.append(
        {
            "name":name,
            "age":int(age),
            "city":city
        }
    )
print(json.dumps(cleaned_data,indent=4))
