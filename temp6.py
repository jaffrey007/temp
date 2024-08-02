import json

# 读取JSON文件
with open('sample.json', 'r') as file:
    data = json.load(file)
print(type(data))
print('当前json数据\n',data)
res_dic = {}
num = 1
for i in data:
    processes_list = []
    for key,value in i.items():
        if key=='details':
            for val in value:
                processes_value = val.get('value')
                processes_list.append(processes_value)
                processes_value2 = val.get('details')[0].get('value')
                processes_list.append(processes_value2)
    res_dic[i.get('name')] = processes_list
    print(f'第{num}object内的数据',processes_list)
    num+=1
print(res_dic)
