import json

def extract_nested_json(complex_json):
    nested_json = []
    
    # 假设 complex_json 是复杂的 JSON 数据
    for server in complex_json.get("Servers", []):  # 假设有一个 "Servers" 键
        server_info = {
            "ServerName": server.get("ServerName"),
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

# 读取复杂的 JSON 文件
with open('complex_data.json', 'r') as f:
    complex_json = json.load(f)

# 构建 nested_json
nested_json = extract_nested_json(complex_json)

# 打印结果
print(json.dumps(nested_json, indent=2))
"""
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

##json to table.

import pandas as pd

def extract_process_info(obj):
    data = []
    
    if isinstance(obj, dict):
        server_name = obj.get("ServerName")
        for process in obj.get("Processes", []):
            process_name = process.get("PROCESS")
            process_str = process.get("str")
            process_min = process.get("min")
            process_max = process.get("max")
            process_owner = process.get("owner")
            data.append([server_name, process_name, process_str, process_min, process_max, process_owner])
            
    return data



# 提取数据
all_data = []
for server in nested_json:
    all_data.extend(extract_process_info(server))

# 创建 DataFrame
columns = ["ServerName", "PROCESS", "str", "min", "max", "owner"]
df = pd.DataFrame(all_data, columns=columns)

# 打印表格
print(df.to_string(index=False))



# 示例嵌套 JSON 数据,一个serverName一个object，serverName的值需要
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
