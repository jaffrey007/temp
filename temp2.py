import json

def contains_string(data, search_string):
    # 如果是字典，遍历每个键值对
    if isinstance(data, dict):
        # print("this is a dict")
        for key, value in data.items():
            if contains_string(value, search_string):  # 递归调用
                return True
    # 如果是列表，遍历每个元素
    elif isinstance(data, list):
        # print("this is a list")
        for item in data:
            if contains_string(item, search_string):  # 递归调用
                return True
    # 如果是字符串，检查是否包含目标字符串
    elif isinstance(data, str):
        # print("this is a str")
        return search_string in data

    return False  # 如果没有找到，返回 False


# 示例 JSON 数据，包含嵌套对象
json_data = {
    "name": "Alice",
    "age": 30,
    "address": {
        "city": "Wonderland",
        "zipcode": "12345",
        "coordinates": {
            "lat": 12.34,
            "long": 56.78
        }
    },
    "hobbies": [
        "reading",
        {
            "type": "traveling",
            "details": {
                "destination": "Wonderland",
                "duration": "2 weeks"
            }
        },
        "coding"
    ]
}

# 查找字符串
search_str = "Wonder"
if contains_string(json_data, search_str):
    print(f"Found '{search_str}' in the JSON data.")
else:
    print(f"'{search_str}' not found in the JSON data.")
