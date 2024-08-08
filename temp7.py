import json  # 导入json模块，用于处理JSON数据
# import pandas as pd
# 读取JSON文件
with open('4.json', 'r') as file:  # 以只读模式打开名为'your_file.json'的文件
    data = json.load(file)  # 将文件中的JSON数据加载到变量data中

res_dic = []  # 初始化一个空列表，用于存储结果
process_list=[]


def contains_key_value(d, key, value):
    """
    递归检查字典中是否存在特定的键值对。
    
    :param d: 要检查的字典
    :param key: 要查找的键
    :param value: 要查找的值
    :return: 如果找到，则返回True，否则返回False
    """
    if isinstance(d, dict):  # 检查是否是字典
        if key in d and d[key] == value:  # 检查是否存在该键值对
            return True
        for k, v in d.items():  # 遍历字典的每个键值对
            if isinstance(v, (dict, list)):  # 如果值是字典或列表，递归调用
                if contains_key_value(v, key, value):
                    return True
    elif isinstance(d, list):  # 如果是列表
        for item in d:
            if contains_key_value(item, key, value):  # 对每个项递归调用
                return True
    return False  # 如果未找到，返回False


# AttributeError: 'NoneType' object has no attribute 'append'
"""
遍历JSON对象，查找进程集合。
"""
# 在单个的object中有效,获取进程集合，这个函数有问题：没有获取到process list。只是单个字母。
def traverse_json(obj):
    results = []  # 用于存储所有符合条件的进程实例
    if isinstance(obj, dict):  # 如果对象是字典
        if "id" in obj and obj["id"] == "procInst":  # 检查是否为进程实例
            results.append(obj["value"])  # 将找到的进程集合添加到结果列表中
        else:
            for value in obj.values():  # 遍历字典的每个值
                results.extend(traverse_json(value))  # 递归调用并合并结果
    elif isinstance(obj, list):  # 如果对象是列表
        for item in obj:
            results.extend(traverse_json(item))  # 递归调用并合并结果
    return results  # 返回所有找到的结果
    """
    遍历JSON对象，提取进程信息（字符串、最大值、最小值和所有者）。
    """
""" 
dict list.
process_item = [
    {'proc1': [proc1_str, proc1_min, proc1_max, proc1_owner]},
    {'proc2': [proc2_str, proc2_min, proc2_max, proc2_owner]},
    {'proc3': [proc3_str, proc3_min, proc3_max, proc3_owner]}
]

 """
# 获取进程字符串、最大值、最小值和所有者
def traverse_proc_info(obj):

    proc_info = {}  # 初始化一个字典用于存储进程各个信息
    if isinstance(obj, dict):  # 如果对象是字典
    # 逻辑是错的！
        if "id" in obj:  # 检查是否有'id'字段
            if obj["id"] == "procString":  # 检查是否为进程字符串
                proc_info['proc_str'] = obj["value"]  # 保存进程字符串
            elif obj["id"] == "procMaxCnt":  # 检查是否为最大计数
                proc_info['proc_max'] = obj["value"]  # 保存最大值
            elif obj["id"] == "procMinCnt":  # 检查是否为最小计数
                proc_info['proc_min'] = obj["value"]  # 保存最小值
            elif obj["id"] == "procOwner":  # 检查是否为所有者
                proc_info['proc_owner'] = obj["value"]  # 保存所有者
        for value in obj.values():  # 遍历字典的每个值
            child_info = traverse_proc_info(value)  # 递归调用
            if child_info:  # 如果找到了子信息
                proc_info.update(child_info)  # 更新进程信息
    elif isinstance(obj, list):  # 如果对象是列表
        for item in obj:
            child_info = traverse_proc_info(item)  # 递归调用
            if child_info:  # 如果找到了子信息
                proc_info.update(child_info)  # 更新进程信息
    return proc_info  # 返回进程信息

# 遍历data中的每个对象
for i in data:
    if contains_key_value(i,"monitoringProfile", "Unix_Processes"):
        process_list = traverse_json(i)  # 获取进程集合
        if process_list:  # 如果找到了进程集合
            for proc_item in process_list:  # 打印每个进程
                # print(proc_item)
                process_info = traverse_proc_info(i)  # 获取进程信息
                if process_info:  # 如果找到了进程信息
                    # 创建字典，包含进程名称及其相关信息
                    res_dict = {
                        proc_item: [
                            process_info.get('proc_str'), 
                            process_info.get('proc_min'), 
                            process_info.get('proc_max'), 
                            process_info.get('proc_owner')
                        ]
                    }
                    res_dic.append(res_dict)  # 将结果添加到res_dic

# 打印最终的结果列表，以易于阅读的JSON格式输出
print(json.dumps(res_dic, ensure_ascii=False, indent=4))  # 使用indent参数格式化输出

#问题：sendmail的procString为什么是udevd？




