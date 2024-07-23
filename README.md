

import json

# Define the path to your JSON file
json_file_path = 'your_file.json'

# Define the path to the file containing the search strings
search_strings_file_path = 'search_strings.txt'

# Read the search strings from the file
with open(search_strings_file_path, 'r') as file:
    search_strings = [line.strip() for line in file]

# Open and read the JSON file
with open(json_file_path, 'r') as file:
    json_data = json.load(file)

# Create a dictionary to store the results
results = {}

##迭代-->判断-->迭代-->判断
# Iterate through the JSON data and check for the search strings.

for obj in json_data:
    # 遍历oject kv
    for key, value in obj.items():
        # 如果value是一个list
        if isinstance(value, list):
            # 遍历所有的value，看看是否包含search_string:
            for item in value:
                for search_string in search_strings:
                    print(type(obj))
                    print(type(item))
                    print(type(value))
                    if isinstance(obj, dict):
                        if "id" in obj and obj["id"] == "procInst":
                            results[search_string].append(item)
                        break

        elif isinstance(value, str):
            for search_string in search_strings:
                    if isinstance(obj, dict):
                        if "id" in obj and obj["id"] == "procInst":
                            results[search_string].append(item)
# Generate the table
print("| Search String | Values |")
print("| --- | --- |")
for search_string, values in results.items():
    # 为什么需要这句话？
    for value in values:
        print(f"| {search_string} | {value} |")

