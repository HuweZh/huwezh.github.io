import base64
import os
import re
import shutil

# 获取路径下的所有文件
def get_md_file():
    path = os.path.abspath(os.path.dirname(os.getcwd()))
    md_path = path + "/docs/md/"

    files = os.listdir(md_path)  # 获得文件夹中所有文件的名称列表

    result = []
    # 遍历下属的文件夹，获取md文件
    for file in files:
        sub_path = md_path+"/"+file
        sub_files = os.listdir(sub_path)
        for sub_file in sub_files:
            if ".md" in sub_file:
                result.append(sub_path+"/"+sub_file)
    return result

# 转为base64编码字符串


def trans_2_base64(file_name):
    f = open(file_name, 'rb')  # 二进制方式打开图文件
    ls_f = base64.b64encode(f.read())  # 读取文件内容，转换为base64编码
    f.close()
    return ls_f.decode('utf-8')

# 获取文件中的图片文件


def get_image_file(file):
    # 最小匹配，匹配括号
    min_bracket = re.compile(r'[(](.*?)[)]', re.S)

    # 拿到括号内的内容
    result = []
    # for file_name in file_names:
    f = open(file)
    for line in f:  # 遍历文件，一行行读取，并添加到s中
        content_list = re.findall(min_bracket, line)
        for content in content_list:
            if ".jpg" in content or ".png" in content or ".jpeg" in content:
                result.append(content)
    f.close()
    return result

# 获取图片文件对应的编码
def get_image_map(file):
    image_map = {}
    # 当前的md文件
    images = get_image_file(file)
    for image in images:
        image_map[image] = trans_2_base64(get_md_file_prefix(file) + image)
    return image_map    


def get_md_file_prefix(file):
    index = file.rfind("/")
    return file[0:index+1]

# 生成一个新的文件
def create_new_md_file (file_name, new_file_name):
    image_map = get_image_map(file_name)
    target_file = open(new_file_name, "w")
    origin_file = open(file_name)
    for line in origin_file:
        # 对每一行都进行替换
        for key in image_map:
            if key in line:
                target_file.write(line.replace(key, "data:image/png;base64,"+image_map[key]))
            else:
                target_file.write(line)
    origin_file.close()
    target_file.close()

# build project
def build_project():
    os.system("cd D:\workspace\HuweZh.github.io")
    os.system("npm run build")
    
    # 复制dist文件夹到docs
    shutil.rmtree("D:\workspace\HuweZh.github.io\docs")
    # os.mkdir()
    shutil.copytree("D:\workspace\HuweZh.github.io\dist","D:\workspace\HuweZh.github.io\docs")
    shutil.rmtree("D:\workspace\HuweZh.github.io\dist")
build_project()