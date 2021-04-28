import os
import shutil


def duplicate(src, path):
    shutil.copyfile(src, path, follow_symlinks = False)


def mkdir(dirname = r"./test"):
    key_path = r"/Key"
    output_path = r"/Output"
    sql_path = r"/SQL"
    
    src_of_tool = "./tool.py"
    path_of_tool = dirname + r"/tool.py"
    
    src_of_prototype = "./prototype.py"
    path_of_prototype = dirname + r"/main.py"
    
    try:  
        os.makedirs(dirname + key_path)
        print(key_path+"目录创建成功")
    except FileExistsError:
        print(key_path+"目录存在")
        
    try:  
        os.makedirs(dirname + output_path)
        print(output_path+"目录创建成功")
    except FileExistsError:
        print(output_path+"目录存在")
        
    try:  
        os.makedirs(dirname + sql_path)
        print(sql_path+"目录创建成功")
    except FileExistsError:
        print(sql_path+"目录存在")
        
    key_origin_name = r"/origin.json"
    key_test_name = r"/test.json"
    
    if os.path.exists(dirname + key_path + key_origin_name)==0:
        file = open(dirname + key_path + key_origin_name, 'w')
        file.write('[{"database":,"user":,"password":,"host":,"port":}]')
        file.close()
        print(key_origin_name+"文件创建成功")
    else:
        print(key_origin_name+"文件存在")
        
    if os.path.exists(dirname + key_path + key_test_name)==0:
        file = open(dirname + key_path + key_test_name, 'w')
        file.write('[{"database":,"user":,"password":,"host":,"port":}]')
        file.close()
        print(key_test_name+"文件创建成功")
    else:
        print(key_test_name+"文件存在")

    duplicate(src_of_tool,path_of_tool)
    duplicate(src_of_prototype,path_of_prototype)

dirname = input("dirname:")
mkdir(dirname)