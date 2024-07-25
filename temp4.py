import json

# Define the path to your JSON file
json_file_path = 'One_splite.json'
search_strings_file_path = 'search_strings.txt'
# Open and read the JSON file
with open(json_file_path, 'r') as file:
    json_data = file.read()
# Read the search strings from the file

with open(search_strings_file_path, 'r') as file:
    search_strings = [line.strip() for line in file]

# Parse the JSON string into a Python dictionary
data = json.loads(json_data)

# # Initialize an empty list to store the 'procInst' values
# proc_inst_values = []

# # GetProcess func. Traverse the nested JSON structure to find the 'procInst' values
# def traverse_json(obj):
#     if isinstance(obj, dict):
#         if "id" in obj and obj["id"] == "procInst":
#             proc_inst_values.append(obj["value"])
#         else:
#             for value in obj.values():
#                 traverse_json(value)
#     elif isinstance(obj, list):
#         for item in obj:
#             traverse_json(item)

# Call the traverse_json function with the top-level JSON object

# 查看是否包含server_Name函数


for obj in data:
    print(type(obj))
