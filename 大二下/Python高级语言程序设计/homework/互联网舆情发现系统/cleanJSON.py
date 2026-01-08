import os

directories = ['./Keywords', './Topics', './User']

for directory in directories:
    if not os.path.exists(directory):
        print(f"目录 {directory} 不存在，跳过...")
        continue
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path) and filename.endswith('.json'):
            try:
                os.remove(file_path)
                print(f"已删除: {file_path}")
            except Exception as e:
                print(f"无法删除 {file_path}: {e}")
print("JSON 文件清理完成。")