import json
import re

# Path to your local JSON file
json_path = "fake_smartphone_data.json"

# Load JSON data from file
with open(json_path, "r", encoding="utf-8") as file:
    data = json.load(file)

# Function to clean and convert price string to integer
def convert_price_to_int(price_str):
    # Remove any non-digit characters
    cleaned = re.sub(r"[^\d]", "", price_str)
    return int(cleaned)

# Update price field in each product
for item in data:
    if "Price" in item:
        item["Price"] = convert_price_to_int(item["Price"])

# Save updated data back to the JSON file
with open(json_path, "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4)

print("Price values converted to integers and saved.")
