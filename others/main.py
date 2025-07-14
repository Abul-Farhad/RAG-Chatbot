import json

# Input and output file paths
input_file = 'products.json'           # Your original JSON file
output_file = 'products_fixture.json'  # Fixture file for Django

# Load original data
with open(input_file, 'r') as f:
    data = json.load(f)

# Convert to Django fixture format
fixture = []
for idx, item in enumerate(data, start=1):
    fixture.append({
        "model": "chatbot.product",
        "pk": idx,
        "fields": {
            "brand": item["Brand"],
            "model": item["Model"],
            "price": item["Price"],
            "quantity": item["Quantity"],
            "reviews": item["reviews"]
        }
    })

# Write the fixture data
with open(output_file, 'w') as f:
    json.dump(fixture, f, indent=4)

print(f"✅ Converted and saved as {output_file}")
