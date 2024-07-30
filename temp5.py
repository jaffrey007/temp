import json  # 导入 json 模块以处理 JSON 数据

# 从 JSON 文件中读取数据
with open('data.json', 'r') as json_file:  # 打开 data.json 文件进行读取
    json_object = json.load(json_file)  # 将 JSON 数据加载到 Python 对象中

# 定义递归函数来提取进程信息
def extract_processes(details):
    processes = []  # 创建一个空列表来存储进程名称
    for item in details:  # 遍历每个项
        if item['id'] == 'processes':  # 检查当前项的 id 是否为 'processes'
            processes.append(item['value'])  # 如果是，则将其值添加到 processes 列表中
        if 'details' in item and item['details']:  # 检查是否有嵌套的 details
            processes.extend(extract_processes(item['details']))  # 递归调用以提取嵌套进程
    return processes  # 返回提取的进程列表

# 从文件中读取主机名
with open('hostname.txt', 'r') as file:  # 打开 hostname.txt 文件进行读取
    hostnames = [line.strip() for line in file.readlines()]  # 读取所有行并去除空白字符

# 创建表格
table = []  # 创建一个空列表来存储结果

for entry in json_object:  # 遍历 JSON 对象中的每个条目
    hostname = entry['name']  # 获取当前条目的主机名
    if hostname in hostnames:  # 检查主机名是否在 hostnames 列表中
        processes = extract_processes(entry['details'])  # 提取当前条目的进程信息
        process_list = ','.join(processes)  # 将进程列表转换为以逗号分隔的字符串
        table.append((hostname, process_list))  # 将主机名和进程字符串添加到表格中

# 打印表格
print(f"{'hostname':<15} {'process'}")  # 打印表头
for hostname, process in table:  # 遍历表格中的每一行
    print(f"{hostname:<15} {process}")  # 打印主机名和对应的进程信息
