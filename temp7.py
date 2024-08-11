import json
# server_info是一个字典。
# process_info也是一个dict
# proceses是个list
json_file_path = 'sample.json'
# Open and read the JSON file
process_list=[]
process_str=[]
process_min=[]
process_max=[]
process_own=[]
with open(json_file_path, 'r') as file:
    json_data = file.read()
# Read the search strings from the file


def extract_nested_json(i):
    nested_json = []
    
    # 假设 complex_json 是复杂的 JSON 数据
    for server in i.get("name", []):  # 假设有一个 "Servers" 键
        server_info = {
            "ServerName": server.get("name"),
            "Processes": []
        }
        
        for process in server.get("Processes", []):  # 假设每个服务器有一个 "Processes" 键
            process_info = {
                "PROCESS": process.get("PROCESS"),
                "str": process.get("str"),
                "min": process.get("min"),
                "max": process.get("max"),
                "owner": process.get("owner")
            }
            server_info["Processes"].append(process_info)
        
        nested_json.append(server_info)
    
    return nested_json

def traverse_json_process(obj):
    if isinstance(obj, dict):
        if "id" in obj and obj["id"] == "procInst":
            process_list.append(obj["value"])
        else:
            for value in obj.values():
                traverse_json_process(value)
    elif isinstance(obj, list):
        for item in obj:
            traverse_json_process(item)

def traverse_json_str(obj):
    if isinstance(obj, dict):
        if "id" in obj and obj["id"] == "procString":
            process_str.append(obj["value"])
        else:
            for value in obj.values():
                traverse_json_str(value)
    elif isinstance(obj, list):
        for item in obj:
            traverse_json_str(item)

def traverse_json_min(obj):
    if isinstance(obj, dict):
        if "id" in obj and obj["id"] == "procMin":
            process_min.append(obj["value"])
        else:
            for value in obj.values():
                traverse_json_min(value)
    elif isinstance(obj, list):
        for item in obj:
            traverse_json_min(item)

def traverse_json_max(obj):
    if isinstance(obj, dict):
        if "id" in obj and obj["id"] == "proc_Max":
            process_max.append(obj["value"])
        else:
            for value in obj.values():
                traverse_json_max(value)
    elif isinstance(obj, list):
        for item in obj:
            traverse_json_max(item)

def traverse_json_own(obj):
    if isinstance(obj, dict):
        if "id" in obj and obj["id"] == "procOwner":
            process_own.append(obj["value"])
        else:
            for value in obj.values():
                traverse_json_own(value)
    elif isinstance(obj, list):
        for item in obj:
            traverse_json_own(item)

# 读取复杂的 JSON 文件
for i in json_data:
    traverse_json_process(i)


def create_nested_json(server_names):
    nested_json = []
    
    for server_name in server_names:
        processes = []
        for proc, s, mn, mx, own in zip(process_list, process_str, process_min, process_max, process_own):
            process_info = {
                "PROCESS": proc,
                "str": s,
                "min": mn,
                "max": mx,
                "owner": own
            }
            processes.append(process_info)
        
        server_info = {
            "ServerName": server_name,
            "Processes": processes
        }
        nested_json.append(server_info)
    
    return nested_json

# 示例服务器名称列表
server_names = ["serverNameX", "serverNameY"]

# 生成 nested_json
nested_json = create_nested_json(server_names)
print(json.dumps(nested_json, indent=4))

df = pd.DataFrame(nested_json)
print(nested_json)





# # 构建 nested_json
# nested_json = extract_nested_json()
# # 打印结果
# print(json.dumps(nested_json, indent=2))
# """
nested_json = [
    {
        "ServerName": "serverNameX",
        "Processes": [
            {"PROCESS": "process_A", "str": "testA", "min": 25, "max": 34, "owner": "ownerx"},
            {"PROCESS": "process_B", "str": "testB", "min": 25, "max": 34, "owner": "ownery"},
            {"PROCESS": "process_C", "str": "testC", "min": 25, "max": 34, "owner": "ownery"},
        ]
    },
    {
        "ServerName": "serverNameY",
        "Processes": [
            {"PROCESS": "process_C", "str": "testA", "min": 25, "max": 34, "owner": "owneryx"},
            {"PROCESS": "process_D", "str": "test2", "min": 25, "max": 34, "owner": "owneryx"},
        ]
    }
]
"""

