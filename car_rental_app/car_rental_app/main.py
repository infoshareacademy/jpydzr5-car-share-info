from json_handler import json_reader

# Read from the JSON file
instance_001 = json_reader(path="static/json/id_001.json")

# Print values from the instance
print(f"Brand: {instance_001['id_001']['brand']}")
print(f"Model: {instance_001['id_001']['model']}")
