import json

# 读取 wetab.txt 文件内容
with open('wetab.txt', 'r', encoding='utf-8') as file:
    wetab_data = json.load(file)

# 创建一个新的字典，用于存储转换后的数据
itab_new_data = {
    "navConfig": []
}

# 遍历 wetab_data 中的每个元素
for category in wetab_data['data']['store-icon']['icons']:
    # 创建一个新的字典，用于存储当前类别的信息
    category_info = {
        "id": category['id'],
        "name": category['name'],
        "icon": "icon-" + category['name'],
        "children": []
    }
    
    # 遍历当前类别的子元素
    for child in category['children']:
        # 创建一个新的字典，用于存储子元素的信息
        child_info = {
            "id": child['id'],
            "type": "icon",
            "name": child['name'],
            "src": child.get('bgImage', ""),  # 使用 get 方法，如果 'bgImage' 不存在，则返回空字符串
            "backgroundColor": "transparent"
        }
        
        # 检查 'target' 键是否存在，如果存在则添加到 child_info 中
        if 'target' in child:
            child_info['url'] = child['target']
        
        # 如果存在文件夹形式的元素，需要保留
        if 'folderSize' in child:
            child_info['type'] = 'folder'
            child_info['children'] = []
            for folder_child in child['children']:
                # 创建文件夹子元素的信息
                folder_child_info = {
                    "id": folder_child['id'],
                    "url": folder_child.get('target', ""),  # 使用 get 方法，如果 'target' 不存在，则返回空字符串
                    "type": "icon",
                    "name": folder_child['name'],
                    "src": folder_child.get('bgImage', ""),  # 使用 get 方法，如果 'bgImage' 不存在，则返回空字符串
                    "backgroundColor": "transparent"
                }
                child_info['children'].append(folder_child_info)
    
        # 将子元素添加到当前类别的 children 列表中
        category_info['children'].append(child_info)
    
    # 将当前类别的信息添加到 itab_new_data 中
    itab_new_data['navConfig'].append(category_info)

# 将转换后的数据写入到 itab-new.txt 文件中
with open('itab-new.txt', 'w', encoding='utf-8') as file:
    json.dump(itab_new_data, file, ensure_ascii=False, indent=4)

print("转换完成，文件已保存为 itab-new.txt")